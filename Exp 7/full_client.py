import socket
import sys
import time
x = socket.socket()
#host = input(str("Enter the hostname of the server: "))
host = '127.0.0.1'
port = 8080
x.bind((host,port))
#x.connect((host,port))
print("Connected to chat server...")
while True:
    incoming_msg = x.recv(1024)
    incoming_msg = imcoming_msg.decode()
    print("Server: ",incoming_msg)
    msg = input(str(">>"))
    Msg = msg.encode()
    x.send(Msg)
    print("Message has beem sent...")
