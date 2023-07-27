import socket 
import time
import binascii
import socket
import struct
import sys

HOST = '192.168.137.165' # 보내는 호스트 IP
PORT = 9999

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
client_socket.connect((HOST, PORT)) 

cnt = 0
sens = 2.1
packer = struct.Struct('If')
values = (1, 2.7)

while True: 
    cnt = cnt +1
    sens = sens + 0.1
    values = (cnt, sens)
    packed_data = packer.pack(*values)
    print('sending "%s"' % binascii.hexlify(packed_data), values)

    client_socket.sendall(packed_data)


    time.sleep(2)

    client_socket.close()