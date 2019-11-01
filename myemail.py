import smtplib, ssl

port = 465
password = "RAd@AXaaUwnv2.X"
smtp_server = "mail.cock.li"
sender_email = "imoder@cock.li"
receiver_email = "toth3balint@gmail.com"
content = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, content)
