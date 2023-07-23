import qrcode
import tifffile as tf
import cv2

cap = cv2.VideoCapture(0) # 0번째 카메라 장치 (Device ID)
qr = cv2.QRCodeDetector()

if not cap.isOpened(): # 카메라가 잘 열리지 않은 경우
    exit() # 프로그램 종료
    
while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    cv2.imshow('camera', frame)
    
    data, box, straight_qrcode = qr.detectAndDecode(frame)
    if(data):
        print(data)
        break

    if cv2.waitKey(1) == ord('q'): # 사용자가 q 입력
        break

cap.release()
cv2.destroyAllWindows()


# Create sample QRcode
"""
img = qrcode.make('https://github.com/mingming2000/daAIson') # tmp dir
img.save("./test.png")
print("Image saved")
"""