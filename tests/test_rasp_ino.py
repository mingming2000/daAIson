import serial

ser = serial.Serial('/dev/ttyUSB1', 9600) # 시리얼 포트와 통신 속도 설정 (아두이노와 동일해야 함)

try:
    while True:
        data = input("메시지를 입력하세요: ")
        ser.write(data.encode()) # 아두이노로 데이터 전송

        response = ser.readline() # 아두이노로부터 데이터 수신
        print("아두이노로부터 받은 데이터:", response.decode())
except KeyboardInterrupt:
    ser.close() # Ctrl+C로 프로그램 종료 시 시리얼 포트 닫기

