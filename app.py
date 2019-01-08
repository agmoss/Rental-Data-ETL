import logging
import pandas as pd
import re

from scripts import Database
from scripts import Accessor
from scripts import Rental

import mysql.connector


def main():
    """Extract, Transform, Load"""

    logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info('Start')

    i = 0 #Loop counter

    while True:

        try:

            page = str(i)

            url = 'https://www.rentfaster.ca/api/search.json?keywords=&proximity_type=location-proximity&cur_page=' + page + '&beds=&type=&price_range_adv[from]=null&price_range_adv[to]=null&novacancy=0&city_id=1'

            # Access object
            scr = Accessor.Accessor(url)

            data = scr.get_json()

            # There are multiple keys that can be accessed at this level, we want the listings data
            listings = data['listings']

            # We have reached the last page
            if len(listings) == 0:
                break
            
            # We have not reached the last page
            i += 1
                
            logging.info("Page " + page + " data obtained")

            # Connect to the database (exception raised if not connected)
            conn = Database.Database.connect()
            
            for listing in listings:

                try:

                    # Data Cleaning
                    listing['sq_feet'] = re.sub("[^0-9]", "", listing['sq_feet'])

                    listing['bedrooms'] = listing['bedrooms'].replace('bachelor', "0")
                    
                    listing['retrieval_date'] = pd.to_datetime('today').strftime("%m/%d/%Y")

                    # Convert the list to a CSV string
                    listing['utilities_included'] = ",".join([str(x) for x in listing['utilities_included']]) 

                    # Remove whitespace 
                    listing['utilities_included'] = listing['utilities_included'].strip()

                    # Remove trailing comma
                    listing['utilities_included'] = listing['utilities_included'].rstrip(',')

                    db = Database.Database.db_config()[3]

                    # Prepare a statement
                    statement = Database.Database.sql_writer_insert(db, listing.keys())
                    
                    # Instantiate Object
                    rental = Rental.Rental(listing["ref_id"],listing["userId"], listing["id"] ,listing["title"] ,listing["price"],listing["type"] ,
                    listing["sq_feet"],listing["availability"],listing["avdate"],listing["location"] ,listing["rented"] ,listing["thumb"] , listing["thumb2"] ,
                    listing["slide"] , listing["link"] ,listing["latitude"] , listing["longitude"],listing["marker"] ,listing["address"], listing["address_hidden"],  
                    listing["city"] ,listing["province"] , listing["intro"] , listing["community"] ,listing["quadrant"] , listing["phone"] , listing["phone_2"] ,
                    listing["preferred_contact"] ,listing["website"], listing["email"] , listing["status"] , listing["bedrooms"] , listing["den"] ,listing["baths"] , 
                    listing["cats"] , listing["dogs"] ,listing['utilities_included'], listing["retrieval_date"])

                    Database.Database.insert(conn, rental, statement) # exception NOT raised if data not inserted

                # Duplicate entry
                except mysql.connector.errors.IntegrityError as ie: # TODO: Custom raise

                    if ie.errno == 1062: # Duplicate entry

                        statement = Database.Database.sql_writer_update(db, list(rental.__dict__.keys()))
                        Database.Database.update(conn, rental, statement)

                except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    logging.info(message)
                    continue

            conn.close()

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            logging.info(message)
            raise

        finally:
            logging.info("Page complete")

    logging.info("Au revoir")

if __name__ == "__main__":
    main()
    # TODO: Handle raised exceptions
    # TODO: Write tests