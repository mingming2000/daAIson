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

## install openCV
```
$ sudo run apt-get update
$ sudo apt-get install -y libgl1-mesa-dev
``

## 패키지 URL 중복 설치된 것 삭제
```
cd /etc/apt/sources.list.d
sudo rm google-cloud-sdk.list
```
