from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import time

# If modifying these scopes, delete the file token.pickle.

    # number of mails to search
    N = 2

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