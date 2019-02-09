# Rental Listings ETL
>A streamlined and efficient ETL pipeline for online rental listing data.

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

This project gathers rental listing data from the Rentfaster.ca API. A custom data engineering process cleans the data and stores it in the appropriate format for analytical queries.

The data collected by this service forms the foundation for The Calgary Project.

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

### Code
* [Requests](http://docs.python-requests.org/en/master/) - HTTP library 
* [Pandas](https://pandas.pydata.org/) - Python data analysis library
* [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) - MySQL driver written in python
* [Schedule](https://pypi.org/project/schedule/) - Python job scheduling for humans.
* [pytest](https://docs.pytest.org/en/latest/) - Testing library

### Services
* [Microsoft Azure](https://azure.microsoft.com/en-ca/) - Cloud service

## Contributing

Feedback and constructive criticism is more than welcome!

## Author

* **Andrew Moss** - *Creator* - [agmoss](https://github.com/agmoss)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Rentfaster.ca