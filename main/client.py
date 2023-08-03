import requests
import json
import RPi.GPIO as GPIO 
import time

from blindbee import camera


URL = 'http://192.168.137.87:5000/send'


# def send_json_to_server(data, server_url):
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post(server_url, data=data, headers=headers)
#     return response.json()

def send_qrname_to_server(qr_name: str, server_url: str):
    server_url += f"/{qr_name}"
    print(server_url)
    response = requests.get(server_url)
    return response, response.content


# 사용할 GPIO 핀의 번호를 설정
button_pin = 27
 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) #핀모드 설정

# 버튼 핀의 입력설정 , PULL DOWN 설정 
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 


if __name__ == '__main__':
    debug: bool = True
    try:
        while(True):
            if GPIO.input(button_pin) == GPIO.HIGH:
                print("waiting...", end='\r')
                continue
            # Replace 'http://external_ip_address:port/receive_json' with the actual URL of your Flask server
            
            # Recognize QR code
            if not debug:
                qr_scanner = camera.BlindBeeCamera()
                name, _, _ = qr_scanner.regqr()
            else:
                name = 'one'  # for Debugging
            print(name)
            
            # Replace `sample_data.json` with the path to your JSON file
            # file = {"value": name}
            # print(file)
            # json_data = json.dumps(file)

            response_data = send_qrname_to_server(name, URL)
            print(response_data)
            time.sleep(4)
    except KeyboardInterrupt:
        print("Stop..")