import os 
import smtplib
import email
import imaplib
from time import sleep
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

username = '' #Username(sender email address) EX: abcd@gmail.com
password = '' #Gmail App Password EX: aswd dedw frfr frgt
target_email = "darksideofmosy@gmail.com" 
re_server = 'imap.gmail.com'

while True:

    print("Retrieving Email Inbox...")
    print("")

    delay = 60

    mail = imaplib.IMAP4_SSL(re_server)
    mail.login(username, password)

    # choose mailbox
    mail.select('inbox')

    # retrieve all emails  
    status, data = mail.search(None, 'ALL')

    mail_ids = []

    for block in data:
        mail_ids += block.split()


    for i in mail_ids:

        # retrieve the raw email data
        status, data = mail.fetch(i, '(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                #parsed into email object 
                message = email.message_from_bytes(response_part[1])
            
                # retrieve sender email 
                mail_from = message['from']

                # retrieve email subject 
                mail_subject = message['subject']

                if message.is_multipart():
                    mail_content = ''
                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:
                    mail_content = message.get_payload()

 
                if mail_from == "darksider <darksideofmosy@gmail.com>":
                    print(f'From: {mail_from}')
                    print(f'Subject: {mail_subject}')
                    print("")
                    
                    subject = mail_subject
                    
                    
    if subject == "help":
        print("sending help message...")
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "EPS32mail help"
        msg['From'] = username
        msg['To'] = target_email
        html = """ <!DOCTYPE html>
        <html>
        <head></head>
        <body>
        <h1>EPS32mail help</h1>
        <br>
        <h2>Options</h2>
        <p>help : send help message</p>
        <p>none : do nothing</p>
        <p>cap : capture photo</p>
        <p>100 : 100 seconds cycle delay</p>
        <p>200 : 200 seconds cycle delay</p>
        <p>3600 : 3600 seconds cycle delay</p>
        <p>7200 : 7200 seconds cycle delay</p>
        </body>
        </html>"""

        text = MIMEText(html, 'html')
        msg.attach(text)

        #fp = open('s25.jpg', 'rb')
        #image = MIMEImage(fp.read())
        #fp.close()

        #msg.attach(image)


        se_server = smtplib.SMTP('smtp.gmail.com', 587)
        sleep(2)
        se_server.ehlo()
        se_server.starttls()
        se_server.login(username,password)
        se_server.sendmail(username, target_email, msg.as_string())
        se_server.quit()
        se_server.close()
        print("Email Sent")

    if subject == "none":
        print("Do Nothing...")

    if subject == "100":
        delay = 100
        print("Delay set to 100 seconds...")
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "100 seconds cycle delay"
        msg['From'] = username
        msg['To'] = target_email
        html = """ <!DOCTYPE html>
        <html>
        <head></head>
        <body>
        <h1>100 second cycle delay</h1>
        <br>
        <h2>set to 100 seconds cycle delay</h2>
        </body>
        </html>"""

        text = MIMEText(html, 'html')
        msg.attach(text)
        se_server = smtplib.SMTP('smtp.gmail.com', 587)
        sleep(2)
        se_server.ehlo()
        se_server.starttls()
        se_server.login(username,password)
        se_server.sendmail(username, target_email, msg.as_string())
        se_server.quit()
        se_server.close()
        print("Email Sent")

    if subject == "200":
        delay = 200
        print("Delay set to 200 seconds...")
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "200 seconds cycle delay"
        msg['From'] = username
        msg['To'] = target_email
        html = """ <!DOCTYPE html>
        <html>
        <head></head>
        <body>
        <h1>200 second cycle delay</h1>
        <br>
        <h2>set to 200 seconds cycle delay</h2>
        </body>
        </html>"""

        text = MIMEText(html, 'html')
        msg.attach(text)
        se_server = smtplib.SMTP('smtp.gmail.com', 587)
        sleep(2)
        se_server.ehlo()
        se_server.starttls()
        se_server.login(username,password)
        se_server.sendmail(username, target_email, msg.as_string())
        se_server.quit()
        se_server.close()
        print("Email Sent")

    
    if subject == "3600":
        delay = 3600
        print("Delay set to 1 hour...")
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "1 hour cycle delay"
        msg['From'] = username
        msg['To'] = target_email
        html = """ <!DOCTYPE html>
        <html>
        <head></head>
        <body>
        <h1>1 hour cycle delay</h1>
        <br>
        <h2>set to 1 hour cycle delay</h2>
        </body>
        </html>"""

        text = MIMEText(html, 'html')
        msg.attach(text)
        se_server = smtplib.SMTP('smtp.gmail.com', 587)
        sleep(2)
        se_server.ehlo()
        se_server.starttls()
        se_server.login(username,password)
        se_server.sendmail(username, target_email, msg.as_string())
        se_server.quit()
        se_server.close()
        print("Email Sent")
    
    if subject == "7200":
        delay = 7200
        print("Delay set to 2 hours...")
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "2 hours cycle delay"
        msg['From'] = username
        msg['To'] = target_email
        html = """ <!DOCTYPE html>
        <html>
        <head></head>
        <body>
        <h1>2 hours cycle delay</h1>
        <br>
        <h2>set to 2 hours cycle delay</h2>
        </body>
        </html>"""

        text = MIMEText(html, 'html')
        msg.attach(text)
        se_server = smtplib.SMTP('smtp.gmail.com', 587)
        sleep(2)
        se_server.ehlo()
        se_server.starttls()
        se_server.login(username,password)
        se_server.sendmail(username, target_email, msg.as_string())
        se_server.quit()
        se_server.close()
        print("Email Sent")



        

    print("===================================")
    print("")
    sleep(delay)
