import socket
import time
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('127.0.0.1',10001)
try:
    while True :
        h,t = [1,2]
        message = str(h) + ',' + str(t)
        sent = sock.sendto(message.encode(),server_address)
        time.sleep(1)
finally:
    print("Close socket")
    sock.close()