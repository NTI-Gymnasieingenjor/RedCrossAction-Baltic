# Imports mail modules
from __future__ import print_function
import smtplib, ssl
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time
import pickle
import os.path
import sys
import pytz
import base64



def create_message(sender, to, subject, message_text):
    """Create a message for an email.
      Args:
          sender: Email address of the sender.
          to: Email address of the receiver.
          subject: The subject of the email message.
          message_text: The text of the email message.
      Returns:
          An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_message(service, user_id, message):
    """Send an email message.
      Args:
          service: Authorized Gmail API service instance.
          user_id: User's email address. The special value "me"
          can be used to indicate the authenticated user.
          message: Message to be sent.
      Returns:
          Sent Message.
    """
    
    message = (service.users().messages().send(userId=user_id, body=message).execute())
    print('Message Id: %s' % message['id'])
    return message


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_service(path):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    scores = {} # scores is an empty dict already

    if os.path.getsize('token.pickle') > 0:      
        with open('token.pickle', "rb") as f:
            unpickler = pickle.Unpickler(f)
        # if file is not empty scores will be equal
        # to the value unpickled
            scores = unpickler.load()
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

    # Startar Gmail v1 med den som är inloggad
    service = build('gmail', 'v1', credentials=creds)
 

path_to_pickle = r"C:\Users\fredrik.nyberg\Documents\GitHub\RedCrossAction-Baltic\token.pickle"
subject = "Hi! from python"
sender = "python.ormar@gmail.com"
to = "python.ormar@gmail.com"
message_text = "This e-mail is sent from Gmail API via python! Isn't that Cool?"

user_id = "me"

service = get_service(path_to_pickle)
raw_text = create_message(sender, to, subject, message_text)
message_data = send_message(service, user_id, raw_text)