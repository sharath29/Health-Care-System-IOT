# dbms-project
Using raspberry pi and ardiuno board to read data from sensors attached to patient and send real time health sensor data to the doctor and notifying incase of any abnormal sensor data.

# SETUP
1.Clone this project into your local machine.

2.Run ifconfig and find out your ipaddress of your local machine.
![ScreenShot](https://raw.github.com/sharath29/dbms-project/master/)

3.Go to raspberrypi files 
  sudo vim etc/wpa_supplicant/wpa_supplicant.config

  add
  network={
      ssid="network-name"
      psk="network-password"
      key_mgmt=WPA-PSK
  }
  save and close

3.Use Nmap to scan the subnet make last field of your ip address as 0 and add /24 to your ip address.
  eg: nmap -sP 192.168.1.0/24
  
  This will display all the devices connected to this network(subnet).

4.Place the pulse sensor folder inside the arduino library folder in your raspberry pi.Compile and load the files into the arduino. Connect the arduino to raspberry pi.

5.ssh into raspberry using
  ssh pi@<ip_address of pi> or ssh pi@raspberrypi.local

6.Activate virtualenv
  cd into the project folder(dbms-project)
  source tutorial/bin.activate
  
7.Run django server using
  cd into manage.py location
  python manage.py runservers <ip_address of pi>:<port number>
  This web page can be accessed by any device inside this subnet.
  
8.Make sure the arduino port number from tools is tty/ACM0.(we are using this port inside our python script)

9.Before starting python script (monitors the sensor's data).
  Make sure you have a twilio account.
  Create an account and create a project and register your phone number.
  Then copy the session_id and auth_id to your python script.
  
10.Run script and record data from sensors attached to arduino.
