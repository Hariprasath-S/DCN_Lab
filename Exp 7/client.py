import socket
from time import ctime
import threading
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
ipport = (host, 6071)
buff = 1024

client.connect(ipport)
print("Connected...")

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

t1 = threading.Thread(target = send(), name=1)
t2 = threading.Thread(target = recieve(), name=2)
