![Flake8](https://github.com/syedwaseemjan/Flample/actions/workflows/flake8.yaml/badge.svg)
![Black](https://github.com/syedwaseemjan/Flample/actions/workflows/black.yaml/badge.svg)
![Tests](https://github.com/syedwaseemjan/Flample/actions/workflows/tests.yaml/badge.svg)


# Flample
Flample is a Python Flask Sample Restful API.

## Concept

Sqlite DB is used for storing data. Sqlalchemy is used to help with the queries. I have used a service layer which is an internal API of this system. On top of this internal API, two  applications have been implemented.

1. Restful API
2. Frontend

Restful API is used for CRUD operations. Frontend application is used for serving static files(CSS, JS, HTML) and is also responsible for routing as I have not used any frontend routing solution.
All API endpoints are hidden behind authentication. Currently using cookies based session and authentication and API can be tested in browser easily for now. We can easily switch to Token based authentication (Will do it when have time).

No major frontend framework used due to shortage of time, just basic jquery. Dashboard.js is reponsible for doing all ajax requests to the backend API.

On the backend, functional tests are added for testing all the endpoints. I am using 

1. Pytest
2. Factory boy

## Development Environment

At the bare minimum you'll need the following for your development environment:

1. [Python](http://www.python.org/)
2. [Sqlite](https://sqlite.org)

### Local Setup

The following assumes you have all of the recommended tools listed above installed.

#### 1. Clone the project:

    $ git clone git@github.com:syedwaseemjan/Flample.git
    $ cd Flample

#### 2. Create and initialize virtualenv for the project:

    $ mkdir flample_virtualenv
    $ virtualenv flample_virtualenv
    $ source flample_virtualenv/bin/activate
    $ pip install -r requirements.txt

#### 3. Setup the Sqlite DB (Add default admin user):

    $ flask create_db
    $ flask create_admin

#### 4. Run tests:
    
    $ pytest -v

#### 5. Run the server:

    $ python runserver.py

#### 6. Load the system in browser:

    Visit http://127.0.0.1:5000
    Username: admin@flample.com
    Password: test123


### Helpful Commands

There are a few commands to help you out with the task of keeping your code compliant
with BriteLines standards:

1. Run `black` and `flake8` checkers:

```
$ flake8
```

2. Fix all the code style and import order issues:

```
$ black --check .
```
