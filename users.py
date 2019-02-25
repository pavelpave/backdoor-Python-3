import socket
import os

host = "192.168.43.22"
port = 9090
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.bind((host,port))
print("start_server")
