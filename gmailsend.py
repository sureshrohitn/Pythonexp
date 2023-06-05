import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
with open('welcome', 'rb') as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'welcome to test mail'
msg['From'] = 'sureshrohitn@gmail.com'
msg['To'] = 'sureshktd92@gmail.com'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail('sureshrohitn@gmail.com', ['sureshktd92@gmail.com'], msg.as_string())
s.quit()