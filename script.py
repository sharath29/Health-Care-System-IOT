#! /usr/bin/python
import time
from datetime import datetime 
import serial
import MySQLdb as mdb
from twilio.rest import Client


def sendsms(value1,value2):
        account_sid = "AC4dc4c052c83af8da23b185ee9b6f946a"
        auth_token = "b265146ea246e18d57da8a1eec8d7664"

        client = Client(account_sid, auth_token)

        client.messages.create(
        to="+918618648750",
        from_="+14139923440",
        body="This is emergency message.\n"+" Heart rate is "+str(value1)+" Temperature is "+str(value2))

# def sendsms2():
#         account_sid = "ACd4a5361556cddfda66f560eaa82f0014"
#         auth_token = "8c0799d6b11411568ae551a6ab296c7c"

#         client = Client(account_sid, auth_token)

#         client.messages.create(
#         to="+918762266730",
#         from_="+1 319-313-5151 ",
#         body="Patient about to get unconscious.\n")

arduino = serial.Serial("/dev/ttyACM2",115200) 

i= 10
while i<= 60:
	d = datetime.now()	
	dat,tim = d.date(),d.time()		 		
	arduino.flush()	
	data = arduino.readline()
	rate = data.split(",")
	if len(rate) == 2:
		temp,pulserate = rate[0],rate[1].strip('\r\n')
		print pulserate,temp
		if int(pulserate) > 150 or (int(temp) > 32):
			sendsms(pulserate,temp)
		# if int(adxl)>750:
		# 	sendsms2()
		db = mdb.connect("localhost","root","sharath","testdb")
		cursor = db.cursor()
		data = '''INSERT INTO pulse_temp VALUES (%s,%s,%s,%s)'''
		try:
			cursor.execute( data,( str(temp),str(pulserate),str(dat),str(tim) ) )
			db.commit()
		except:
			print "not inserted"
		time.sleep(5)
	i+=1

db.close()