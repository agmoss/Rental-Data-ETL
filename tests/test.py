import pytest

from scripts import Database
from scripts import Accessor


def test_connection_success():

	try:
		conn = Database.Database.connect()
	except MyError:
		pytest.fail("Unhandled exception")
    
def test_api():

	page = "1"

	url = 'https://www.rentfaster.ca/api/search.json?keywords=&proximity_type=location-proximity'
	'&cur_page=' + page + '&beds=&type=&price_range_adv[from]=null&price_range_adv[to]=null&novacancy=0&city_id=1'

	# Access object
	scr = Accessor.Accessor(url)

	data = scr.get_json()

	assert data != None