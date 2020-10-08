# Imports mail modules
import smtplib, ssl
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# For SSL
port = 465

# The mail you send from
sender_email = ("python.ormar@gmail.com")

# The password associated with the mail you typed in
password = input("Skriv in ditt lösenord: ")

mailSent = False

text = """\
Hej!
Jag skickade detta meddelande från Python!
Mvh
PythonOrmarna
"""

html="""\
<html>
     <head>
         <meta charset="utf-8">
     </head>
     <body>
         <h1>Hej!</h1>
         <h2>Jag skickade detta meddelande från Python!</h2>
        
         <p>Mvh<br>
             <strong>PythonOrmarna</strong>
         </p>
     </body>
 </html>
"""


# The message you choose to send
email_message = MIMEMultipart("alternative")
email_message["Subject"] = "Hej på dig!"
email_message["From"] = sender_email

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
email_message.attach(part1)
email_message.attach(part2)

# Create a secure SSL context
context = ssl.create_default_context()

# Sending message
print("Skickar meddelande!")

# Connect to smtp mail server
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    # Logs in to the mail server
    server.login(sender_email, password)
    with open("contacts.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for email in reader:
            server.sendmail(sender_email, email, email_message.as_string())
            print(f"Sending email...")
            # Send email here

# Confirmation message
print("Meddelande skickat!")
mailSent = True