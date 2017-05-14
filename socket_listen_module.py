#! /bin/python3

import socket

host = ''
port = 2222
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.bind((host, port))
except socket.error as e :
    print (e)

s.listen(5)
conn, addr = s.accept()

print (conn)
print (type(addr))
print (addr[0])
print (addr[1])
