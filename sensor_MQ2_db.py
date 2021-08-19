import RPi.GPIO as GPIO
import time
import MySQLdb
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN) 
#GPIO.setup(11,GPIO.OUT)

conn= MySQLdb.connect("localhost","user","password","database")
c = conn.cursor()
sql="insert into mq2_tab(ch)values(%s)"

while True:
    i=GPIO.input(11)
    if i==1:
        c.executemany(sql,"a")
        conn.commit()
        print "intruder Detected"
        time.sleep(3)



  
        
