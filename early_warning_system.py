# Imports mail modules
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# For SSL
port = 465

# The mail you send from
sender_email = ("python.ormar@gmail.com")

# The password associated with the mail you typed in
password = input("Skriv in ditt lösenord: ")

# The mail you want to send to
receiver_email = ("python.ormar@gmail.com")

# The message you choose to send
email_message = MIMEMultipart("alternative")
email_message["Subject"] = "Hej på dig!"
email_message["From"] = sender_email
email_message["To"] = receiver_email

text = """\
Hej!
Jag skickade detta meddelande från Python!
MVH
PythonOrmarna
"""
html = """\
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Hej!</h1>
        <h2>Jag skickade detta meddelande från Python!</h2>
        
        <p>MVH <br>
            <strong>PythonOrmarna</strong>
        </p>
    </body>
</html>
"""

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
    # Sends the email
    server.sendmail(sender_email, receiver_email, email_message.as_string())

# Confirmation message
print("Meddelande skickat!")