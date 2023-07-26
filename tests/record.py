import pyaudio
import wave

class Record (object):
    def __init__(self) -> None:
        p = pyaudio.PyAudio()
        default_input_device_info = p.get_default_input_device_info()
        
        

    def store (self):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        # CHANNELS = default_input_device_info['maxInputChannels']  
        CHANNELS = 9
        RATE = 8000
        RECORD_SECONDS = 5
        WAVE_OUTPUT_FILENAME = "output.wav"
        input_device_index = 4
        stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=input_device_index,
                frames_per_buffer=CHUNK)
        
        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
            print("Recording is finished.")
            stream.stop_stream()
            stream.close()
            p.terminate()
            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
            wf.close()
        return frames
    



# wav 파일 읽기

'''
import wave
import sys

import pyaudio

CHUNK = 1024 #안되면 4096으로

if len(sys.argv) < 2:
    print(f'Plays a wave file. Usage: {sys.argv[0]} filename.wav')
    sys.exit(-1)

with wave.open(sys.argv[1], 'rb') as wf:
    # Instantiate PyAudio and initialize PortAudio system resources (1)
    p = pyaudio.PyAudio()

    # Open stream (2)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Play samples from the wave file (3)
    while len(data := wf.readframes(CHUNK)):  # Requires Python 3.8+ for :=
        stream.write(data)

    # Close stream (4)
    stream.close()

    # Release PortAudio system resources (5)
    p.terminate()
    '''