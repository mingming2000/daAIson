from blindbee import BlindBeeCamera
from blindbee import stt
from test_onoff import SystemOnOff
from test_rasp2ino import Rasp2Ino
from test_record import Record
from blindbee import BlindBeeCamera, TextToSpeech, tts
from blindbee import (
    stt, tts,
    BlindBeeCamera, 
    TextToSpeech
)

n = input("1-picamera 2-stt 3-touch 4-charger 5-r2a 6-record 7-ttsandstt 8-tts 9-speaker")

if n ==1:
    if __name__ == "__main__":
        #run_quickstart()
        # $ export GOOGLE_APPLICATION_CREDENTIALS="/home/dspi/storage/dauntless-graph-393517-4fc404d248f0.json"

        cam = BlindBeeCamera()
        data, box, straight_qrcode = cam.testing()



elif n ==2:

    if __name__ == '__main__':
        test_stt = stt.SpeechToText()
        test_stt.testing()
        
    
    
    

#systemonoff 
#touchin 12 out 4 charger 18

elif n ==3 :
    a = -1 
    a = SystemOnOff.Touch()
    print (a)

elif n == 4:
    a = -1 
    a = SystemOnOff.BeeConnect()
    print (a)
    
elif n==5 :
    inputnum = input("arduino")
    Rasp2Ino.send_number_to_arduino(inputnum)

elif n==6 :
    lis = Record.store()
    print (lis)
    
    
    
elif n==7 :

    if __name__ == '__main__':
        test_stt = stt.SpeechToText()
        TTS= tts.TextToSpeech()

        test_stt.testing()
        TTS.testing()
        test_stt.testing()
        TTS.testing()
        
    
    
    
# Text To Speech API
# $ export GOOGLE_APPLICATION_CREDENTIALS="/home/dspi/storage/dauntless-graph-393517-4fc404d248f0.json" 


# Speech To Text API
# $ export GOOGLE_APPLICATION_CREDENTIALS="/home/dspi/storage/dauntless-graph-393517-0433c47d97ff.json"
elif n==8 :
    if __name__ == "__main__":

        """ 
        When testing QR -> tts
        """
        # cam = BlindBeeCamera()
        # data, box, straight_qrcode = cam.testing()
        
        TTS= tts.TextToSpeech()
        TTS.testing()
