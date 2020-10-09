# Project documentation

## Branches

In this project we make use of two branches: `master` and `development`. This is so that we can push code to `development` without making any changes to the current GitLab Pages-website, aka `master`. If we are forced to push code for various reasons we can do it easily without risk of intervening with the current live webpage.

### Run email tests/validation

#

Email tests are for checking if email is existing and is correctly witted. (Right now we need to start them manually before we push)

    How to start email tests with Selenium in Python:

        - Install Python 3.8.5 (during installation check box Add Python to path, then reboot your system)

        - If you want to test email from contacs.csv (execute emailvalidaion.py in your code environment)

        - The test passes when you get message "(yourEmail) is correct" otherwise it will show specific error
