# 1F427_Productivity
A tool for uninhibited reflection on your productivity 

[![Build Status](https://travis-ci.org/mhbeals/1F427_Productivity.svg?branch=master)](https://travis-ci.org/mhbeals/1F427_Productivity)

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

On unix-like platforms it is recommended to set up a virtualenv:
```bash
# Setup a new venv in this repository as a folder called "venv"
python3 -m venv venv

# Activate the venv
source venv/bin/activate

```

When you are finished you can deactivate the virtualenv with
`deactivate`.  Within this venv, or using Anaconda on Windows, install
the requirements from the `requirements.txt` using pip:

``` bash
# Install requirements
pip install -r requirements.txt
```

### Testing

Run the test suite with

``` bash
pytest
```

## Usage

Currently 1F427 runs on a local web server. The `penguin_server`
python script will set up the database and launch this server. This
expects a unix-like environment but may also be used in a
Windows/anaconda environment.

```bash
./penguin_server
```


### Task Recording

+ Enter the name of their task
+ Click to indicate if this is a wholly **new** task, **ongoing** from a previous session, or they are now **done** with that task
+ Enter the number and units that best describe the energy employed on that task
+ Choose the emoji that best describes the emotion associated with completing that task
+ Press "Submit"

#### Users will be greeted with a large version of their emoji to indicate that it has been successfully recorded

### Analytics

+ Swipe down to the second page of the interface

#### Users will be presented with a display of all their previous emojis, according to the time of day they completed them

+ Press on a group of emojis to see more detailed information on which tasks are associated with those emojis
