# daAIson!

## Clone Our Github Project!
```
$ git clone https://github.com/mingming2000/daAIson.git
```

## Project overview (Coming Soon)

![image](https://github.com/mingming2000/daAIson/assets/102716945/69e5ae9b-3488-426a-9ecf-a3037c19946c)

Motivation
=============
The passage describes a device designed to assist visually impaired individuals in distinguishing and identifying various objects commonly found in daily life, such as sealed containers, PET bottles, cosmetics, and medicine bottles, which may have similar shapes but contain different contents. The current methods available to visually impaired individuals, such as smartphone apps that read text or video calls with social workers for assistance, have limitations. The proposed device aims to address these challenges by providing a user-friendly way for visually impaired individuals to store and differentiate object information.

Ideas
====================
The device incorporates two main approaches: QR codes and Braille output. QR codes are used to store information about the objects, making it easy to encode and decode data. The device utilizes a camera and open CV technology to recognize QR codes visually. To assist tactile recognition, Braille is printed around the QR codes so that visually impaired individuals can differentiate objects using their sense of touch. Instead of expensive Braille printers, the device employs affordable solenoid actuators to create embossed Braille on paper.

To ensure ease of use for visually impaired users, the team designed the device to be entirely voice-operated. They utilized Google API for text-to-speech and speech-to-text conversions, enabling visually impaired individuals to interact with the device using voice commands.

Considering the unique needs of visually impaired individuals, the team also paid special attention to the design of the device. They used a yellow color for the device's appearance, which is easy for visually impaired individuals to recognize. Additionally, they chose a distinctive shape, resembling a bee, to facilitate tactile differentiation.

In summary, the passage discusses the development of a device with QR codes and Braille output to assist visually impaired individuals in identifying and distinguishing everyday objects. The device is voice-operated and designed with specific features to cater to the needs of visually impaired users.

Blind Bee Design
=============

We made BB in the form of bees and beehives. 
This was done to make it easy for visually impaired people to spot because yellow is the most visible color, and to make it easy to be sure that it is a BB product through a unique design. 
The interior and exterior design of the product was designed through a program called "Free Cad" and produced through a 3d printer at Korea University's makersplace.

the size of body is 150 X 150 X 120 (mm)

PICTURE
---------
![BB_camera](https://github.com/mingming2000/daAIson/assets/138636306/dbb97edd-246c-46b9-b045-129efbaf26ad "BB_camera")

BB_camera - Here is a device that recognizes qr.



![BB_outside](https://github.com/mingming2000/daAIson/assets/138636306/89b549f9-83c0-44e7-986e-9c3ad1be6121 "BB_outside")

BB_Body - There is a device that outputs voices for each situation and recognizes voices and a device that prints braille.

CAD file
----------
here is cad files 

[BB_CAD.zip](https://github.com/mingming2000/daAIson/files/12224967/BB_CAD.zip)


In cad_BB.zip, the following folders and files are composed.

![CAD_excell](https://github.com/mingming2000/daAIson/assets/138636306/9e69a6b9-5208-4751-a4a7-e9bf905a0547)

Blind Bee Composition
=============
BB is composed of many circuits and components such as Raspberry Pi 4 and Arduino Nano.
We will show you simple circuit diagram and explain usage of each circuit and component. 

Circuit file
--------------
[Circuit Diagram](https://github.com/mingming2000/daAIson/files/12224828/Circuit.Diagram.xlsx)

This is a simple diagram of how the circuit will connect and work.

![circuit_overview](https://github.com/mingming2000/daAIson/assets/138636306/90e2c154-08db-4d0e-b6ac-1404fd2c0482)

This is a picture of how the circuit's power is distributed.


![circuit_power](https://github.com/mingming2000/daAIson/assets/138636306/4cfde137-8fe3-4d2d-aba0-afd847fcdf9c)


> 1F
> - First floor of circuit is power connection layer. We get 12V electricity from power supply and also get 5v electricity from external power using 5V converter. We use box socket for convinience of supplying power. Box socket is emplaced on each layer of circuit, so we can easily divide and supply 5V / 12V power. Also we use header socket for solenoids. Organizing 12V electricity and output of Relay-module in header socket for easy connecting to solenoids.

> 2F
> - Second floor of circuit is Arduino-Relay layer. We use Arduino nano to control Relay-module and Infrared-sensor. Arduino nano get 5V, 20mA electricity to VCC and GND PIN and Arduiono send output signal to Relay-module(PIN 2,3,5,6,7,8) and Infrared-sensor (PIN 10).
> - Relay-module is used to control Solenoids. we connect 12V electricity to COM terminal of Relay-module. If signal is sent to Signal-input of Relay-module, 12V electricity is supplied to Solenoids. 

> 2.5F (Solenoids circuit)
> - This layer is connection circuit of Infrared-sensor / Solenoids and 2F. We use header sockets to easily distribute electric wire for each VCC and GND and SIG.

> 3F
> - 


Possiblilty of futher developement
=============
1. It would be more useful to add a feature that identifies objects based on information such as their shape, size, and text written on the surface, without the need for QR code recognition, using deep learning.

2. For scalability, the information about visually impaired users' belongings stored in Blind Bee can be integrated with their smartphone apps, allowing the functionality to be extended to external devices and platforms. In this case, additional features that were not implemented in Blind Bee can be provided using technologies from different platforms.

## A Quick Guide for Git/Github and Miniconda/Anaconda
- Check out this [foloder](./docs/) that offers a quick guide for begineers.
- There may be some confusion when reading the documentation because of my poor english skills. Thus, if you have questions about this, feel free to contact me (HeumWoo Park).
- I wish you success in this project. Good Luck :) 
