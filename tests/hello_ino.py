import serial

# 시리얼 포트 설정
ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)  # 라즈베리 파이 3 이상일 경우 '/dev/ttyS0', 미만 버전일 경우 '/dev/ttyAMA0'을 사용

try:
    while True:
        # 아두이노로부터 메시지 수신
        if ser.in_waiting > 0:
            message = ser.readline().decode('utf-8').rstrip()
            print(f"Received message from Arduino: {message}")

        # 라즈베리 파이에서 아두이노로 메시지 전송
        message_to_send = "Hello Arduino!"
        ser.write(message_to_send.encode('utf-8'))
        print(f"Sent message to Arduino: {message_to_send}")

except KeyboardInterrupt:
    ser.close()

