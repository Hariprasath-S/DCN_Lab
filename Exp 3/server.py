import socket

ip = "localhost"
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("localhost", 9999))

print("Server is waiting...")

while True:
    data, addr = server.recvfrom(1024)
    print("Connected with: ", addr)
    print("Message : ", data)