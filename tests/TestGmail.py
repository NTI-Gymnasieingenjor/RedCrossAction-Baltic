from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time
from datetime import datetime
import sys
import pytz
import base64


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
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

    # Call the Gmail API
    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])

    #Get messages
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])

    # mail number
    mail_nr = 0

    message_count = int(input("Hur många mails vill du söka igenom? "))
    if not messages:
        print('No messages')
    else:
        for message in messages[:message_count]:
            mail_nr += 1
            msg = service.users().messages().get(userId='me', id=message['id'], format='raw').execute()
            print("="*100)
            print("\nMail:", mail_nr)
            datum = int(msg['internalDate'])
            datum /= 1000
            print("Datum:", datetime.fromtimestamp(datum).strftime('%Y-%m-%d %H:%M:%S'))
            print("Medelande:", msg['snippet'])
        

            print("\n")
            time.sleep(2)

if __name__ == '__main__':
    main()