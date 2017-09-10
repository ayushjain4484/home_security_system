import RPi.GPIO as GPIO
import time
import MySQLdb
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN) 
#GPIO.setup(11,GPIO.OUT)

conn= MySQLdb.connect("localhost","root","raspberry","testwebsite")
c = conn.cursor()
sql="insert into pir_tab(ch)values(%s)"

while True:
    i=GPIO.input(7)
    if i==1:
        c.executemany(sql,"a")
        conn.commit()
        print "intruder Detected"
        time.sleep(3)



  
        
