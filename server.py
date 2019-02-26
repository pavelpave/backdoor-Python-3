import socket

host = "192.168.43.22"
port = 9090
s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
s.bind((host,port))
print("start_server  "+ socket.gethostname() +"")
server = (9090,host)
massAddr = []

while True :
    data,addres = s.recvfrom(1024)
    data.decode()

    if not addres in massAddr:
        massAddr.append(addres)
        print("добавлен новый юзер ==>"+ addres[1] +"")
        s.send(bytes('qwe', encoding = 'utf-8'),server)

