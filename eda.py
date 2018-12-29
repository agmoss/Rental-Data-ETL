import logging
import numpy as np
import time
import pandas as pd
import mysql.connector


from scripts import db_functions as db
from scripts import plot as p
from scripts import plotly_plots as pl

def read_data():
    # Read in the data from db
    try:

        # Database connection 
        conn = db.connect()

        # Read in a dataframe from the rentfaster database
        df = pd.read_sql('SELECT * FROM rental_data', con=conn)

        # Not of use for analysis: intro, link, marker, phone, phone_2, preferred_contact, slide, thumb, thumb_2, title, website

        df.drop(['intro','link','marker','phone','phone_2','preferred_contact','slide','thumb','thumb2','title','website'],axis = 1,inplace = True)

        # Variables
        # discrete categorical attributes: address, availability, avdate, dity, community, den, location, province, quadrant, rented, status, type, utilities_included
        # discrete numeric attributes: address_hidden,baths,bedroons,cats,dogs, email, id, ref_id, userId
        # continuous attributes: latitude, longitude, price, sq_feet, 

        # price per foot column
        df['price_per_foot'] = df['price'] / df['sq_feet']

        return df


    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        logging.info(message)
        raise


if __name__ == "__main__":
    df = read_data()

    p.boxplot_price_quadrant(df)

    # There are clearly a lot of outliers in the 'price' column, we shall remove them

    # keep rows that are within +3 to -3 standard deviations in the column 'Price'
    df =  df[np.abs(df.price-df.price.mean()) <= (3 * df.price.std())]

    p.boxplot_price_quadrant(df)

    print(df['location'].value_counts())

    # Examine the distribution

    print("Mean Price: {} ".format(df['price'].mean()))
    print("Kurtosis: {} ".format(df['price'].kurtosis()))
    print("Skew: {}".format(df['price'].skew()))

    p.distplot_price(df)

    # Normally Distributed? I guess...

    # Examination of correlation between variables
    p.corr_heat(df)

    p.bar_community(df)



