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

# If modifying these scopes, delete the file token.pickle.
# SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

"""Shows basic usage of the Gmail API.
Lists the user's Gmail labels.
"""
global msg
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
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

service = build('gmail', 'v1', credentials=creds)

def send_message():
    gmail_to = 'python.ormar@gmail.com'
    gmail_subject = 'Python gmail API email'
    gmail_content = 'POG!'

    message = MIMEText(gmail_content)
    message ['to'] = gmail_to
    message ['subject'] = gmail_subject
    # This is how gmail api reads messages
    raw = base64.urlsafe_b64encode(message.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}

    try:
        message = (service.users().messages().send(userId='me', body=body).execute())
        print("Din meddelande är skickat!")
    except errors.MessageError as error:
        print('An error occurred: %s' % error)

send_message()