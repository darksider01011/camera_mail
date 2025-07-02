import os 
import smtplib
import email
import imaplib
from time import sleep
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

username = 'bisimchi0110@gmail.com' #Username(sender email address) EX: abcd@gmail.com
password = 'g' #Gmail App Password EX: aswd dedw frfr frgt
target_email = "darksideofmosy@gmail.com" 
re_server = 'imap.gmail.com'

while True:
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
                    print(f'Content: {mail_content}')

                    subject = mail_subject
                    content = mail_content
                    
    if subject == "help":
        print("sending help message...")
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "mailer help"
        msg['From'] = username
        msg['To'] = target_email
        html = """ <!DOCTYPE html>
        <html>
        <head></head>
        <body>
        <h1>{dkp}</h1>
        <br>
        <h2>Options</h2>
        <p>Count: {count}</p>
        <p>Delay: {delay} Minutes</p>
        <h2>Product</h2>
        <p>Url: {url}</p>
        </body>
        </html>""".format(dkp=1, url=1, count=1, delay=1)

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
        print("Done!")


    print("=========================")
    print("")
    sleep(30)
