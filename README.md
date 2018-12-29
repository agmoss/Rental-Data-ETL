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

## Built With

* [Plotly](https://plot.ly/python/) - Open Source Graphing Library
* [Seaborn] (https://seaborn.pydata.org/) - Statistical Data Visualization
* [Requests](http://docs.python-requests.org/en/master/) - HTTP library 
* [Pandas](https://www.crummy.com/software/BeautifulSoup/) - Dataframe object
* [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) - MySQL driver written in python

## Contributing

Feedback and constructive criticism is more than welcome

## Author

* **Andrew Moss** - *Creator* - [agmoss](https://github.com/agmoss)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
