from blindbee import record
from blindbee import stt

if __name__ == '__main__':
    r = record.Record()
    r.recording("temp_input_audio.linear16")

    s = stt.SpeechToText()
    test_stt = s.transcribe_audio_to_text("temp_input_audio.linear16")