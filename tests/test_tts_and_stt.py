from blindbee import (
    stt, tts,
    BlindBeeCamera, 
    TextToSpeech
)

if __name__ == '__main__':
    test_stt = stt.SpeechToText()
    TTS= tts.TextToSpeech()

    test_stt.testing()
    TTS.testing()
    test_stt.testing()
    TTS.testing()

