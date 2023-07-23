from typing import *
import logging
# from abc import abstractmethod, abstractclassmethod, abstractproperty

from picamera import PiCamera
from time import sleep
import qrcode as qr
import cv2
import numpy as np


# class _Interface(object):
#     @abstractproperty
#     def image(self): ...

#     @abstractmethod
#     def regqr(self): ...


class BlindBeeCamera(object):
    '''
        Hello, world!
    '''
    _qr_detector = cv2.QRCodeDetector()
    _cam = PiCamera()
    _image_file = "test.jpg"

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

    def regqr(self):
        cur_img = self.image
        data, box, straight_qrcode = self._qr_detector.detectAndDecode(cur_img)
        while True:
            if data:
                print(data)
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

