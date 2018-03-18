#!/usr/bin/python

import socket

target_host = "127.0.0.1"
target_port = 5555

# create socket object 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect client

client.connect((target_host, target_port))

# send data

client.send("GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n")

# get data

response = client.recv(4096)

print response
