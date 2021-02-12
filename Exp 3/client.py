import socket

ip = "192.198.10.14"
port = 9999
msg = "I am the client"


tosend = str.encode(msg)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(tosend, (ip, port))