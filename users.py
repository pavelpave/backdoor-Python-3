import socket
import os
import urllib.request

external_ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')

print(external_ip)

host = external_ip
port = 9090
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
# s.bind((host,port))
print('start')
while True:
    s.connect((host,port))
    data = s.recvfrom(1024)
    print(data)
