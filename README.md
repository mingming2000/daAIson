![image](https://github.com/mingming2000/daAIson/assets/102716945/69e5ae9b-3488-426a-9ecf-a3037c19946c)

>We are `daAIson` of Korea Univ. [HandS](https://hands.korea.ac.kr/)
><br>We made `BlindBee` in the form of bees and beehives. 
><br>
><br>This was done to make it easy for `visually impaired people` to spot because yellow is the most visible color, and to make it easy to be sure that it is a BB product through a unique design. 

<br>
<br>
<br>

# BlindBee
<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/102716945/62233d26-fd40-4f8d-b4ee-a5bd34a07adc width="500" height="500"></p>

<br>
<br>
<br>
<br>
<br>
<br>

# Table of content
 1. [Motivation](#Motivation)
    1) [Ideas](#Ideas)
 3. [Software](#Software)
    1) [State Diagram](#State-Diagram)
    2) [File Hierarcy](#file-hierarcy)
 5. [Hardware](#Hardware)
    1. [Design](#Design)
    2. [Circuit files](#Circuit-files)
    3. [Simple Diagram of Circuit](#Simple-diagram-of-circuit)
 6. [Discussion](#Discussion)
 7. [Appendix](#Appendix)

<br>
<br>
<br>
<br>
<br>
<br>

Motivation
=============
Sealed containers, PET bottles, and commonly sold cosmetics and medicine bottles are everyday objects. They all have standardized shapes, but there are numerous products with different contents. While sighted individuals can differentiate these objects through visual cues, it is nearly impossible for visually impaired individuals to do the same. [(ref.)](https://www.joongang.co.kr/article/23615660#home)

Currently, there are options available, such as smartphone apps that read text or video calls with social workers, to assist visually impaired individuals. However, these methods may be challenging for visually impaired individuals as they require pressing application buttons or making phone calls, which can be difficult using a phone.

Additionally, some products have Braille on them, but it is inadequate. For example, all beverages may be labeled simply as "beverage" or "carbonated," making it hard to distinguish specific product names. To address these issues and enable visually impaired individuals to independently identify objects, the team aimed to create a device that can easily store and differentiate object information.

Ideas
-----------
The device incorporates two main approaches: QR codes and Braille output. QR codes are used to store information about the objects, making it easy to encode and decode data. The device utilizes a camera and open CV technology to recognize QR codes visually. To assist tactile recognition, Braille is printed around the QR codes so that visually impaired individuals can differentiate objects using their sense of touch. Instead of expensive Braille printers, the device employs affordable solenoid actuators to create embossed Braille on paper.

To ensure ease of use for visually impaired users, the team designed the device to be entirely voice-operated. They utilized Google API for text-to-speech and speech-to-text conversions, enabling visually impaired individuals to interact with the device using voice commands.

Considering the unique needs of visually impaired individuals, the team also paid special attention to the design of the device. They used a yellow color for the device's appearance, which is easy for visually impaired individuals to recognize. Additionally, they chose a distinctive shape, resembling a bee, to facilitate tactile differentiation.

In summary, the passage discusses the development of a device with QR codes and Braille output to assist visually impaired individuals in identifying and distinguishing everyday objects. The device is voice-operated and designed with specific features to cater to the needs of visually impaired users.


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Software
You can find pip list [here](#pip-list). All codes are written by python.

Technologies used are
- The HyperText Transfer Protocol (HTTP) using Flask
- Google API (Speech, Text to Speech)
- Multiprocessing

## State Diagram
<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/102716945/3711c096-3833-4f30-986e-648e5f23e6d4></p>

- `S0`: standby. When switch on, it changes to State1 (S1)
- `S1`: starts BlindBee. says "What can I help you?"
  <br>If user answers "Detecting"(detect object), the state changes to state2.
  <br>elif user answers "Saving"(register object), the state changes to state3. 
- `S2`: client starts to detect QR code and returns name of QR code.
  <br>When server receives this, it converts it to object name refering qr.csv and speaks "The object is {object name}"
- `S3`: When user says object name and QR number, server saves them in qr.csv

## file hierarcy
<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/102716945/6a18278c-bcc1-48e8-bb03-1b3a5c41b27e></p>
<br>

### 1) Server (Main Body)

| file name | operation |
|:----------|:----------|
| **main.py**        | When button pushed, **BlindBee program starts** by running this file. <br>This runs two python definition(**Flask server** and service.py) by using **multiprocessing**|
| **state.py**       | difines **4 state (S0 ~ S4)** and logs current state. <br>Details are described [here](#State-Diagram)|
| **qr.csv**         | works like **dynamic QR** by linking qr data with object name.|
| **text_color.py**  | customize state text color|
| **record.py**      | records user's audio and stt(speech to text) **transribes this to text**.|
| **service.py**     | defines the operation according to the **state**<br>And communicates with arduino for printing braille|
| **stt.py**         | transcribes audio to text by using google **'Speech To Text API'**|
| **tts.py**         |(1) plays audio files  <br>(2) converts input text to audio and save  <br>(3) **converts input text(QR name) to audio and just play it** <br> by using google **'Text To Speech API'**|

<br>

### 2) Client (Camera Module)
| file name | operation |
|:----------|:----------|
|**client.py**      |When button on the camera module pushed, <br>picamera starts to **recognize QR codes** and request to server using **Flask**.|
|**camera.py**      |**recognizes QR** code|

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Hardware
## Design
The interior and exterior design of the product was designed through a program called "Free Cad" and produced through a 3d printer at Korea University's makersplace.
You can also download CAD files [here](https://github.com/mingming2000/daAIson/files/12224967/BB_CAD.zip).
![BB_camera](https://github.com/mingming2000/daAIson/assets/138636306/dbb97edd-246c-46b9-b045-129efbaf26ad "BB_camera")

- BB_camera - Here is a device that recognizes qr.



![BB_outside](https://github.com/mingming2000/daAIson/assets/138636306/89b549f9-83c0-44e7-986e-9c3ad1be6121 "BB_outside")

- BB_Body - There is a device that outputs voices for each situation and recognizes voices and a device that prints braille.
<br>size: 150X150X120 [HxWxZ] (mm)

<br>


<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/138636306/9e69a6b9-5208-4751-a4a7-e9bf905a0547>

<br>

## Circuit files

BB is composed of many circuits and components such as Raspberry Pi 4 and Arduino Nano.
<br>This is circuit diagram and explain usage of each circuit and component.
<br>You can also download circuit files [here](https://github.com/mingming2000/daAIson/files/12224828/Circuit.Diagram.xlsx)
![blindbee](https://github.com/mingming2000/daAIson/assets/102716945/3a12aceb-51d2-4a83-a206-7f2cd16e2af0)


## Simple diagram of circuit
This is a simple diagram of how the circuit will connect and work.

<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/138636306/90e2c154-08db-4d0e-b6ac-1404fd2c0482>

This is a picture of how the circuit's power is distributed.
<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/138636306/4cfde137-8fe3-4d2d-aba0-afd847fcdf9c>


 **1F**
 - First floor of circuit is power connection layer. We get 12V electricity from power supply and also get 5v electricity from external power using 5V converter. We use box socket for convinience of supplying power. Box socket is emplaced on each layer of circuit, so we can easily divide and supply 5V / 12V power. Also we use header socket for solenoids. Organizing 12V electricity and output of Relay-module in header socket for easy connecting to solenoids.

 **2F**
 - Second floor of circuit is Arduino-Relay layer. We use Arduino nano to control Relay-module and Infrared-sensor. Arduino nano get 5V, 20mA electricity to VCC and GND PIN and Arduiono send output signal to Relay-module(PIN 2,3,5,6,7,8) and Infrared-sensor (PIN 10).
 - Relay-module is used to control Solenoids. we connect 12V electricity to COM terminal of Relay-module. If signal is sent to Signal-input of Relay-module, 12V electricity is supplied to Solenoids. 

 **2.5F (Solenoids circuit)**
 - This layer is connection circuit of Infrared-sensor / Solenoids and 2F. We use header sockets to easily distribute electric wire for each VCC and GND and SIG. Solenoids activate sequentially only when they get 12V electricity from Relay-module, so power can be ditributed efficiently.  

 **3F**
 - Third floor of circuit is Raspberry Pi layer. We use Raspberry Pi to run overall code of our product and communicate with another Raspberry Pi in Camera module part. Also battery charging module is connected to 5V electricity and GND, so we can charge lithium polymer battery in camera module.

 **Camera Module**
 - On Camera Module part, another Raspberry Pi 4 and camera module is connected to PCB board. As Camera Module is separated with main body, so we should prepare another power supply for Raspberry Pi 4. We use two 3.4V lithuim polymer battery and connect it serially. two serially connected battery supply 7.8V voltage, but rated voltage of Raspberry Pi 4 i 5V. So we use regulator for stepping down voltage 7.8V to 5V


<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

Discussion
=============
1. It would be more useful to add a feature that identifies objects based on information such as their shape, size, and text written on the surface, without the need for QR code recognition, using deep learning.

2. For scalability, the information about visually impaired users' belongings stored in Blind Bee can be integrated with their smartphone apps, allowing the functionality to be extended to external devices and platforms. In this case, additional features that were not implemented in Blind Bee can be provided using technologies from different platforms.

<br>
<br>
<br>

## Appendix
### Clone Our Github Project!

```
$ git clone https://github.com/mingming2000/daAIson.git
```
### A Quick Guide for Git/Github and Miniconda/Anaconda
- Check out this [foloder](./docs/) that offers a quick guide for begineers.

<br>
<br>
<br>

### pip list
```
Package                       Version
----------------------------- ------------
arandr                        0.1.10
astroid                       2.5.1
asttokens                     2.0.4
automationhat                 0.2.0
beautifulsoup4                4.9.3
blinker                       1.4
blinkt                        0.1.2
buttonshim                    0.0.2
cachetools                    5.3.1
Cap1xxx                       0.1.3
certifi                       2020.6.20
chardet                       4.0.0
click                         7.1.2
colorama                      0.4.4
colorzero                     1.1
cryptography                  3.3.2
cupshelpers                   1.0
dbus-python                   1.2.16
distro                        1.5.0
docopt                        0.6.2
docutils                      0.16
drumhat                       0.1.0
envirophat                    1.0.0
ExplorerHAT                   0.4.2
Flask                         1.1.2
fourletterphat                0.1.0
future                        0.18.3
google-api-core               2.11.1
google-api-python-client      2.94.0
google-auth                   2.22.0
google-auth-httplib2          0.1.0
google-auth-oauthlib          1.0.0
google-cloud                  0.34.0
google-cloud-aiplatform       1.28.1
google-cloud-bigquery         3.11.4
google-cloud-core             2.3.3
google-cloud-domains          1.5.2
google-cloud-resource-manager 1.10.2
google-cloud-speech           2.21.0
google-cloud-storage          2.10.0
google-cloud-texttospeech     2.14.1
google-cloud-translate        3.11.2
google-cloud-vision           3.4.4
google-crc32c                 1.5.0
google-resumable-media        2.5.0
googleapis-common-protos      1.59.1
gpiozero                      1.6.2
grpc-google-iam-v1            0.12.6
grpcio                        1.56.2
grpcio-status                 1.56.2
html5lib                      1.1
httplib2                      0.22.0
idna                          2.10
iso8601                       2.0.0
isort                         5.6.4
itsdangerous                  1.1.0
jedi                          0.18.0
Jinja2                        2.11.3
lazy-object-proxy             0.0.0
logilab-common                1.8.1
lxml                          4.6.3
MarkupSafe                    1.1.1
mccabe                        0.6.1
microdotphat                  0.2.1
mote                          0.0.4
motephat                      0.0.3
mypy                          0.812
mypy-extensions               0.4.3
numpy                         1.25.1
oauthlib                      3.1.0
opencv-python                 4.6.0.66
packaging                     23.1
pantilthat                    0.0.7
parso                         0.8.1
pexpect                       4.8.0
pgzero                        1.2
phatbeat                      0.1.1
pianohat                      0.1.0
picamera                      1.13
picamera2                     0.3.9
pidng                         4.0.9
piexif                        1.1.3
piglow                        1.2.5
pigpio                        1.78
Pillow                        8.1.2
pip                           20.3.4
pri                           1.0.5
proto-plus                    1.22.3
protobuf                      4.23.4
psutil                        5.8.0
pyasn1                        0.5.0
pyasn1-modules                0.3.0
PyAudio                       0.2.13
pycairo                       1.16.2
pycups                        2.0.1
pydub                         0.25.1
pygame                        1.9.6
Pygments                      2.7.1
PyGObject                     3.38.0
pyinotify                     0.9.6
PyJWT                         1.7.1
pylint                        2.7.2
PyOpenGL                      3.1.5
pyOpenSSL                     20.0.1
pyparsing                     3.1.0
pypng                         0.20220715.0
PyQt5                         5.15.2
PyQt5-sip                     12.8.1
pyserial                      3.5b0
pysmbc                        1.0.23
python-apt                    2.2.1
python-dateutil               2.8.2
python-prctl                  1.7
PyYAML                        6.0.1
qrcode                        7.4.2
rainbowhat                    0.1.0
reportlab                     3.5.59
requests                      2.25.1
requests-oauthlib             1.0.0
responses                     0.12.1
roman                         2.0.0
RPi.GPIO                      0.7.0
rsa                           4.9
RTIMULib                      7.2.1
scrollphat                    0.0.7
scrollphathd                  1.2.1
Send2Trash                    1.6.0b1
sense-hat                     2.4.0
serial                        0.0.97
setuptools                    52.0.0
Shapely                       1.8.5.post1
simplejpeg                    1.6.4
simplejson                    3.17.2
six                           1.16.0
skywriter                     0.0.7
sn3218                        1.2.7
soupsieve                     2.2.1
spidev                        3.5
ssh-import-id                 5.10
thonny                        4.0.1
toml                          0.10.1
touchphat                     0.0.1
twython                       3.8.2
typed-ast                     1.4.2
typing-extensions             3.7.4.3
unicornhathd                  0.0.4
uritemplate                   4.1.1
urllib3                       1.26.5
v4l2-python3                  0.3.2
Wave                          0.0.2
webencodings                  0.5.1
Werkzeug                      1.0.1
wheel                         0.34.2
wrapt                         1.12.1
```

<br>
<br>
<br>

### Components

#### Raspberry Pi
Raspberry Pi on 2F run overall code of our project and also take input from MIC, print output to speaker and control Arduino nano using serial communication. Raspberry Pi on camera module is connected to camera module and communicate image information in real time with Raspberry Pi on 2F. Rated voltage and current for Raspberry Pi is 5V, 3A. As it control entire product, we put effort to stably supplying power for Raspberry Pi.

#### Arduino Nano
Arduino Nano communicate with Raspberry Pi with serial communication. When Nano get signal, it activate relay module and infrared sensor as compiled code. Likewise Arduino control our braille printer, so stable power supplying is important in our project

#### Infrared Sensor (SEN030111)
![Infrared Sensor](https://github.com/mingming2000/daAIson/assets/140086562/53d5daa9-d9cd-40d2-ad7b-b270e1659127)
Infrared Sensor detect move between two infrared sensor. We use this sensor for detecting insert of paper in printer. When sensor detect code, arduino get signal from sensor and send signal to relay modules.

#### Relay Module
![1CH Relay Module](https://github.com/mingming2000/daAIson/assets/140086562/f8633603-c7e3-4fc8-8a98-ef7e566220ec)                                          Each Relay Module has 6 port.VCC and GND for activation and SIG input for control. COM port is common terminal which always connected to relay module. We apply 12V voltage to COM port. NO / NC ports are core terminals of relay module. If there's no signal input COM terminal is connected to NO terminal. If module get electrical signal to SIG port, COM termial is connected to NC terminal. It makes relay module as sort of switch. We use one 2CH Relay module and one 4CH Relay module.

#### Solenoid (JF-0530B-12V)
Solenoid activate when 12V or more voltage applied to itself. By magnetic force iron rod in solenoids move when electricity flows. We use this move of rod as printer. When paper is detected, we run code for printing. However power consumption of solenoid is higher than we think, so it is hard to activate 6 solenoids at once. We use relay module for individual control of solenoids. For each time only one solenoid activate, so we prevent shortage of power.

#### Lithium Polymer Battery (DTP 804030 1000) & Battery Charging Module (SZH-EK026)
We use two 3.4V / 1000mAh lithium polymer battery. We connect is serially and use it as 7.8V power supply for Raspberry Pi. we use two battery, so battery capacity is 2000mAh. Rated current for Raspberry Pi is 3A. We can only use camera module for 2/3 hours (approximately 45 minutes). That's the reason why we need to use battery charging module. Battery charging module get power from extenal power, so we can stably supply power for battery.

#### Regulator (AMS1117-5V)
As Rated Voltage of Raspberry Pi is 5V, we need to step down voltage of batteries. Otherwise overvoltage cause damage on Raspberry Pi board. Regulator is sort of step down convertor. It convert high voltage to specific voltage, besides regulator step down voltage to decided voltage regardless of input voltage. So we secure stable power consumption for Raspberry Pi by using regulator

#### MIC / Speaker
First input device and last output device. Our voice detected in MIC converts to text file. Speaker also print voice which converted from text file.


<img src = https://github.com/mingming2000/daAIson/assets/102716945/fcac4a72-0d84-47e3-ac4d-b200684067dd>
