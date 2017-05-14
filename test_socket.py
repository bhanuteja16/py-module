#! /bin/python3

import socket 

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print (s)

#s.connect(('www.purple.com', 80))
s.bind(('127.0.0.1', 3355))
s.listen(1)
conn, addr = s.accept()
print (conn)
print (addr)

while True :
    data = conn.recv(4)
    print (data.decode(), end='')
    if not data: break
    conn.send(data)

s.close()
