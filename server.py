import socket
import sys
import time
from datetime import datetime

port = 60000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#host = socket.gethostname()
s.bind(("0.0.0.0", port))
print('Server Initiated!\nListening...')
filename = sys.argv[1]
while True:
    data, addr = s.recvfrom(1024)
    print('Got connection from', addr, datetime.now())
    print("Message from Client: ", data.decode())
    f = open(filename, 'rb')
    data = f.read()

    print(len(data))
    for x in range(0, len(data), 1024):
        r = s.sendto(data[x:min(x+1024, len(data))], addr)
        #print(r)


    f.close()
    print('File Sent!', datetime.now())
