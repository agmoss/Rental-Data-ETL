import logging
import mysql.connector
import sys
import re

import pandas as pd


def db_config():
    """Setup"""

    import json

    with open('config.json', 'r') as f:
        config = json.load(f)

    host = config['DATABASE_CONFIG']['host']
    user = config['DATABASE_CONFIG']['user']
    password = config['DATABASE_CONFIG']['password']
    db = config['DATABASE_CONFIG']['dbname']

    return host, user, password, db


def connect():
    """ Connect to MySQL database """

    while True:

        try:
            host, user, password, db = db_config()

            conn = mysql.connector.connect(host=host,
                                        database=db,
                                        user=user,
                                        password=password)

        except mysql.connector.errors.ProgrammingError as e:

            if e.errno == 1049:  # Database not created yet
                create_db()
                connect()
            elif e.errno == 1045:
                logging.info("FATAL: Access denied: password or db name incorrect")
                logging.info(e)
                sys.exit(-1)
            else:
                logging.info(e)
                raise

        except mysql.connector.errors.InterfaceError as e:
            logging.info(e)
            raise

        except Exception as ex:
            logging.info(ex)
            raise

        else:
            return conn


def create_db():
    try:
        host, user, password, db = db_config()

        conn = mysql.connector.connect(host=host,
                                       user=user,
                                       password=password)

        mycursor = conn.cursor()

        mycursor.execute("CREATE DATABASE " + db)

        logging.info('Database created')

    except Exception as ex:  # TODO: Handle this
        logging.info(ex)
        raise


def create_table(conn):
    try:

        # Determine if table already exists
        mycursor = conn.cursor()
        mycursor.execute("SHOW TABLES")

        if "rental_data" in mycursor:
            raise ("Table already in existence")

        mycursor.execute(
            "CREATE TABLE rental_data (address VARCHAR(255), address_hidden INT, availability VARCHAR(255), avdate VARCHAR(255),"
            "baths INT, bedrooms INT, cats INT, city VARCHAR(255), community VARCHAR(255), den VARCHAR(255), dogs INT,"
            "email INT, id INT, intro VARCHAR(255), latitude DECIMAL, link VARCHAR(255), location VARCHAR(255), longitude DECIMAL,"
            "marker VARCHAR(255), phone VARCHAR(255), phone_2 VARCHAR(255), preferred_contact VARCHAR(255),"
            "price DOUBLE, province VARCHAR(255), quadrant VARCHAR(255), ref_id VARCHAR(255) PRIMARY KEY, rented VARCHAR(255),"
            "slide VARCHAR(255), sq_feet DECIMAL, status VARCHAR(255), thumb VARCHAR(255), thumb2 VARCHAR(255), title VARCHAR(255),"
            "type VARCHAR(255),	userId INT, utilities_included VARCHAR(255), website VARCHAR(255), retrieval_date VARCHAR(255))") 

        logging.info("Table created")

    except Exception as ex:
        logging.info(ex)
        raise


def insert(db, val, sql):
    """Insert the list of records"""

    while True:

        try:
            my_cursor = db.cursor()
            my_cursor.execute(sql, val)
            db.commit()
            logging.info('Record inserted')
            break

        except mysql.connector.errors.ProgrammingError as e:

            if e.errno == 1146:  # Database table not created yet
                create_table(db)
                
            elif e.errno == 1054:
                logging.info('Bad record, not updated or inserted')
                logging.info(e)
                logging.info(type(e))
                break #TODO: These errors are caused by nan's in the df. They are just null values. Find a way to insert them as null
            else:
                raise # Unhandled exception

        except mysql.connector.errors.IntegrityError as ie:

            if ie.errno == 1062: # Duplicate entry

                # Get the error message
                string = str(ie.args[1])

                # Remove the error code 
                string = string.split(':', 1)[-1]

                # Get the PK that caused the error
                string = re.findall(r"'(.*?)'", string, re.DOTALL)
                
                sql = "UPDATE rental_data SET retrieval_date = %s WHERE ref_id = %s"
                val = (str(pd.to_datetime('today').strftime("%m/%d/%Y")), string[0])

                my_cursor.execute(sql, val)
                db.commit()

                logging.info("Duplicate Entry, PK updated " + string[0])
                break
                #TODO: Make this into a real update

            else:
                logging.info('Record unable to be updated')
                logging.info(ie.args)
                pass 

        except Exception as ex:  # TODO Expand on exception handling (there should be some mysql error objects to access)
            logging.info(ex)
            logging.info(type(ex))
            raise #Unhandled exception

        else:
            break


def sql_writer_insert(table_name, header_list):
    """Generate a custom SQL insert statement"""

    s_list = []

    for i in range(len(header_list)):
        s_list.append('%s')

    # Convert
    header_list = ','.join(map(str, header_list))
    s_list = ','.join(map(str, s_list))

    sql = "INSERT INTO " + table_name + " (" + header_list + ") " + "VALUES" + " (" + s_list + ")" 

    return sql


if __name__ == '__main__':
    connect()
