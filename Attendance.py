import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gmailUser = 'ajaytyagi0209@gmail.com'
gmailPassword = 'Ajay@1234'
recipient = '500067403@stu.upes.ac.in'

message = f'Sent mail from python'

msg = MIMEMultipart()
msg['From'] = f'"Ajay" <{gmailUser}>'
msg['To'] = 'Me'
msg['Subject'] = "Sending mail from python"
msg.attach(MIMEText(message))

try:
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmailUser, gmailPassword)
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    mailServer.close()
    print ('Email sent!')
except:
    print ('Something went wrong...')