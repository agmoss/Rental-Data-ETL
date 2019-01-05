import logging
import mysql.connector
import sys
import re
import pandas as pd


class Database:

    @staticmethod
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

    @staticmethod
    def connect():
        """ Connect to MySQL database """

        while True:

            try:
                host, user, password, db = Database.db_config()

                conn = mysql.connector.connect(host=host,
                                            database=db,
                                            user=user,
                                            password=password)

            except mysql.connector.errors.ProgrammingError as e:

                if e.errno == 1049:  # Database not created yet
                    Database.create_db()
                    Database.connect()
                elif e.errno == 1045:
                    logging.info("FATAL: Access denied: password or db name incorrect")
                    logging.info(e)
                    sys.exit(-1)
                else:
                    logging.info(e)
                    raise

            except mysql.connector.errors.InterfaceError as e:

                if e.errno == 2003: # A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond)
                    logging.info("FATAL: Cannot connect to the database, ensure that port 3306 is open and the cloud db is online")
                    logging.info(e)
                    sys.exit(-1)
                else:
                    raise

            except Exception as ex:
                logging.info(ex)
                raise

            else:
                return conn

    @staticmethod
    def create_db():
        try:
            host, user, password, db = Database.db_config()

            conn = mysql.connector.connect(host=host,
                                        user=user,
                                        password=password)

            mycursor = conn.cursor()

            mycursor.execute("CREATE DATABASE " + db)

            logging.info('Database created')

        except Exception as ex:  # TODO: Handle this
            logging.info(ex)
            raise

    @staticmethod
    def create_table(conn):
        try:

            db = Database.db_config()[3]

            # Determine if table already exists
            mycursor = conn.cursor()
            mycursor.execute("SHOW TABLES")

            if db in mycursor:
                raise ("Table already in existence")

            mycursor.execute(
                "CREATE TABLE " + db + " (ref_id VARCHAR(255) PRIMARY KEY,userId INT,id INT,title VARCHAR(255),price DOUBLE,type VARCHAR(255),"
                "sq_feet DECIMAL,availability VARCHAR(255),avdate VARCHAR(255), location VARCHAR(255),rented VARCHAR(255),"
                "thumb VARCHAR(255), thumb2 VARCHAR(255),slide VARCHAR(255),link VARCHAR(255),latitude DOUBLE(20,10),longitude DOUBLE(20,10),marker VARCHAR(255),"
                "address VARCHAR(255),address_hidden INT,city VARCHAR(255),province VARCHAR(255),intro VARCHAR(255), community VARCHAR(255),"
                "quadrant VARCHAR(255),phone VARCHAR(255),phone_2 VARCHAR(255),preferred_contact VARCHAR(255),website VARCHAR(255),"
                "email INT,status VARCHAR(255),bedrooms INT,den VARCHAR(255),baths INT,cats INT,dogs INT,utilities_included VARCHAR(255),"
                "retrieval_date VARCHAR(255))") 

            logging.info("Table created")

        except Exception as ex:
            logging.info(ex)
            raise

    @staticmethod
    def insert(db, obj, sql):
        """Insert the list of records"""

        # Get the member variables as a tuple
        val = tuple(obj.__dict__.values())

        while True:

            try:
                my_cursor = db.cursor()
                my_cursor.execute(sql, val)
                db.commit()
                logging.info('Record inserted')
                break

            except mysql.connector.errors.ProgrammingError as e:

                if e.errno == 1146:  # Database table not created yet
                    Database.create_table(db)
                    
                elif e.errno == 1054:
                    logging.info('Bad record, not updated or inserted')
                    logging.info(e)
                    logging.info(type(e))
                    break #TODO: These errors are caused by nan's in the df. They are just null values. Find a way to insert them as null

                else:
                    logging.info(e)
                    logging.info(type(e))
                    break

            except mysql.connector.errors.IntegrityError as ie:

                if ie.errno == 1062: # Duplicate entry

                    logging.info("Duplicate entry")
                    break
                    #TODO: Make this into a real update

                else:
                    logging.info('Record unable to be updated')
                    logging.info(ie.args)
                    break

            except Exception as ex:  # TODO Expand on exception handling (there should be some mysql error objects to access)
                logging.info(ex)
                logging.info(type(ex))
                break

            else:
                break

    @staticmethod
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
    print(__name__)
