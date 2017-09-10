#importing packages
import RPi.GPIO as GPIO
import time
import MySQLdb
import smtplib

#setting up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.OUT)

#defining Functions
def emailpir():
    content = 'Someone is trying to enter your house'
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('ayushforibm@gmail.com','A1b2c3d4#')
    mail.sendmail('HomeSecurity','ayushjain4484@gmail.com',content)
    mail.close()

def emailmq2():
    content = 'Smoke Detected in your house'
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('ayushforibm@gmail.com','A1b2c3d4#')
    mail.sendmail('HomeSecurity','ayushjain4484@gmail.com',content)
    mail.close()

#establishing Database Connection
conn= MySQLdb.connect("localhost","root","raspberry","testwebsite")
c = conn.cursor()
sqlmq="insert into mq2_tab(ch)values(%s)"
sqlpir="insert into pir_tab(ch)values(%s)"

#taking inputs form Sensors
while True:
    m=GPIO.input(11)
    p=GPIO.input(7)
    if m==1:
        c.executemany(sqlmq,"a")
        conn.commit()
        print "intruder Detected"
        emailmq2()#sending email
        time.sleep(3)
    if p==1:
        c.executemany(sqlpir,"a")
        conn.commit()
        print "intruder Detected"
        emailpir()#sending email
        time.sleep(3)


