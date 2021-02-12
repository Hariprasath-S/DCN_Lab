import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('gct.ac.in',80))
    s.sendall(b"GET / HTTP/1.1\r\nHost: gct.ac.in\r\nAccept: text/html\r\nConnection: close\r\n\r\n")
    
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(data.decode())
