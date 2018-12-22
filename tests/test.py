import pytest

from ..scripts import db_functions as db
from ..scripts import get 

import pandas as pd
from pandas.io.json import json_normalize


# Test connect()
def test_connection_success():
    connection = db.connect()
    assert connection != None 

def test_api():

    page = "1"

    url = 'https://www.rentfaster.ca/api/search.json?keywords=&proximity_type=location-proximity'
    '&cur_page=' + page + '&beds=&type=&price_range_adv[from]=null&price_range_adv[to]=null&novacancy=0&city_id=1'

    # Access object
    scr = get.Accessor(url)

    data = scr.get_json()

    assert data != None

def test_data():

    page = "1"

    url = 'https://www.rentfaster.ca/api/search.json?keywords=&proximity_type=location-proximity'
    '&cur_page=' + page + '&beds=&type=&price_range_adv[from]=null&price_range_adv[to]=null&novacancy=0&city_id=1'

    # Access object
    scr = get.Accessor(url)

    data = scr.get_json()

    # There are multiple keys that can be accessed at this level, we want the listings data
    listings = data['listings']

    # Convert to a dataframe
    df = json_normalize(listings)

    df.drop(['utilities_included'], axis=1, inplace=True)

    # Convert to list
    total_data = df.apply(lambda x: x.tolist(), axis=1)

    for row in total_data:
        assert len(row) == len(df.columns)
