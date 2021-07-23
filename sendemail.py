import numpy as np
import pandas as pd

import smtplib
import csv
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def read_template(filename):
    with open(filename,'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
        return Template(template_file_content)

print('Enter your email address:')
MY_ADDRESS = input()  #enter your gmail account address
print('Enter Password:')
PASSWORD = input()          #enter your password
s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

# read the message template
message_template = read_template('template.txt')
# SUBJECT = input('Enter the subject of email:')

#Read the csv file
df = pd.read_csv('details.csv')
print(df)

for i in range(0,df.shape[0]):
    msg = MIMEMultipart() # create a message

    # add in the actual person name to the message template
    message=message_template.substitute(name=df.at[i,'name'],eventname="An Insights into Research Paper Writing", eventdate="July 31 2021, 5:00 PM")

    # Prints out the message body for our sake
    print(message)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=df.at[i,'email']
    msg['Subject']="Template: Registration Confirmation Mail"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg

# Terminate the SMTP session and close the connection
s.quit()



