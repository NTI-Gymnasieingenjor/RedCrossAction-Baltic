from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import time
from google.auth.transport.requests import Request
# For send message function
from email.mime.text import MIMEText
from email import errors
import base64
# File with emails
import csv

# LOGIN ======================================================================

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

global msg
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first time.
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

# Starts Gmail V1 with logged in user
service = build('gmail', 'v1', credentials=creds)

# ==================================================================================

# MAIL SENDER ================================================================

def send_message():
    # Opens file with emails
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        # Skip header row
        next(reader)
        # Loops through emails file
        for email in reader:
            # Email content
            gmail_content = 'Systemet har känt av en oroväckande mängd Tweet med #red_cross_warning_system, vänligen inspektera.'
            # Email subject
            gmail_subject = 'Systemvarning från Twitter!'
            # Revomes brackets and quotations
            email = "".join(email)
            print("\nEmail: " + email)

            # Uses email preferences
            message = MIMEText(gmail_content)
            message ['subject'] = gmail_subject
            message ['to'] = email

            # Gmail API reads messages
            raw = base64.urlsafe_b64encode(message.as_bytes())
            raw = raw.decode()
            body = {'raw': raw}

            # Sends the message
            try:
                message = (service.users().messages().send(userId='me', body=body).execute())
                print("Ditt meddelande är skickat!")
            # If any error happends
            except errors.MessageError as error:
                print('An error occurred: %s' % error)

# Starts function
if __name__ == "__main__":
    send_message()