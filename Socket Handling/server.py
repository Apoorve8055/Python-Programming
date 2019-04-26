import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('127.0.0.1',10001)
sock.bind(server_address)

with open('DataLog.txt','w') as f:
    while True:
        data,address = sock.recvfrom(4096)
        mess = str(data)
        f.write(mess)
        print(mess)
f.close()