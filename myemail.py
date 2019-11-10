import smtplib, ssl, random
import datetime


mytime = datetime.datetime.now().strftime("%H:%M")
port = 465
password = ""
smtp_server = ""
sender_email = ""
receiver_email = ""
with open('C:/Users/theco/Documents/GitHub/asd/asd/emails.txt', "r") as f:
    line = f.readline()
    recipients_emails = []
    print(recipients_emails)
    while line:
       recipients_emails.append(line.replace("\n",""))
       line = f.readline()
       #print(line)

print(recipients_emails)
content = """\
Subject: Napi fost

Hello, Ezt az üzenetet minden nap megfogod kapni mostantól pontban délben ha megy akkor a gépem."""

context = ssl.create_default_context()

while True:
    if mytime == "12:00":
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, recipients_emails, content)
