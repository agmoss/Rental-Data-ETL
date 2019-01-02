import logging
import pandas as pd
import re

from scripts import db_functions as db
from scripts import Accessor
from scripts import Rental


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
            conn = db.connect()

            for x in listings:

                try:

                    x['sq_feet'] = re.sub("[^0-9]", "", x['sq_feet'])

                    x['bedrooms'] = x['bedrooms'].replace('bachelor', "0")
                    
                    x['retrieval_date'] = pd.to_datetime('today').strftime("%m/%d/%Y")

                    # Prepare a statement
                    statement = db.sql_writer_insert('rental_data', x.keys())
                    
                    # Instantiate Object
                    rental = Rental.Rental(x["ref_id"],x["userId"], x["id"] ,x["title"] ,x["price"],x["type"] ,
                    x["sq_feet"],x["availability"],x["avdate"],x["location"] ,x["rented"] ,x["thumb"] , x["thumb2"] ,
                    x["slide"] , x["link"] ,x["latitude"] , x["longitude"],x["marker"] ,x["address"], x["address_hidden"],  
                    x["city"] ,x["province"] , x["intro"] , x["community"] ,x["quadrant"] , x["phone"] , x["phone_2"] ,
                    x["preferred_contact"] ,x["website"], x["email"] , x["status"] , x["bedrooms"] , x["den"] ,x["baths"] , 
                    x["cats"] , x["dogs"] ,"null", x["retrieval_date"])

                    db.insert(conn, rental, statement)  # exception NOT raised if data not inserted

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