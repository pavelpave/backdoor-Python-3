import socket
import os
import urllib.request
import subprocess

external_ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')

print(external_ip)

host = external_ip
port = 9090

server = ("212.26.236.115",9090)
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
# s.bind((host,port))
print('start')
try:
    while True:

        s.connect(server)
        data,addres = s.recvfrom(1024)
        udata = data.decode("utf-8")
        print(data)
        s.send(b"hi")

except:
    raise("out")
