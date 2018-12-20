import logging
import pandas as pd
from pandas.io.json import json_normalize

from scripts import db_functions as db
from scripts import get


def main():
    """Main method of the program"""

    logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info('Start')

    frames = []

    # Pagination
    for i in range(10):

        try:

            page = str(i)

            url = 'https://www.rentfaster.ca/api/search.json?keywords=&proximity_type=location-proximity'
            '&cur_page=' + page + '&beds=&type=&price_range_adv[from]=null&price_range_adv[to]=null&novacancy=0&city_id=1'

            # Access object
            scr = get.Accessor(url)

            data = scr.get_json()

            # There are multiple keys that can be accessed at this level, we want the listings data
            listings = data['listings']

            # Convert to a dataframe
            df = json_normalize(listings)

            # Append to the list of dataframes
            frames.append(df)

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            logging.info(message)
            raise

        finally:

            df = pd.concat(frames, axis=0)

            # TODO: The utilities column has [] around its contents, mysql thinks its a list within a list...
            df.drop(['utilities_included'], axis=1, inplace=True)

            # Convert to list
            total_data = df.apply(lambda x: x.tolist(), axis=1)

    try:
        # Connect to the database (exception raised if not connected)
        conn = db.connect()

        # Prepare a statement
        statement = db.sql_writer_insert('rental_data', list(df))

        for row in total_data:
            db.insert(conn, row, statement)  # exception raised if data not inserted
            logging.info('Record inserted')

        conn.close()

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        logging.info(message)
        raise

    finally:
        logging.info("Au revoir")


if __name__ == "__main__":
    main()
    # TODO: Handle raised exceptions
    # TODO: Write tests
