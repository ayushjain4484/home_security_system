import smtplib
def email(content="Mail text"):
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('user@gmail.com','password#')
    mail.sendmail('HomeSecurity','user@gmail.com',content)
    mail.close()
email()
