import os
from datetime import datetime
from datetime import date
import requests
import subprocess
import smtplib
import shutil
import warnings
import email
import imaplib
from time import sleep
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

warnings.filterwarnings("ignore", category=DeprecationWarning)

username = '' #Username(sender email address) EX: abcd@gmail.com
password = '' #Gmail App Password EX: aswd dedw frfr frgt
target_email = "darksideofmosy@gmail.com" 
re_server = 'imap.gmail.com'

def func():
    while True:
        try:
            print("Retrieving Email Inbox...")
            print("")

            # main loop delay
            delay = 5

            try:
                mail = imaplib.IMAP4_SSL(re_server)
            except Exception as e:
                print("ERROR: Failed to start IMAP server")
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "failed to start imap server"
                msg['From'] = username
                msg['To'] = target_email
                html = """ <!DOCTYPE html>
                <html>
                <head></head>
                <body>
                <h1>failed to start imap server</h1>
                <br>
                <p>ERROR: {e}</p>
                </body>
                </html>""".format(e = e)

                text = MIMEText(html, 'html')
                msg.attach(text)
                se_server = smtplib.SMTP('smtp.gmail.com', 587)
                sleep(2)
                try:
                    se_server.ehlo()
                    se_server.starttls()
                    se_server.login(username,password)
                    se_server.sendmail(username, target_email, msg.as_string())
                    se_server.quit()
                    se_server.close()
                    print("INFO: Error Sent")
                except:
                    print("ERROR: Failed to send email")

            try:
                mail.login(username, password)
            except Exception as e:
                print("ERROR: Failed to login to email")
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "failed to login to email"
                msg['From'] = username
                msg['To'] = target_email
                html = """ <!DOCTYPE html>
                <html>
                <head></head>
                <body>
                <h1>Failed to login to email</h1>
                <br>
                <p>ERROR: {e}</p>
                </body>
                </html>""".format(e = e)

                text = MIMEText(html, 'html')
                msg.attach(text)
                se_server = smtplib.SMTP('smtp.gmail.com', 587)
                sleep(2)
                try:
                    se_server.ehlo()
                    se_server.starttls()
                    se_server.login(username,password)
                    se_server.sendmail(username, target_email, msg.as_string())
                    se_server.quit()
                    se_server.close()
                    print("INFO: Error Sent")
                except:
                    print("ERROR: Failed to send email")

            try:
                # choose mailbox
                mail.select('inbox')
            except Exception as e:
                print("ERROR: failed to select mail inbox")
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "Failed to select mail inbox"
                msg['From'] = username
                msg['To'] = target_email
                html = """ <!DOCTYPE html>
                <html>
                <head></head>
                <body>
                <h1>Failed to select mail inbox</h1>
                <br>
                <p>Error: {e}</p>
                </body>
                </html>""".format(e = e)

                text = MIMEText(html, 'html')
                msg.attach(text)
                se_server = smtplib.SMTP('smtp.gmail.com', 587)
                sleep(2)
                try: 
                    se_server.ehlo()
                    se_server.starttls()
                    se_server.login(username,password)
                    se_server.sendmail(username, target_email, msg.as_string())
                    se_server.quit()
                    se_server.close()
                    print("INFO: Error Sent")
                except:
                    print("ERROR: Failed to send email")
                

            try:
                # retrieve all emails  
                status, data = mail.search(None, 'ALL')
            except Exception as e:
                print("Error: Failed to retrieve mails")
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "Failed to retrieve mails"
                msg['From'] = username
                msg['To'] = target_email
                html = """ <!DOCTYPE html>
                <html>
                <head></head>
                <body>
                <h1>Failed to retrieve mails</h1>
                <br>
                <p>ERROR: {e}</p>
                </body>
                </html>""".format(e = e)

                text = MIMEText(html, 'html')
                msg.attach(text)
                se_server = smtplib.SMTP('smtp.gmail.com', 587)
                sleep(2)
                try:
                    se_server.ehlo()
                    se_server.starttls()
                    se_server.login(username,password)
                    se_server.sendmail(username, target_email, msg.as_string())
                    se_server.quit()
                    se_server.close()
                    print("INFO: Error Sent")
                except:
                    print("ERROR: Failed to send email")
                

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
                            #print(f'Prompt: {mail_subject}')
                            #print("")
                    
                            subject = mail_subject
                    
            print("    Prompt: ", subject)
            print("")
            if subject == "help":
                print("INFO: Sending help message...")
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "EPS32mail help"
                msg['From'] = username
                msg['To'] = target_email
                html = """ <!DOCTYPE html>
                <html>
                <head></head>
                <body>
                <h1>Camera Mail Help</h1>
                <br>
                <h2>Options</h2>
                <p>help: send help message</p>
                <p>none: do nothing</p>
                <p>cap: capture photo</p>
                <p>status: camera status</p>
                <p>100: 100 seconds cycle delay</p>
                <p>200: 200 seconds cycle delay</p>
                <p>3600: 3600 seconds cycle delay</p>
                <p>7200: 7200 seconds cycle delay</p>
                </body>
                </html>"""

                text = MIMEText(html, 'html')
                msg.attach(text)
                se_server = smtplib.SMTP('smtp.gmail.com', 587)
                sleep(2)
                try:
                    se_server.ehlo()
                    se_server.starttls()
                    se_server.login(username,password)
                    se_server.sendmail(username, target_email, msg.as_string())
                    se_server.quit()
                    se_server.close()
                    print("INFO: Email Sent")
                except:
                    print("ERROR: failed to send email")

            if subject == "none":
                print("INFO: Do Nothing...")

            if subject == "100":
                delay = 100
                print("INFO: Delay set to 100 seconds...")
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "100 seconds cycle delay"
                msg['From'] = username
                msg['To'] = target_email
                html = """ <!DOCTYPE html>
                <html>
                <head></head>
                <body>
                <h2>100 second cycle delay</h2>
                <br>
                <h2>Set to 100 seconds cycle delay</h2>
                </body>
                </html>"""

                text = MIMEText(html, 'html')
                msg.attach(text)
                se_server = smtplib.SMTP('smtp.gmail.com', 587)
                sleep(2)
                try:
                    se_server.ehlo()
                    se_server.starttls()
                    se_server.login(username,password)
                    se_server.sendmail(username, target_email, msg.as_string())
                    se_server.quit()
                    se_server.close()
                    print("INFO: Email Sent")
                except:
                    print("ERROR: Failed to send email")

            if subject == "200":
                delay = 200
                print("INFO: Delay set to 200 seconds...")
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "200 seconds cycle delay"
                msg['From'] = username
                msg['To'] = target_email
                html = """ <!DOCTYPE html>
                <html>
                <head></head>
                <body>
                <h2>200 second cycle delay</h2>
                <br>
                <h2>Set to 200 seconds cycle delay</h2>
                </body>
                </html>"""

                text = MIMEText(html, 'html')
                msg.attach(text)
                se_server = smtplib.SMTP('smtp.gmail.com', 587)
                sleep(2)
                try:
                    se_server.ehlo()
                    se_server.starttls()
                    se_server.login(username,password)
                    se_server.sendmail(username, target_email, msg.as_string())
                    se_server.quit()
                    se_server.close()
                    print("INFO: Email Sent")
                except:
                    print("ERROR: failed to send email")

    
            if subject == "3600":
                delay = 3600
                print("INFO: Delay set to 1 hour...")
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "1 hour cycle delay"
                msg['From'] = username
                msg['To'] = target_email
                html = """ <!DOCTYPE html>
                <html>
                <head></head>
                <body>
                <h1>1 hour cycle delay</h>
                <br>
                <h2>set to 1 hour cycle delay</h2>
                </body>
                </html>"""

                text = MIMEText(html, 'html')
                msg.attach(text)
                se_server = smtplib.SMTP('smtp.gmail.com', 587)
                sleep(2)
                try:
                    se_server.ehlo()
                    se_server.starttls()
                    se_server.login(username,password)
                    se_server.sendmail(username, target_email, msg.as_string())
                    se_server.quit()
                    se_server.close()
                    print("INFO: Email Sent")
                except:
                    print("ERROR: failed to send email")
    
            if subject == "7200":
                delay = 7200
                print("INFO: Delay set to 2 hours...")
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
                <h2>Set to 2 hours cycle delay</h2>
                </body>
                </html>"""

                text = MIMEText(html, 'html')
                msg.attach(text)
                se_server = smtplib.SMTP('smtp.gmail.com', 587)
                sleep(2)
                try:
                    se_server.ehlo()
                    se_server.starttls()
                    se_server.login(username,password)
                    se_server.sendmail(username, target_email, msg.as_string())
                    se_server.quit()
                    se_server.close()
                    print("INFO: Email Sent")
                except:
                    print("ERROR: failed to send email")
            
            if subject == "status":
                print("INFO: Retrieving camera status...")
                try:
                    cmd = "ping 10.110.169.10"
                    result = subprocess.check_output(cmd, shell=True, text=True)
                except Exception as e:
                    print("ERROR:", e)
                    result = e
            
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "Camera Status"
                msg['From'] = username
                msg['To'] = target_email
                html = """ <!DOCTYPE html>
                <html>
                <head></head>
                <body>
                <h1>Camera Status</h1>
                <br>
                <p>{result}</p>
                </body>
                </html>""".format(result=result)

                text = MIMEText(html, 'html')
                msg.attach(text)
                se_server = smtplib.SMTP('smtp.gmail.com', 587)
                sleep(2)
                try:
                    se_server.ehlo()
                    se_server.starttls()
                    se_server.login(username,password)
                    se_server.sendmail(username, target_email, msg.as_string())
                    se_server.quit()
                    se_server.close()
                    print("INFO: Email Sent")
                except:
                    print("ERROR: failed to send email")

            if subject == "cap":
                print("INFO: Capturing image...")
                error_selenium = "NONE"
                error_download = "NONE"

                
                options = Options()
                options.add_argument('--headless')
                options.add_argument("--disable-logging")  # Disables all logging
                options.add_argument("--log-level=3")
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                driver = webdriver.Chrome(options=options)
                url = "http://10.110.169.10/"
                # click on capture button 
                try:
                    driver.get(url)
                    element = driver.find_element(By.XPATH, "/html/body/div[1]/p[2]/button[2]")
                    element.click()
                    print("")
                    print("INFO: Selenium is clicked on capture button")
                except Exception as e:
                    print("ERROR: Failed to start selenium")
                    error_selenium = e

                sleep(6)

                # download image
                try:
                    res = requests.get("http://10.110.169.10/saved-photo").content
                    f = open('saved-photo.jpg', 'wb')
                    f.write(res)
                    f.close()
                    print("INFO: Image downloaded")
                except Exception as e:
                    print("ERROR: Failed to download image")          
                    error_download = e 

                

                today = date.today() 

                current_datetime = datetime.now()
                
                # store hour an min in file name
                hour = current_datetime.hour
                min = current_datetime.minute
                time = str(hour) + "," + str(min) + ".jpg"

                # create folder
                folder_name = str(today.month) + "." + str(today.day)
                path = "image_archive/" + folder_name
                exist = os.path.exists(path)
                if exist == False:
                    print("INFO: folder craeted")
                    os.makedirs(path) 
                else: 
                    print("INFO: folder exist")
                
                # rename image name
                os.rename('saved-photo.jpg', str(time))

        
                msg = MIMEMultipart('alternative')
                msg['Subject'] = "Captured image"
                msg['From'] = username
                msg['To'] = target_email
                html = """ <!DOCTYPE html>
                <html>
                <head></head>
                <body>
                <h1>Captured Image</h1>
                <p>Selenium_error: {error_selenium}</p>
                <p>Download_error: {error_download}</p>
                <p>Time: {current_datetime}</p>
                </body>
                </html>""".format(error_selenium = error_selenium, error_download = error_download, current_datetime = current_datetime)

                text = MIMEText(html, 'html')
                msg.attach(text)

                # attach image to email
                try:
                    fp = open(str(time), 'rb')
                    image = MIMEImage(fp.read())
                    fp.close()
                    msg.attach(image)
                except:
                    print("ERROR: failed to find image")

                se_server = smtplib.SMTP('smtp.gmail.com', 587)
                sleep(2)
                try:
                    se_server.ehlo()
                    se_server.starttls()
                    se_server.login(username,password)
                    se_server.sendmail(username, target_email, msg.as_string())
                    se_server.quit()
                    se_server.close()
                    print("INFO: Email Sent")
                except: 
                    print("ERROR: failed to send email")
                
                # move image to archive folder
                source = str(time)
                dest = path 
                print("INFO: ", source)
                shutil.move(source, dest)
                print("INFO: image file moved to archive")


            print("===================================")
            print("")
            sleep(delay)

        except Exception as e:
            print("MAIN_LOOP_ERROR:", e)
            print("===================================")
            sleep(20)
            func()
    
func()
