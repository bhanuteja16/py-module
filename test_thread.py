#! /bin/python3

import threading
from queue import Queue
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 3355))
s.listen(10)

def newconn(conn, addr) :
    #print (addr)
    conn.send('Connected'.encode())
    while True :
        data = conn.recv(512)
        if not data : break
        print (data.decode(), end='')
        conn.send(data)

while True:
    conn, addr = s.accept()
    t = threading.Thread(target=newconn, args=(conn, addr))
    t.daemon = True
    t.start()


