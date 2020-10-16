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

## Running the program

Before you can properly run the program you first need to make some minor changes.

### Gmail API


    Follow step one in the python quickstart guide (https://developers.google.com/gmail/api/quickstart/python)
    
        - Then you have created your own credentials.json file. Add it to your local repository
    
    Follow step two to install the library by writing pip command in your terminal:
    
        - Modules needed for python to successfully run the script (pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib)
        
     Follow step three to create token file:
     
        - It will automatically add the file to the same path as credentials.json
       

        
### Twitter API

        - Request access for twitter developer account

        - Once you have access navigate to the developer portal page
        
        - Create a project and request for API keys and token
