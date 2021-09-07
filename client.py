import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 60000
msg_to_server = "Hello Server!"
s.sendto(msg_to_server.encode("utf-8"), (host, port))

with open('File_Received.txt', 'a') as f:
    print('File Opened!')
    print('Receiving data...')
    data, addr = s.recvfrom(1024)
    file_data = data.decode()
    f.write(file_data)

f.close()
print('File Successfully Received!')
s.close()
print('Connection Closed!')