import socket
from time import ctime
import threading
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
ipport = (host, 6071)
buff = 1024
server.bind(ipport)
server.listen(5)
print("Waiting for connection...")
client,addr = server.accept()
print("Connection made...with ",host)

def recieve():
    while True:
        msg = client.recv(buff)
        
        if not msg:
            print("Ending connection")
            break
        print(msg.decode())

def send():
    while True:
        smsg = input(">>>")
        if not smsg:
            break
        client.send(str.encode(smsg))

t1 = threading.Thread(target = send(), name=3)
t2 = threading.Thread(target = recieve(), name=4)
