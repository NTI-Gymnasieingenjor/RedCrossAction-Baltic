import imaplib
import email
from email.header import decode_header
import webbrowser
import os

from email.utils import parsedate_tz, mktime_tz, formatdate
import time


# account credentials
username = "python.ormar@gmail.com"
password = input("Lösenord: ")

# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")

# authenticate
imap.login(username, password)
status, messages = imap.select("INBOX")

# number of top emails to fetch
N = 5

# total number of emails
messages = int(messages[0])

# mail number
mail_nr = 0

try:
    for i in range(messages, messages-N, -1):
        # fetch the email message by ID
        res, msg = imap.fetch(str(i), "(RFC822)")
        mail_nr = mail_nr + 1
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode()
                # email sender
                from_ = msg.get("From")

                # date anjd time when the mail was recived
                date = msg["Date"]

                # changes date to local timezone
                tt = parsedate_tz(date)
                timestamp = mktime_tz(tt)
                print("\nMail", mail_nr)
                if from_ == "python.ormar@gmail.com":
                    print("\nDetta mail är från erat säkerhetssystem.")
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
imap.close()
imap.logout()