import socket

SERVER_IP = '192.168.137.165'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("Connected to Server")

    while True:
        message = "Hello, Server!"
        client_socket.sendall(message.encode('utf-8'))

        data = client_socket.recv(1024)
        if not data:
            break

        print(f"Data received: {data.decode('utf-8')}")

except Exception as e:
    print(f"ERR: {e}")

# 연결 종료
client_socket.close()
