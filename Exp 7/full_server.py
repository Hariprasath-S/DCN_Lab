import socket
import sys
import time
x = socket.socket()
host = socket.gethostname()
port = 8080
#x.connect((host,port))
print("server done binding...")
print("server is waiting...")
x.bind((host,port))
x.listen(1)

connection,address = x.accept()
print(connection,address," Has connected to the server and is now online")
while True:
    display_msg = input(str(">>"))
    display_msg = display_msg.encode()
    connection.send(display_msg)
    print("Message has been sent...")
    in_msg = connection.recv(1024)
    in_msg = in_msg.decode()
    print("Client: ",in_msg)
