import RPi.GPIO as GPIO
import time

class SystemOnOff(object):
    def __init__(self) -> None:
        
        TouchInPin = 12
        TouchOutPin = 4

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TouchInPin, GPIO.IN)
        GPIO.setup(TouchOutPin,GPIO.OUT)
        
#터치 센서 터치 ->1출력, 노터치 0출력
    def Touch(self):
        try:
            while True:
                if GPIO.input(self.TouchInPin)==True:
                    return 1 # 음성인식 함수 시작 
                else:
                    return 0 # 음성인식 함수 시작
        except KeboardInterrupt:
            GPIO.cleanup()
            
            
#카메라모듈 핀 연결 확인 
    #위에 벌 본체에서 떨어지면 바로 작동하도록 설정 떨어지면 1 아니면 0 출력
    #연결된 상태면 음성 명령 했을 때 카메라 작동 하도록 1 출력 
    def BeeConnect(self):
        ChargerPin = 18  # 확인하려는 GPIO 핀 번호
        GPIO.setmode(GPIO.BCM)
        

        GPIO.setup(ChargerPin, GPIO.IN)
        pin_state = GPIO.input(ChargerPin)

        if pin_state == GPIO.HIGH:
            print("GPIO 핀이 HIGH(1) 상태입니다. 외부 기기가 연결되었을 수 있습니다.")
            # 음성 명령에 대한 리턴 받기 
            return 0
        else:
            print("GPIO 핀이 LOW(0) 상태입니다. 외부 기기가 연결되지 않았을 수 있습니다.")
            return 1
            
            
    def close(self):
        GPIO.cleanup()
