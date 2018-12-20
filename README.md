# RentFaster API ETL

Query the rentfaster.ca API and store the cleaned results in a MySQL database. 

This is a work in progress.


## About

Each rentfaster.ca webpage exposes a JSON API of the page content. Using pagination, get requests are sent to each individual API. The request responses are converted to dataframe objects and cleaned of inconsistencies and bad data. The cleaned data is then inserted into a MySQL database for storage and analysis.


The starting URL for the script is:

```
https://www.rentfaster.ca/api/search.json?keywords=&proximity_type=location-proximity%27%27&cur_page&beds=&type=&price_range_adv[from]=null&price_range_adv[to]=null&novacancy=0&city_id=1
```

which corresponds to...

```
https://www.rentfaster.ca/ab/calgary/rentals/?beds=&baths=&type=&price_range_adv%5Bfrom%5D=null&price_range_adv%5Bto%5D=null
```

as a browser page. 



### Prerequisites

Dependencies can be installed via:

```
pip install requirements.txt
```


## Built With

* [Requests](http://docs.python-requests.org/en/master/) - HTTP library 
* [Pandas](https://www.crummy.com/software/BeautifulSoup/) - Dataframe object
* [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) - MySQL driver written in python


## Contributing

Feedback and constructive criticism is more than welcome


## Author

* **Andrew Moss** - *Creator* - [agmoss](https://github.com/agmoss)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
