import logging
import numpy as np
import time
import pandas as pd
import mysql.connector

from scripts import Query as q
from scripts import db_functions as db
from scripts import plot as p
from scripts import plotly_plots as pl

if __name__ == "__main__":

    conn = db.connect()

    get = q.Query(conn)

    df = get.data_for_analysis()

    pl.bar_community(df)

    p.boxplot_price_quadrant(df)

    pl.box_price_quadrant(df)

    # There are clearly a lot of outliers in the 'price' column, we shall remove them

    # keep rows that are within +3 to -3 standard deviations in the column 'Price'
    df =  df[np.abs(df.price-df.price.mean()) <= (3 * df.price.std())]

    print(df['location'].value_counts())

    # Examine the distribution

    print("Mean Price: {} ".format(df['price'].mean()))
    print("Kurtosis: {} ".format(df['price'].kurtosis()))
    print("Skew: {}".format(df['price'].skew()))

    p.distplot_price(df)

    pl.distplot(df)

    # Normally Distributed? I guess...

    # Examination of correlation between variables
    p.corr_heat(df)



    



