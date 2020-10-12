# Imports the necessary selenium extension
import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Creates a variable "options" with the Options() class attributes
options = webdriver.ChromeOptions()

# Adds headless as an argument
options.add_argument("headless")

# Makes the driver variable with respective attributes
driver = webdriver.Chrome(options=options)


# Validates Online

# Loads in the website
driver.get("https://validateemailaddress.org/")

# Finds the accept cookie button and clicks it
driver.find_element_by_id("accept").click()

# Finds the contact.csv file
with open("contacts.csv") as file:

        # variable with contacts.csv content
        reader = csv.reader(file)
        
        next(reader)  # Skip header row
        for email in reader:

            # Looks for the class name "input" element and sends the respective mail
            driver.find_element_by_class_name("input").send_keys(email)

            # Makes a variable which stores the "submit" element. The check button on the browser
            link = driver.find_element_by_class_name('submit')

            # Clicks on the stored element
            link.click()

            print("Validating...")
            # If
            try:
                print(email, driver.find_element_by_class_name("failed").text,"\n")

            # Else
            except:
                print(email, "is correct\n")

            # Wait for 3 seconds
            time.sleep(3)

            # Clears input field
            driver.find_element_by_class_name("input").clear()

