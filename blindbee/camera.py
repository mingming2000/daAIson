from typing import *
import logging
# from abc import abstractmethod, abstractclassmethod, abstractproperty

from time import sleep
import qrcode as qr
import cv2
import numpy as np

# from blindbee import flask_server///

# class _Interface(object):
#     @abstractproperty
#     def image(self): ...

#     @abstractmethod
#     def regqr(self): ...


class BlindBeeCamera(object):
    def __init__(self):
        from picamera import PiCamera
        '''
            Hello, world!
        '''
        self._qr_detector = cv2.QRCodeDetector()
        self._cam = PiCamera()
        self._image_file = "test.jpg"

    # @staticmethod
    # def get_outcome2():
    #     return self.regqr()

    # @classmethod
    # def get_outcome(cls):
    #     return self.regqr()

    @property
    def image(self) -> np.ndarray :
        self._cam.start_preview()
        self._cam.capture(self._image_file)
        self._cam.stop_preview()
        return cv2.imread(self._image_file)

    def recognize_qr(self):
        while True:
            cur_img = self.image
            data, box, straight_qrcode = self._qr_detector.detectAndDecode(cur_img)
            if data:
                print(data)
                break
        return data, box, straight_qrcode

    def testing(self):
        while True:
            cur_img = self.image
            data, box, straight_qrcode = self._qr_detector.detectAndDecode(cur_img)
            print("-------------------------------------------------------")
            print("Camera is working. The image is: ")
            print(cur_img)
            print("-------------------------------------------------------")
            if data:
                print(f"QR code is recognized as {data}")
                break
        return data, box, straight_qrcode

    # def regqr(self):
    #     self.cam.start_preview()
    #     qr = cv2.QRCodeDetector()
    #     # frame = np.empty((240, 320, 3))
    #     #sleep(10)

    #     # Recognize QRcode
    #     self.cam.capture("test.jpg")
    #     frame = cv2.imread("test.jpg")

    #     data, box, straight_qrcode = qr.detectAndDecode(frame)
    #     while(True):
    #         if(data):
    #             print(data)
    #             break

    #     self.cam.stop_preview()
        
    #     return data, box, straight_qrcode

