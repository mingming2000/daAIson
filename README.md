<p align="left"><img src = https://github.com/mingming2000/daAIson/assets/102716945/fcac4a72-0d84-47e3-ac4d-b200684067dd width="200" height="200"></p>

We are `daAIson` at Korea Univ. [HandS](https://hands.korea.ac.kr/) 

<br>
<br>

![image](https://github.com/mingming2000/daAIson/assets/102716945/69e5ae9b-3488-426a-9ecf-a3037c19946c)


<br>

>BlindBee(BB) assists `the visually impaired` in `distinguishing everyday objects` like containers and cosmetic products.
><br>BB prints `QR codes` for storing the name of object, and when it is recognized by the camera, the name will be spoken.
><br>Furthermore, BB prints `Braille` beside QRcode, so it can also be recognized without using camera.
><br>BB operates using voice The device is `voice-operated` for convenience.
<br>
<br>
<br>

# BlindBee
<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/102716945/62233d26-fd40-4f8d-b4ee-a5bd34a07adc width="500" height="500"></p>
<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/102716945/d7551504-5956-47ff-97ed-0d8f79a19199 width="398" height="500"></p>

<br>
<br>
<br>


# Table of content
 1. [Motivation](#Motivation)
    1) [Ideas](#Ideas)
 3. [Software](#Software)
    1) [State Diagram](#State-Diagram)
    2) [File Hierarcy](#File-hierarcy)
 5. [Hardware](#Hardware)
    1. [Design](#Design)
    2. [Circuit files](#Circuit-files)
    3. [Simple Diagram of Circuit](#Simple-diagram-of-circuit)
    4. [Usage of Each Components](#Usage-of-Each-Components)
 6. [Discussion](#Discussion)

<br>
<br>
<br>


Motivation
=============
Storage containers, PET bottles, and commonly sold cosmetics and medicine bottles are 'everyday objects'. They all have standardized shapes, but there are numerous products with different contents. While sighted individuals can differentiate these objects through visual cues, it is nearly impossible for visually impaired individuals [to do.](https://www.joongang.co.kr/article/23615660#home)

Currently, there are options available, such as smartphone apps that read text or video calls with social workers, to assist visually impaired individuals. However, these methods are inconvenient for visually impaired individuals as they require pressing application buttons or making phone calls

Additionally, some products have `Braille` on them, but it is inadequate. For example, all beverages may be labeled simply as "beverage" or "carbonated," making it hard to distinguish specific product names. To address these issues and enable visually impaired individuals to independently identify objects, our team aimed to create a device that can easily store and differentiate object information.

Ideas
-----------
The device incorporates two main approaches: `QR codes` and `Braille output`. QR codes are used to store information about the objects, making it easy to encode and decode data. The device utilizes a camera and `openCV` library to recognize QR codes visually. To assist `tactile` recognition, Braille is printed around the QR codes so that visually impaired individuals can differentiate objects using their sense of touch. Instead of expensive Braille printers, the device employs affordable solenoid actuators to create embossed Braille on paper.

To ensure ease of use for visually impaired users, our team designed the device to be entirely voice-operated. They utilized `Google API` for text-to-speech and speech-to-text conversions, enabling visually impaired individuals to interact with the device using voice commands.

Considering the unique needs of visually impaired individuals, our team also paid special attention to the design of the device. They used a `yellow color` for the device's appearance, which is easy for visually impaired individuals to recognize. Additionally, they chose a distinctive shape, resembling a bee, to facilitate tactile differentiation.



<br>
<br>
<br>


# Software
You can find pip list here ["pip-list"](https://github.com/mingming2000/daAIson/blob/main/docs/software.md). All codes are written by python.

Technologies used are
- HTTP using Flask
- Google API (Speech, Text to Speech)
- Multiprocessing

## State Diagram
<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/102716945/3711c096-3833-4f30-986e-648e5f23e6d4></p>

- `S0` : standby. When switch on, it changes to State1 (S1)
- `S1` : BlindBee starts. says "What can I help you?"
  <br>If user answers "Detecting"(detect object), the state changes to state2.
  <br>elif user answers "Saving"(register object), the state changes to state3. 
- `S2` : client starts to detect QR code and returns name of QR code.
  <br>When server receives this, it converts it to object name refering qr.csv and speaks "The object is {object name}"
- `S3` : When user says object name and QR number, server saves them in qr.csv

## File hierarcy
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

# Hardware
## Design
We made BlindBee in the form of `bees and beehives`. Becuase yellow is easy to recognize for the blind and uneven shape is differ from other home appliance.

The interior and exterior design of the product was designed through a program called `Free Cad` and produced through a 3d printer at Korea University's makersplace.
<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/138636306/dbb97edd-246c-46b9-b045-129efbaf26ad "BB_camera" width="300%" height="300%"></p>


- BB_camera - Here is a device that `recognizes QR code`.


<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/138636306/44a77ba6-b23f-44ab-8620-5d9a44a58352 width="300%" height="300%"></p>

- BB_Body - There is a device that `outputs voices` for each situation and `recognizes voices` and a device that `prints braille`.
<br>size: 150X150X120 [HxWxZ] (mm)





## Simple diagram of circuit
This is a simple diagram of how the circuit will connect and work.

<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/140086562/b85c7f6b-a7ca-436a-873d-443dacd9a477>

This is a picture of how the circuit's power is distributed.
<p align="center"><img src = https://github.com/mingming2000/daAIson/assets/140086562/54b52231-a0ab-41f1-82fc-9bf2325800f7>

 **Body**
 - First floor of circuit is `power connection` layer. 
 - Second floor of circuit is `Arduino-Relay` layer. We use Arduino nano to control Relay-module and `Infrared-sensor`. Relay-module is used to `control Solenoids` that prints braille. 
 - Third floor of circuit is `Raspberry Pi` layer. We use Raspberry Pi to run overall code of our product and communicate with another Raspberry Pi in Camera module part. Also battery charging module is connected to 5V electricity and GND, so we can charge lithium polymer battery in camera module.
<br>

 **Camera Module**
 - On Camera Module part, RaspberryPi 4 recives `QRcode` from picamera connected to it. After it decodes the name of object, it sends to server(RaspberryPi4 in the body).
<br>

## Further information

Check out this [file](./docs/hardware.md) offering details of circuit and compenets. 

<br>
<br>
<br>

# Experiment video

# Discussion
1. It would be more useful to add a feature that identifies objects based on information such as their shape, size, and text written on the surface, without the need for QR code recognition, using deep learning.

2. For scalability, the information about visually impaired users' belongings stored in Blind Bee can be integrated with their smartphone apps, allowing the functionality to be extended to external devices and platforms. In this case, additional features that were not implemented in Blind Bee can be provided using technologies from different platforms.



