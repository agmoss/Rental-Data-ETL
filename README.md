# Rental Property Analytics Web Application

The Rental Analytics App is a data science project that offers real time insight to Calgarys rental property market. The app gathers and stores the most recent rental listings and presents the user with advanced statistical visualizations and metrics.  

This is a work in progress.

## About

This app runs of off data obtained from the rentfaster.ca API. 

Each rentfaster.ca webpage exposes a JSON API of the page content. Using pagination, get requests are sent to each individual API. The request responses cleaned of inconsistencies and bad data then inserted into a MySQL database for storage.

The front end of the app querys the database and provides an interactive web platform to the user.

### Prerequisites

Dependencies can be installed via:

```
pip install requirements.txt
```
## Tests

Testing for this project is handled by pytest.

### Testing the database connection & API status

 In the project directory, type:

```
$ pytest tests/test.py
```

All tests should pass before running app.py.

## Built With

* [Django](https://www.djangoproject.com/) - Web framework
* [Plotly](https://plot.ly/python/) - Open source graphing library
* [Seaborn](https://seaborn.pydata.org/) - Statistical data visualization
* [Requests](http://docs.python-requests.org/en/master/) - HTTP library 
* [Pandas](https://www.crummy.com/software/BeautifulSoup/) - Dataframe object
* [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) - MySQL driver written in python
* [Start Bootstrap - SB Admin](https://github.com/BlackrockDigital/startbootstrap-sb-admin) - Open source bootstrap template

## Contributing

Feedback and constructive criticism is more than welcome

## Author

* **Andrew Moss** - *Creator* - [agmoss](https://github.com/agmoss)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
