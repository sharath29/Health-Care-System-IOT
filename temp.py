import serial
import MySQLdb as mdb
from twilio.rest import Client

# arduino = serial.Serial("/dev/ttyACM1",115200)
# db = mdb.connect("localhost","root","sharath","pulse")
# cursor = db.cursor()
# data = '''(SELECT * FROM test)'''
# cursor.execute(data)
# db.commit()

# for i in cursor:
# 	print i[0]
def sendsms(value1,value2):
        account_sid = "AC4dc4c052c83af8da23b185ee9b6f946a"
        auth_token = "b265146ea246e18d57da8a1eec8d7664"

        client = Client(account_sid, auth_token)

        client.messages.create(
        to="+918618648750",
        from_="+14139923440",
        body="This is emergency message.\n"+" Heart rate is "+str(value1)+" Temperature is "+str(value2))
sendsms(1,1)

# while True:
# 	data = arduino.readline()
# 	print data

