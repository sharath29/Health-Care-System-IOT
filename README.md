# dbms-project

# SETUP
1.Clone this project into your local machine.

2.Run ifconfig and find out your ipaddress of your local machine.

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



5.Activate virtualenv
  cd into the project folder(dbms-project)
  source tutorial/bin.activate
  
6.
