import csv

from blindbee import tts
from blindbee import stt
from blindbee import record
from blindbee import camera

if __name__ == '__main__':

    print("------ Start BlineBee ------")

    r = record.Record()
    s = stt.SpeechToText()
    t= tts.TextToSpeech()
    cam = camera.BlindBeeCamera()
    
    while(True):
        t.play_audio("What can I help you?")

        print("[1] Detecting")
        print("[2] Saving")

        r.recording("temp_input_audio.linear16")
        respond1 = s.transcribe_audio_to_text("temp_input_audio.linear16")
        respond1 = respond1.split()[0]
        print(len(respond1))
        find = 0
        if(respond1=='detecting'):
            t.play_audio("Please detect QR code.")
            num1, _, _ = cam.recognize_qr()
            f = open('/home/dspi/daAIson/main/qr.csv', 'r', encoding='utf-8')
            rdr = csv.reader(f)
            for line in rdr:
                print('-----Searching index-------')
                print(line)     # ex ['shampoo', '1']
                if(line[0] == num1):
                    name1 = line[1]
                    print('find name: ',name1)
                    # t.play_audio(f"The object is {name1} and saved as QR number {num1}.")
                    t.play_audio(f"The object is {name1}.")
                    find = 1
            f.close()
            
            if(find == 1):
                break
        elif(respond1=='saving'):
            t.play_audio("Please tell me the qr number.")
            r.recording("temp_input_audio.linear16")
            num2 = s.transcribe_audio_to_text("temp_input_audio.linear16")
            num2 = num2.split()[0]
            
            t.play_audio("Please tell me the object name.")
            r.recording("temp_input_audio.linear16")
            name2 = s.transcribe_audio_to_text("temp_input_audio.linear16")
            name2 = name2.split()[0]
            
            f = open('qr.csv', 'a', encoding='utf-8', newline='')
            wr = csv.writer(f)
            wr.writerow([str(num2), str(name2)])
            f.close()
            
            t.play_audio(f"{name2} is saved as QR number {num2}.")
            break
        
        t.play_audio("Please say again.")
