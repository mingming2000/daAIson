from blindbee import BlindBeeCamera, TextToSpeech, tts

# Text To Speech API
# $ export GOOGLE_APPLICATION_CREDENTIALS="/home/dspi/storage/dauntless-graph-393517-4fc404d248f0.json" 


# Speech To Text API
# $ export GOOGLE_APPLICATION_CREDENTIALS="/home/dspi/storage/dauntless-graph-393517-0433c47d97ff.json"

if __name__ == "__main__":

    """ 
    When testing QR -> tts
    """
    # cam = BlindBeeCamera()
    # data, box, straight_qrcode = cam.testing()
    
    TTS= tts.TextToSpeech()
    TTS.testing()

