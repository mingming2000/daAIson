from blindbee import stt

if __name__ == '__main__':
    test_stt = stt.SpeechToText()
    test_stt.testing()

    # txt = test_stt.transcribe_audio_to_text("/home/dspi/daAIson/tests/temp_input_audio.linear16")
    # print(f"input text is : {txt}")