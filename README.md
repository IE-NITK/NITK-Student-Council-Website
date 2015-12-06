[![Build Status](https://travis-ci.org/IE-NITK/NITK-Student-Council-Website.svg)](https://travis-ci.org/IE-NITK/NITK-Student-Council-Website)

# Student Council Website

Student Council Website is the official "NITK Student Council Website" project. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* Accounts (Manages user accounts including SignUp, SignIn, etc.)
* Profiles (Manages the user profiles)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv Student_Council_Website`
    2. `$ . Student_Council_Website/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
