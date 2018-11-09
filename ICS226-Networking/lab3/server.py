# python server.py 12345 -v

#!/usr/bin/env python

import socket
import sys

TCP_IP = '127.0.0.1'
TCP_PORT = int(sys.argv[1])
BUFFER_SIZE = 1024
VERBOSE = False

if len(sys.argv) > 2:
    if sys.argv[2] == '-v':
        VERBOSE = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(0)

while True:
    byteCount = 0
    FILE = ''
    print('server waiting on port', TCP_PORT)
    conn, addr = s.accept()
    print('server connected to client at', str(addr[0]) + ':' + str(addr[1]))
    data = 'READY'
    conn.send(data.encode('utf-8'))  # echo
    data = conn.recv(BUFFER_SIZE).decode('utf-8')
    if data != '':
        print('server receiving request:', data)
        if data.split(' ', 1)[0] == 'PUT':
            FILE = data.split(' ', 1)[1]
            data = 'OK'
            conn.send(data.encode('utf-8'))  # Send OK to client
            data = conn.recv(BUFFER_SIZE)  # Wait for byte count from client
            byteCount = int.from_bytes(data, byteorder='big')  # convert to byte count to int
            print('server receiving ' + str(byteCount) + ' bytes')
            data = 'OK'
            conn.send(data.encode('utf-8'))  # Send OK to client
            with open('server.txt', 'wb') as file:
                bytesReceived = 0
                while bytesReceived < byteCount:
                    data = conn.recv(BUFFER_SIZE)  # Get a packet of bytes from client
                    file.write(data)  # Write packet to file
                    bytesReceived += 1024
            data = ''
        if data.split(' ', 1)[0] == 'GET':
            print('server sending <NNN> byte')
            data = ''
        if data.split(' ', 1)[0] == 'DELETE':
            print('server deleting file <filename>')
            data = ''
