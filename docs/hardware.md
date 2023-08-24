# CAD files
<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/138636306/06ad6d9f-a75c-4f8e-a98f-6fb53f00085b width="45%" height="45%">

You can also download CAD files [here](https://github.com/mingming2000/daAIson/files/12224967/BB_CAD.zip).

# Circuit files

BB is composed of many circuits and components such as Raspberry Pi 4 and Arduino Nano.
<br>This is circuit diagram and explain usage of each circuit and component.
<br>You can also download circuit files [here](https://github.com/mingming2000/daAIson/files/12224828/Circuit.Diagram.xlsx)
![blindbee](https://github.com/mingming2000/daAIson/assets/102716945/3a12aceb-51d2-4a83-a206-7f2cd16e2af0)

## Simple diagram of circuit
This is a simple diagram of how the circuit will connect and work.

<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/140086562/b85c7f6b-a7ca-436a-873d-443dacd9a477>

This is a picture of how the circuit's power is distributed.
<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/140086562/54b52231-a0ab-41f1-82fc-9bf2325800f7>


 **1F**
 - First floor of circuit is `power connection` layer. We get 12V electricity from power supply and also get 5v electricity from external power using 5V converter. We use box socket for convinience of supplying power. Box socket is emplaced on each layer of circuit, so we can easily divide and supply 5V / 12V power. Also we use header socket for solenoids. Organizing 12V electricity and output of Relay-module in header socket for easy connecting to solenoids.

 **2F**
 - Second floor of circuit is `Arduino-Relay` layer. We use Arduino nano to control Relay-module and `Infrared-sensor`. Arduino nano get 5V, 20mA electricity to VCC and GND PIN and Arduiono send output signal to Relay-module(PIN 2,3,5,6,7,8) and Infrared-sensor (PIN 10).
 - Relay-module is used to control Solenoids. we connect 12V electricity to COM terminal of Relay-module. If signal is sent to Signal-input of Relay-module, 12V electricity is supplied to Solenoids. 

 **2.5F (Solenoids circuit)**
 - This layer is connection circuit of Infrared-sensor / Solenoids and 2F. We use header sockets to easily distribute electric wire for each VCC and GND and SIG. Solenoids activate sequentially only when they get 12V electricity from Relay-module, so power can be ditributed efficiently.  

 **3F**
 - Third floor of circuit is Raspberry Pi layer. We use Raspberry Pi to run overall code of our product and communicate with another Raspberry Pi in Camera module part. Also battery charging module is connected to 5V electricity and GND, so we can charge lithium polymer battery in camera module.

 **Camera Module**
 - On Camera Module part, another Raspberry Pi 4 and camera module is connected to PCB board. As Camera Module is separated with main body, so we should prepare another power supply for Raspberry Pi 4. We use two 3.4V lithuim polymer battery and connect it serially. two serially connected battery supply 7.8V voltage, but rated voltage of Raspberry Pi 4 i 5V. So we use regulator for stepping down voltage 7.8V to 5V

# Usage of Each Components

### Raspberry Pi
Raspberry Pi on 2F run overall code of our project and also take input from MIC, print output to speaker and control Arduino nano using serial communication. Raspberry Pi on camera module is connected to camera module and communicate image information in real time with Raspberry Pi on 2F. Rated voltage and current for Raspberry Pi is 5V, 3A. As it control entire product, we put effort to stably supplying power for Raspberry Pi.

### Arduino Nano
Arduino Nano communicate with Raspberry Pi with serial communication. When Nano get signal, it activate relay module and infrared sensor as compiled code. Likewise Arduino control our braille printer, so stable power supplying is important in our project

### Infrared Sensor (SEN030111)

Infrared Sensor detect move between two infrared sensor. We use this sensor for detecting insert of paper in printer. When sensor detect code, arduino get signal from sensor and send signal to relay modules.

### Relay Module
![1CH Relay Module](https://github.com/mingming2000/daAIson/assets/140086562/7c04d09b-3762-45d1-b167-bd1f1cfc920b)
Each Relay Module has 6 port.VCC and GND for activation and SIG input for control. COM port is common terminal which always connected to relay module. We apply 12V voltage to COM port. NO / NC ports are core terminals of relay module. If there's no signal input COM terminal is connected to NO terminal. If module get electrical signal to SIG port, COM termial is connected to NC terminal. It makes relay module as sort of switch. We use one 2CH Relay module and one 4CH Relay module.

### Solenoid (JF-0530B-12V)
Solenoid activate when 12V or more voltage applied to itself. By magnetic force iron rod in solenoids move when electricity flows. We use this move of rod as printer. When paper is detected, we run code for printing. However power consumption of solenoid is higher than we think, so it is hard to activate 6 solenoids at once. We use relay module for individual control of solenoids. For each time only one solenoid activate, so we prevent shortage of power.

### Lithium Polymer Battery (DTP 804030 1000) & Battery Charging Module (SZH-EK026)
We use two 3.4V / 1000mAh lithium polymer battery. We connect is serially and use it as 7.8V power supply for Raspberry Pi. we use two battery, so battery capacity is 2000mAh. Rated current for Raspberry Pi is 3A. We can only use camera module for 2/3 hours (approximately 45 minutes). That's the reason why we need to use battery charging module. Battery charging module get power from extenal power, so we can stably supply power for battery.

### Regulator (AMS1117-5V)
As Rated Voltage of Raspberry Pi is 5V, we need to step down voltage of batteries. Otherwise overvoltage cause damage on Raspberry Pi board. Regulator is sort of step down convertor. It convert high voltage to specific voltage, besides regulator step down voltage to decided voltage regardless of input voltage. So we secure stable power consumption for Raspberry Pi by using regulator

### MIC / Speaker
First input device and last output device. Our voice detected in MIC converts to text file. Speaker also print voice which converted from text file.
