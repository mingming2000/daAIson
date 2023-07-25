import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀 번호 설정
SPEAKER_PIN = 18

# GPIO 핀 번호 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(SPEAKER_PIN, GPIO.OUT)

def turn_speaker_on():
    GPIO.output(SPEAKER_PIN, GPIO.HIGH)

def turn_speaker_off():
    GPIO.output(SPEAKER_PIN, GPIO.LOW)

try:
    while True:
        turn_speaker_on()
        time.sleep(1)
        print()
        turn_speaker_off()
        time.sleep(1)

except KeyboardInterrupt: 
    GPIO.cleanup()
