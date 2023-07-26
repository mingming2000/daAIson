import RPi.GPIO as GPIO
import time

TouchInPin = 12
TouchOutPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(TouchInPin, GPIO.IN)
GPIO.setup(TouchOutPin,GPIO.OUT)
try:
    while True:
        if GPIO.input(TouchInPin)==Ture:
            GPIO.output(TouchOutPin,True) # 음성인식 함수 시작 
        else:
            GPIO.output(TouchOutPin,False) # 음성인식 함수 시작
except KeboardInterrupt:
    GPIO.cleanup()