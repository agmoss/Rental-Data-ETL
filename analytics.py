import logging
import numpy as np
import time
import pandas as pd
import mysql.connector
import folium
import json

from scripts import Query as q
from scripts import Database
from scripts import LocationMap as lm

from scripts import StaticPlot
from scripts import PlotlyPlots

PATHS = {
    "write": "public/charts/",
    "read":""
}

logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

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

def visuals(df):

    # Instantiate Objects
    sp = StaticPlot.StaticPlot(df,PATHS['write'])
    ply = PlotlyPlots.PlotlyPlots(df,PATHS['write'])

    static_bar_community = sp.bar_community()
    static_box_price_quadrant = sp.boxplot_price_quadrant()
    static_dist_price = sp.distplot_price()
    static_corr_heat = sp.corr_heat()

    dynamic_bar_community = ply.bar_community()
    dynamic_box_price = ply.box_price_quadrant()
    dynamic_dist_price = ply.distplot()
    
    data = {}

    data['dynamic_bar_community'] = str(dynamic_bar_community)
    data['dynamic_box_price'] = str(dynamic_box_price)
    data['dynamic_dist_price'] = str(dynamic_dist_price)

    with open(PATHS['write'] + 'plots.json', 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":

    conn = Database.Database.connect()

    get = q.Query(conn)

    df = get.data_for_analysis()

    visuals(df)