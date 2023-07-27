import binascii
import socket
import struct
import sys
from _thread import *

# 접속한 클라이언트와 통신을 위해, 새로운 쓰레드가 생성 
def threaded(client_socket, addr): 
    #print('Connected by :', addr[0], ':', addr[1]) 

    while True: # 클라이언트가 접속을 끊을 때 까지 반복 
        try:
            unpacker = struct.Struct('I f')
            data = client_socket.recv(unpacker.size)   # 데이터가 수신되면
            if not data: 
                print('Disconnected by ' + addr[0],':',addr[1])
                break

            print('received "%s"' % binascii.hexlify(data))
            unpacked_data = unpacker.unpack(data)
            print('Sens. Data:', unpacked_data)

        except ConnectionResetError as e:
            print('Disconnected by ' + addr[0],':',addr[1])
            break
             
    client_socket.close() 


HOST = '0.0.0.0'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT)) 
server_socket.listen() 

print('server start')


while True: 
    #print('wait')
    client_socket, addr = server_socket.accept()   # 클라이언트가 접속하면
    print('Connected by :', addr[0], ':', addr[1])
    start_new_thread(threaded, (client_socket, addr)) 

server_socket.close()
