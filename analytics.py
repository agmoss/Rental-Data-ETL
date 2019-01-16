import logging
import numpy as np
import time
import pandas as pd
import mysql.connector
import folium
import json
import os

from scripts import Query as q
from scripts import Database
from scripts import LocationMap as lm

from scripts import StaticPlot
from scripts import PlotlyPlots

import definitions


logging.basicConfig(filename='app.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def visuals(df):

    #os.makedirs(os.path.dirname(definitions.PATHS['write_visuals']), exist_ok=True)

    # Location Map
    # Create a folium map object
    mp = folium.Map([51.0486, -114.0708], zoom_start=14)

    # Pass the folium map to the user defined LocationMap class
    heat_map = lm.LocationMap("Folium heat map", mp)

    # Add the data to the map
    heat_map.shape_mark(df)

    # Save the map
    heat_map.fmap.save(os.path.join(definitions.PATHS['write_heatmap'], "calgary_heat_map.html"))

    # Plots
    ply = PlotlyPlots.PlotlyPlots(df)

    dynamic_box_price = ply.box_price_quadrant()
    dynamic_scatter_price_community = ply.scatter_price_community()
    dynamic_pie_community = ply.pie_community()
    dynamic_heat = ply.corr_heatmap()
    dynamic_hist = ply.hist()


    # Metics
    mean_price = df['price'].mean()
    quantity = len(df.index)
    agg_prices = df.groupby('type', as_index=False)['price'].mean()

    agg_prices.set_index('type', inplace = True)

    data = {}

    data['dynamic_box_price'] = str(dynamic_box_price)
    data['dynamic_scatter_price_community'] = str(dynamic_scatter_price_community)
    data['dynamic_pie_community'] = str(dynamic_pie_community)
    data['dynamic_heat'] = str(dynamic_heat)
    data['dynamic_hist'] = str(dynamic_hist)
    data['agg_prices'] = agg_prices.to_json(orient = 'index')
    data['mean_price'] = mean_price
    data['total_listings'] = quantity


    with open(os.path.join(definitions.PATHS['write_visuals'] ,'plots.json'), 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":

    conn = Database.Database.connect()

    get = q.Query(conn)

    df = get.data_for_analysis()

    visuals(df)

    df.to_csv(os.path.join(definitions.PATHS['write_data'], "data.csv"))