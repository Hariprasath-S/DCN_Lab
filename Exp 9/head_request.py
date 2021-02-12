import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('gct.ac.in',80))
    s.sendall(b"HEAD / HTTP/1.1\r\nHost: gct.ac.in\r\nAccept: text/html\r\n\r\n")
    print(str(s.recv(1024),'utf-8'))
