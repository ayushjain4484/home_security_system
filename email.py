import smtplib
def emailpir():
    content = 'Someone is trying to enter your house'
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('ayushforibm@gmail.com','A1b2c3d4#')
    mail.sendmail('HomeSecurity','ayushjain4484@gmail.com',content)
    mail.close()
emailpir()
