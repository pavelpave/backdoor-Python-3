import socket
import urllib.request

host = urllib.request.urlopen('http://ident.me').read().decode("utf-8")
#host = "192.168.43.22"
#212.26.236.115

print(host)
port = 9090
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.bind(("127.0.0.1",9090))
print("start_server  "+ socket.gethostname() +"")
server = (host,9090)
massAddr = []

while True :
    data,addres = s.recvfrom(1024)
    data.decode("utf-8")
    print(data)

    if not addres in massAddr:
        massAddr.append(addres)
        print("добавлен новый юзер ==>"+ addres[1] +"")
        s.send(bytes('qwe', encoding = 'utf-8'),server)

