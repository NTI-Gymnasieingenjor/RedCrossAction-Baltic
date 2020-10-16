# Project documentation

## Branches

In this project we make use of two branches: `master` and `development`. This is so that we can push code to `development` without making any changes to the current GitLab Pages-website, aka `master`. If we are forced to push code for various reasons we can do it easily without risk of intervening with the current live webpage.

## Run email tests/validation

Email tests are used for checking if an email exists and is correctly written. (We currently need to start them manually before we push)

    How to start email tests with Selenium in Python:

        - Install Python 3.8.5 (during installation check the box "Add Python to path", then reboot your system)

        - If you want to test emails from contacs.csv (execute emailvalidaion.py in your code environment)

        - If you get the message "(yourEmail) is correct" the test has passed. Otherwise it'll give you an error showing you what's wrong.

## Python pip install

Modules needed to pip install to successfully run the script.

    Install the library by writing pip command in your terminal:

        - Install the Google Client Library (pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib)

        - Tweepy, Twitter for Python (pip install tweepy)
