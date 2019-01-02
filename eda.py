import logging
import numpy as np
import time
import pandas as pd
import mysql.connector
import folium

from scripts import Query as q
from scripts import Database
from scripts import plot as p
from scripts import plotly_plots as pl
from scripts import LocationMap as lm

from scripts import StaticPlot
from scripts import PlotlyPlots

PATHS = {
    "write": "public/charts/",
    "read":""
}

def main(df):

    # Location Map
    # Create a folium map object
    mp = folium.Map([51.0486, -114.0708], zoom_start=10)

    # Pass the folium map to the user defined LocationMap class
    heat_map = lm.LocationMap("Folium heat map", mp)

    # Add the data to the map
    heat_map.add_heat(df)

    # Save the map
    heat_map.fmap.save(PATHS['write']+"calgary_heat_map.html")

    # There are clearly a lot of outliers in the 'price' column, we shall remove them
    # keep rows that are within +3 to -3 standard deviations in the column 'Price'
    df =  df[np.abs(df.price-df.price.mean()) <= (3 * df.price.std())]

    # Instantiate Objects
    sp = StaticPlot.StaticPlot(df,PATHS['write'])
    ply = PlotlyPlots.PlotlyPlots(df,PATHS['write'])

    sp.bar_community()
    sp.boxplot_price_quadrant()
    sp.distplot_price()
    sp.corr_heat()

    ply.bar_community()
    ply.box_price_quadrant()
    ply.distplot()

    print(df['location'].value_counts())

    # Examine the distribution
    print("Mean Price: {} ".format(df['price'].mean()))
    print("Kurtosis: {} ".format(df['price'].kurtosis()))
    print("Skew: {}".format(df['price'].skew()))
    # # Normally Distributed? I guess...

if __name__ == "__main__":

    conn = Database.Database.connect()

    get = q.Query(conn)

    df = get.data_for_analysis()

    main(df)