import smtplib
import credentials

print(credentials.EMAIL_ADRESS)
print(credentials.EMAIL_PASS)


with smtplib.SMTP('smtp.gmail.com') as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(credentials.EMAIL_ADRESS, credentials.EMAIL_PASS)

    smtp.sendmail(credentials.EMAIL_ADRESS, 'detemew312@wii999.com', 'test mail')