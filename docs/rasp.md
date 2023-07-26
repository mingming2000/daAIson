## SSH (terminal)

# Connect RaspberryPi using terminal (When vscode doenn't work)
```
$ ssh pi@<raspberry ip>  # working on VScode (Ubuntu OS rasp)
```

# RasberryPi static IP Setup
```
$ sudo vi /etc/dhcpcd.conf
```

add below line to the end of the flie

```
interface wlan0
static ip_address="<current rasp IP>"                       # ex. static ip_address="192.168.137.87"
static routers="<current rasp IP (change last adress to 1)" # ex. static routers="192.168.137.1"
```
