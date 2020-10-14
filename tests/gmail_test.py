from __future__ import print_function
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time
import pickle
import os.path
import sys
import pytz
import os

# LOGIN ======================================================================

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
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

    # Starts Gmail V1 with logged in user
    service = build('gmail', 'v1', credentials=creds)
 
# ================================================================================== 


    # MAIL CHECKHER ================================================================

    # get mails via gmail api
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])

    # mail number
    mail_nr = 0

    # variabel for how many mails we want to search through
    message_count = int(input("Hur många mails vill du söka igenom? "))
    # if 0 mails are chosen
    if not messages:
        print('Inga mail i inkorgen')
    else:
        # looks through the email inbox for mails "message_count" amount of times
        for message in messages[:message_count]:
            # gets the email id's in full format so we can extraqct information via the gmail api
            msg = service.users().messages().get(userId='me', id=message['id'], format='full', metadataHeaders=None).execute()
            # gets the headers of the email in a variable
            headers = msg["payload"]["headers"]
            # from headers gets the sender email, who it was from 
            from_ = [i['value'] for i in headers if i["name"]=="From"]
            # from headers gets the subject of the email
            subject = [i['value'] for i in headers if i["name"]=="Subject"]
            # keeps count of the current email
            mail_nr += 1
            # if the email is from the security system email print it's information
            if from_ == ['Python Ormarna <python.ormar@gmail.com>'] or from_ == ['python.ormar@gmail.com']:
                # gets the email in raw format via gmail api
                rawmsg = service.users().messages().get(userId="me", id=message["id"], format="raw", metadataHeaders=None).execute()
                print("="*100)
                print("\nMail:", mail_nr)
                print("Detta mail är från erat säkerhetssystem")
                # variable the UNIX time of when the email was sent
                datum = int(msg['internalDate'])
                datum /= 1000
                # prints the date and time when the email was revived in local y/m/d/h/m/s
                print("Mottaget:", datetime.fromtimestamp(datum).strftime('%Y-%m-%d %H:%M:%S'))
                print("Från:", from_)
                print("Ämne:", subject)
                # prints a snippet from the email
                print(msg['snippet'])
                print("\n")
            else:
                print("="*100)
                print("\nMail:", mail_nr)
                print("Detta mail är INTE från erat säkerhetssystem\n")
            time.sleep(1)
        print("Inga fler mail hittades")
        
if __name__ == '__main__':
    main()