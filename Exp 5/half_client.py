import socket
try:
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except:
    print("Connection error")
client_socket.connect(('127.0.0.1',9998))
while True:
    message=input('>> ')
    client_socket.send(str.encode(message))
    data=client_socket.recv(1024).decode()
    print('Server says: ',data)
    if 'bye' in str(data):
        break
