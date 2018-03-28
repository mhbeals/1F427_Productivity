# 1F427_Productivity
A tool for uninhibited reflection on your productivity 

1F427 (pronounced ":penguin:") allows you to log your activities with
informal measures of time spent and emotional response. The purpose is
*not* to enable "serious" accounting of your time, but to help manage
your mood and energy. What activities make you happier when done in
the morning?

## Requirements

This project is built on Python 3.4 or later.  The Django web
framework is used for this tech demo; we recommend installing in a
virtualenv as outlined below.


## Installation

To set up a virtualenv and install requirements from the `requirements.txt` file:

```bash
# Setup a new venv in this repository as a folder called "venv"
python3 -m venv venv

# Activate the venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

When you are finished you can deactivate the virtualenv with `deactivate`.

## Setup

Build the database and import stuff:

``` bash
python manage.py migrate
python manage.py loaddata core/fixtures/emoji.json
python manage.py loaddata core/fixtures/units.yaml
python manage.py loaddata core/fixtures/tasks.yaml
```

## Usage

Currently 1F427 runs on a local web server. Launch this with

```bash
python manage.py runserver
```
