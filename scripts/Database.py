import logging
import mysql.connector
import sys
import re
import pandas as pd

logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


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
                "CREATE TABLE " + db + " (ref_id VARCHAR(255) PRIMARY KEY,userId INT DEFAULT NULL,id INT,title VARCHAR(255) DEFAULT NULL ,price DOUBLE DEFAULT NULL,type VARCHAR(255) DEFAULT NULL,"
                "sq_feet DECIMAL DEFAULT NULL,availability VARCHAR(255) DEFAULT NULL, avdate VARCHAR(255) DEFAULT NULL, location VARCHAR(255) DEFAULT NULL, rented VARCHAR(255) DEFAULT NULL,"
                "thumb VARCHAR(255) DEFAULT NULL, thumb2 VARCHAR(255) DEFAULT NULL,slide VARCHAR(255) DEFAULT NULL,link VARCHAR(255) DEFAULT NULL,latitude DOUBLE(20,10) DEFAULT NULL,longitude DOUBLE(20,10) DEFAULT NULL,marker VARCHAR(255) DEFAULT NULL,"
                "address VARCHAR(255) DEFAULT NULL,address_hidden INT DEFAULT NULL,city VARCHAR(255) DEFAULT NULL,province VARCHAR(255) DEFAULT NULL,intro VARCHAR(255) DEFAULT NULL, community VARCHAR(255) DEFAULT NULL,"
                "quadrant VARCHAR(255) DEFAULT NULL,phone VARCHAR(255) DEFAULT NULL,phone_2 VARCHAR(255) DEFAULT NULL,preferred_contact VARCHAR(255) DEFAULT NULL,website VARCHAR(255) DEFAULT NULL,"
                "email INT DEFAULT NULL,status VARCHAR(255) DEFAULT NULL,bedrooms INT DEFAULT 0,den VARCHAR(255) DEFAULT NULL,baths INT DEFAULT NULL,cats INT DEFAULT NULL,dogs INT DEFAULT NULL,utilities_included VARCHAR(255) DEFAULT NULL,"
                "position VARCHAR(255) NOT NULL, retrieval_date VARCHAR(255) NOT NULL)") 

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
                    raise #TODO: Custom raise? 

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
    def update(db, obj, sql):
        """Insert the list of records"""

        # List of attribute values
        lis = list(obj.__dict__.values())

        # Remove ref_id
        first = lis.pop(0)

        # Remove retrieval_date
        del lis[-1]

        # Remove position
        del lis[-1]

        # Add ref_id to the end 
        lis.append(first)

        # Convert to tuple for update
        val = tuple(lis)

        while True:

            try:
                my_cursor = db.cursor()
                my_cursor.execute(sql,val)
                db.commit()
                logging.info('Record Updated')
                break
            except Exception as ex: 
                logging.info(ex)
                logging.info(type(ex))
                break

    @staticmethod
    def key_status(db, key_list):
        """UNTESTED Update status to inactive if a database record is no longer present in the API data."""

        cur = db.cursor(buffered=True)

        cur.execute("SELECT ref_id, position FROM rental_data")
        row = cur.fetchone()
        while row is not None:

            if row[0] not in key_list:

                # Update

                val = (row[0],)

                sql = "UPDATE rental_data SET position = 'inactive' WHERE ref_id = %s" 

                mycursor = db.cursor()

                mycursor.execute(sql,val)

                db.commit()

                logging.info("Record updated to inactive")

            row = cur.fetchone()

        cur.close()
        db.close()

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

    @staticmethod
    def sql_writer_update(table_name, header_list):
        """Generate a custom SQL update statement"""

        # Remove ref_id
        header_list.pop(0)

        # Remove retrieval_date
        del header_list[-1]

        # Remove position
        del header_list[-1]

        # Add the s' to each header
        header_list = [s + "=%s" for s in header_list]

        # Convert
        header_list = ','.join(map(str, header_list))

        sql = "UPDATE " + table_name + " SET " + header_list +  " WHERE ref_id =%s "

        return sql


if __name__ == '__main__':
    print(__name__)
    # TODO: Clean up the update hack