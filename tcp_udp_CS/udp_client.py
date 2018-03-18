#!/usr/bin/python

import socket

target_host = "127.0.0.1"
target_port = 5556

# create socket object

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data

client.sendto("AABBCC",(target_host, target_port))

# get data

data, addr = client.recvfrom(4096)

print data
print addr
