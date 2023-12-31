# Book Library REST API

REST API for online library was written as a part of course in Udemy. It supports authors of books and books resources. This is my first big project where i have learned alot about building REST API using python language. Topics that i have learned during this project:
* how to create a REST API using the Python language and the Flask library;
* using popular libraries available in Python, e.g. SQLAlchemy, Alembic, Pytest and many other;
* creating queries to filter, sort and paginate data;
* the application factory pattern;
* writing REST API automted tests;
* creating REST API documentation;
* using MYSQL, SQLite databases;
* using the API testing tool - Postman.

The documentation can be found in `documentation.html`

## Setup

- Clone repository
- Create database and user
- Rename .env.example to `.env` and set your values
```buildoutcfg
# SQLALCHEMY_DATABASE_URI MySQL template
SQLALCHEMY_DATABASE_URI=mysql+pymysql://<db_user>:<db_password>@<db_host>/<db_name>?charset=utf8mb4
```
- Create a virtual environment
```buildoutcfg
python -m venv venv
```
- Install packages from `requirements.txt`
```buildoutcfg
pip install -r requirements.txt
```
- Migrate database
```buildoutcfg
flask db upgrade
```
- Run command
```buildoutcfg
flask run
```


**NOTE**

Import / delete example data from `book_library_app/samples`:

```buildoutcfg
# import
flask db-manage add-data

# remove
flask db-manage remove-data
```

## Tests

In order to execute tests located in `tests/` run the command:

```buildoutcfg
python -m pytest tests/
```

## Technologies / Tools

- Python 3.8.0
- Flask 1.1.2
- Alembic 1.4.2
- SQLAlchemy 1.3.16
- Pytest 5.4.3
- MySQL
- Postman
