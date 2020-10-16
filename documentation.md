# Project documentation

## Branches

In this project we make use of two or more branches: `main` and `development`. Each invividual feature has its own development branch and is merged with main when finished. This is so that we can push code to `development` without making any changes to the current working product, aka `main`. If we are forced to push code for various reasons we can do it easily without risk of intervening with the current live product on the main branch.

### Run email tests/validation

#

Email tests are used for checking if an email exists and is correctly written.

    How to start email tests with Selenium in Python:

        - Install Python 3.8.5 (during installation check the box "Add Python to path", then reboot your system)

        - If you want to test emails from contacts.csv (execute email_validation.py in your code environment)

        - If you get the message "(yourEmail) is correct" the test has passed. Otherwise it'll give you an error showing you what's wrong
