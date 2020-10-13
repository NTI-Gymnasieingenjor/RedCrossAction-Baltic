from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time

import imaplib
import email
from email.header import decode_header
import webbrowser
import os

from email.utils import parsedate_tz, mktime_tz, formatdate


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

    # authenticate
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])

    # number of mails to search
    N = 2

    # total number of emails
    # messages = int(messages[0])

    # mail number
    mail_nr = 0

    try:
        for message in messages[N]:
            # fetch the email message by ID

            mail_nr = mail_nr + 1
                    # parse a bytes email into a message object
            msg = service.users().messages().get(userId='me', id=message['id']).execute()
            print(msg['snippet'])
            print("\n")
            time.sleep(2)
                    # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode()
                # email sender
            from_ = msg.get("From")

                # date and time when the mail was recived
            date = msg["Date"]

                # changes the found date to local timezone
            tt = parsedate_tz(date)
            timestamp = mktime_tz(tt)
            print("\nMail", mail_nr)
            if from_ == "python.ormar@gmail.com":
                print("\nDetta mail är från erat säkerhetssystem.")
                # prints the time when the mail was sent in local time
                print("\nDatum:", formatdate(timestamp, True))
                print("Ämne:", subject)
                print("Från:", from_)
            else: 
                print("Detta mail är INTE från erat säkerhetssystem")

            # if the email message is multipart
            if msg.is_multipart():
                # iterate over email parts
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # print text/plain emails and skip attachments
                        print(body)
            else:
                # extract content type of email
                content_type = msg.get_content_type()
                # get the email body
                body = msg.get_payload(decode=True).decode()
                if content_type == "text/plain":
                    # print only text email parts
                    print(body)
            print("="*100)
    except:
        print("\nInga fler mail hittades // Din inkorg är tom")
if __name__ == '__main__':
    main()