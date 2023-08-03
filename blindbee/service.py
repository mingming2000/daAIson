import csv
import logging
import multiprocessing as mp
import serial
import time

from blindbee import tts
from blindbee import stt
from blindbee import record
from text_color import TextColor
from state import State



# def running_service(queue):

#     While(True):

#     print("------ Start BlineBee ------")

#     r = record.Record()
#     s = stt.SpeechToText()
#     t= tts.TextToSpeech()
#     # cam = camera.BlindBeeCamera()
    
#     while(True):
#         t.play_audio("What can I help you?")

#         print("[1] Detecting")
#         print("[2] Saving")

#         r.recording("temp_input_audio.linear16")
#         respond1 = s.transcribe_audio_to_text("temp_input_audio.linear16")
#         respond1 = respond1.split()[0]
#         print(len(respond1))
#         find = 0
#         if(respond1=='detecting'):
#             t.play_audio("Please detect QR code.")
#             #while(1):
#             #    if len(glist) == num_list:
#             #        break
#             #print(glist)
#             num1 = queue.get()
#             # num1, _, _ = cam.recognize_qr()
#             f = open('/home/dspi/daAIson/main/qr.csv', 'r', encoding='utf-8')
#             rdr = csv.reader(f)
#             for line in rdr:
#                 print('-----Searching index-------')
#                 print(line)     # ex ['shampoo', '1']
#                 if(line[0] == num1):
#                     name1 = line[1]
#                     print('find name: ',name1)
#                     # t.play_audio(f"The object is {name1} and saved as QR number {num1}.")
#                     t.play_audio(f"The object is {name1}.")
#                     find = 1
#             f.close()
            
#             if(find == 1):
#                 break
#         elif(respond1=='saving'):
#             t.play_audio("Please tell me the qr number.")
#             r.recording("temp_input_audio.linear16")
#             num2 = s.transcribe_audio_to_text("temp_input_audio.linear16")
#             num2 = num2.split()[0]
            
#             t.play_audio("Please tell me the object name.")
#             r.recording("temp_input_audio.linear16")
#             name2 = s.transcribe_audio_to_text("temp_input_audio.linear16")
#             name2 = name2.split()[0]
            
#             f = open('qr.csv', 'a', encoding='utf-8', newline='')
#             wr = csv.writer(f)
#             wr.writerow([str(num2), str(name2)])
#             f.close()
            
#             t.play_audio(f"{name2} is saved as QR number {num2}.")
#             break
        
#         t.play_audio("Please say again.")
#         # glist.append(1)

State = {
    "READY": 0,
    "WAIT": 1,
    "DETECT": 2,
    "SAVE": 3,
}


def detecting(t, to_service_queue, to_flask_queue, debug: bool = True) -> int:
    t.play_audio("Please detect QR code.")

    num1 = to_service_queue.get()
    logging.info(TextColor.yellow_bright(f"[Service] Got a data > {num1}"))

    f = open('/home/dspi/daAIson/main/qr.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        logging.info(TextColor.yellow_bright('-----Searching index-------'))
        logging.info(TextColor.yellow_bright(f"{line}"))     # ex ['shampoo', '1']
        if(line[0] == num1):
            name1 = line[1]
            logging.info(TextColor.yellow_bright(f'find name: {name1}'))
            t.play_audio(f"The object is {name1}.")
            find = 1
            break
    f.close()
    to_flask_queue.put("done")
    return find


def saving(t, r, s, debug: bool = True):
    t.play_audio("Please tell me the qr number.")

    if not debug:
        r.recording("temp_input_audio.linear16")
        num2 = s.transcribe_audio_to_text("temp_input_audio.linear16")
        num2 = num2.split()[0]
    else:
        num2 = 'one'    # for debugging

    t.play_audio("Please tell me the object name.")

    if not debug:
        r.recording("temp_input_audio.linear16")
        name2 = s.transcribe_audio_to_text("temp_input_audio.linear16")
        name2 = name2.split()[0]
    else:
        name2 = 'shampoo' # for debugging

    f = open('qr.csv', 'a', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow([str(num2), str(name2)])
    f.close()
    
    t.play_audio("Braille will be printed.")
    
    num = '1'
    ser = serial.Serial('/dev/ttyUSB2', 9600)

    start_time = time.time()

    while True:

        ser.write(num.encode())
        time.sleep(3)
        current_time = time.time()

        if current_time - start_time > 25:
            break
    
    return name2, num2


def running_service(to_service_queue: mp.Queue, to_flask_queue: mp.Queue, cur_state: State):
    debug: bool = True
    respond1 = 'detecting'
    r = record.Record()
    s = stt.SpeechToText()
    t= tts.TextToSpeech()
    start = 1

    t.play_audio("Standby. Call if needed.")
    logging.info(TextColor.yellow_bright("------ Standby. Call if needed. ------"))

    while(True):
        if(start == 1):
            logging.info(TextColor.yellow_bright(f"------ Start BlineBee ------"))
            while(True):
                logging.info(TextColor.yellow_bright(f"S:{cur_state}"))
                if cur_state.is_ready:
                    t.play_audio("What can I help you?")
                    logging.info(TextColor.yellow_bright("Select [1] >> Detecting"))
                    logging.info(TextColor.yellow_bright("Select [2] >> Saving"))
                    cur_state.wait

                if not debug:
                    r.recording("temp_input_audio.linear16")
                    respond1 = s.transcribe_audio_to_text("temp_input_audio.linear16")
                    logging.info(TextColor.yellow_bright(f"Finish to record via microphone!"))
                    if respond1 == None:
                        t.play_audio("Please say again.")
                        continue
                    respond1 = respond1.split()[0]

                find = 0
                if(respond1=='detecting'):
                    logging.info("Detecting mode")
                    cur_state.detecting
                    find = detecting(t, to_service_queue, to_flask_queue)
                    if(find == 1):
                        cur_state.ready
                        break
                elif(respond1=='saving'):
                    logging.info("Saving mode")
                    cur_state.saving
                    name2, num2 = saving(t, r, s)
                    t.play_audio(f"{name2} is saved as QR number {num2}.")
                    cur_state.ready
                    break
                t.play_audio("Please say again.")

