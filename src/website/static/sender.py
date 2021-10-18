from src.website.static import credentials
import smtplib
import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# in order for this to work, you need to make a file inside the parent folder of 'sender.py' named 'credentials.py'
# and add 2 strings to it named 'EMAIL_ADDRESS' and 'EMAIL_PASS' containing your email and password/app password

def mail_sender(subject, content, mail):
    with smtplib.SMTP('smtp.gmail.com') as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(credentials.EMAIL_ADDRESS, credentials.EMAIL_PASS)
        content = f'Subject: {subject}\n\n{content}'
        smtp.sendmail(credentials.EMAIL_ADDRESS, mail, content)


def mail_sending(subject, content, emails):
    for mail in emails:
        mail = mail.strip()
        if re.fullmatch(regex, mail):
            mail_sender(subject, content, str(mail))
