import email
import imaplib


username = '' #Username(sender email address) EX: abcd@gmail.com
password = '' #Gmail App Password EX: aswd dedw frfr frgt
server = 'imap.gmail.com'

mail = imaplib.IMAP4_SSL(server)
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

            subject = []
            content = []  
            if mail_from == "darksider <darksideofmosy@gmail.com>":
                print(f'From: {mail_from}')
                print(f'Subject: {mail_subject}')
                print(f'Content: {mail_content}')

                subject = mail_subject
                content = mail_content

print(subject)
print(content)



