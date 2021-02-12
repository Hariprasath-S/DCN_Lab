import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',9999))
print("Server is waiting...")
data,addr=server.recvfrom(1024)
print(data,addr)
server.sendto(data,addr)
