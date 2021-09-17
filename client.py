import socket
import sys
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = sys.argv[1]
file_size = int(sys.argv[2])
port = 60000

msg_to_server = b"Hello Server!"
s.sendto(msg_to_server, (host, port))

with open('File_Received.txt', 'wb') as f:
    print('File Opened!')
    print('Receiving data...')
    data = b""
    tdata = b""
    while(len(data)<(file_size)):
        tdata, addr = s.recvfrom(file_size-len(data))
        data += tdata
        print(len(tdata), len(data), datetime.now())
    f.write(data)

# we will never reach here, it looks like udp looses data   
f.close()
print('File Successfully Received!')
s.close()
print('Connection Closed!')
