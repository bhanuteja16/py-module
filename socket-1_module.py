#! /bin/python3

import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print (s)

server = 'www.chiark.greenend.org.uk'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET /~sgtatham/putty/latest.html HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server,port))
s.send(request.encode())
result = s.recv(512)

while len(result) > 0 :
    print (result)
    result = s.recv(512)
    #time.sleep(1)
