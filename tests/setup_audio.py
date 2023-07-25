# import pyaudio

# p = pyaudio.PyAudio()

# default_input_device_info = p.get_default_input_device_info()
# channels = default_input_device_info['maxInputChannels']

# print(f"기본 입력 장치의 채널 수: {channels}")
import pyaudio

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
print(numdevices)

for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))