import socket
try:
    server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Server is ready...')
except:
    print("Connection error")
server_socket.bind(('127.0.0.1',9998))
server_socket.listen(1)
client,addr=server_socket.accept()
while True:
    data=client.recv(1024).decode()
    print('Client says: ',data)
    message=input('>> ')
    client.send(str.encode(message))
    if 'bye' in str(message):
        break
client.close()
