import socket 
import time
import binascii
import socket
import struct
import sys
from blindbee import BlindBeeCamera

HOST = '192.168.137.165' # 보내는 호스트 IP
PORT = 22


# cnt = 0
# sens = 2.1
# packer = struct.Struct('If')
# values = (1, 2.7)

if __name__ == "__main__":
    #run_quickstart()
    # $ export GOOGLE_APPLICATION_CREDENTIALS="/home/dspi/storage/dauntless-graph-393517-4fc404d248f0.json"

    cam = BlindBeeCamera()
    data, box, straight_qrcode = cam.recognize_qr()


    while True: 
        #cnt = data
        #sens = 2.1
        #packer = struct()
        values = (data, straight_qrcode)       
        #values = (cnt, sens)
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        client_socket.connect((HOST, PORT)) 
        #packed_data = packer.pack(*values)
        #print('sending "%s"' % binascii.hexlify(data), values)
        print('sending %s' %data)


        #client_socket.sendall(packed_data)
        client_socket.send(values)


        time.sleep(2)

        client_socket.close()