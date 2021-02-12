import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
message=input("Enter message: ")
client.sendto(str.encode(message),('127.0.0.1',9999))
data,addr=client.recvfrom(1024)
print(data,addr)
