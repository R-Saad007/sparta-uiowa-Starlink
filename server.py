import socket
import sys
port = 60000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
s.bind((host, port))
print('Server Initiated!\nListening...')
filename = sys.argv[1]
while True:
    data, addr = s.recvfrom(1024)
    print('Got connection from', addr)
    print("Message from Client: ", data.decode())
    f = open(filename, 'rb')
    info = f.read(1024)
    while info:
        s.sendto(info, addr)
        info = f.read(1024)

    f.close()
    print('File Sent!')
    print("===========================")