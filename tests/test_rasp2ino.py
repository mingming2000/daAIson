import time

class Rasp2Ino(object):
    def __init__(self) -> None:
        pass
    
    def send_number_to_arduino(number):
        try:
            ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) # 아두이노와 시리얼 통신을 위한 포트 및 보드레이트 설정
            time.sleep(2) # 아두이노 부팅 시간을 고려하여 적절한 대기 시간 설정

            ser.write(str(number).encode()) # 숫자를 바이트 형태로 인코딩하여 아두이노로 전송
            print(f"라즈베리파이에서 아두이노로 숫자 {number}를 전송했습니다.")

            ser.close()
        except serial.SerialException as e:
            print(f"시리얼 통신 오류: {e}")

    