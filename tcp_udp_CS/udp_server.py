#!/usr/bin/python

import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 5556

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((bind_ip, bind_port))

while True:
    data, addr = server.recvfrom(4096)
    print "received message:",data
    server.sendto("hello",addr)
