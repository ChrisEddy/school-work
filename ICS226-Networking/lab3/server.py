# py -3 server.py 12345 -v

#!/usr/bin/env python

import socket
import sys
import os

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
            conn.send(data.encode('utf-8'))  # Send OK to client, server wants file size in byteCount
            data = conn.recv(BUFFER_SIZE)  # Wait for byte count from client
            byteCount = int.from_bytes(data, byteorder='big')  # convert byte count to int
            print('server receiving ' + str(byteCount) + ' bytes')
            data = 'OK'
            conn.send(data.encode('utf-8'))  # Send OK to client, server is ready to receive data
            with open(FILE, 'wb') as file:
                bytesReceived = 0
                while bytesReceived < byteCount:
                    data = conn.recv(BUFFER_SIZE)  # Get a packet of bytes from client
                    file.write(data)  # Write packet to file
                    bytesReceived += 1024
            data = 'DONE'
            conn.send(data.encode('utf-8'))
            data = ''

        if data.split(' ', 1)[0] == 'GET':
            FILE = data.split(' ', 1)[1]
            FILE_STATS = os.stat(FILE)
            FILE_SIZE = FILE_STATS.st_size
            data = 'OK'
            conn.send(data.encode('utf-8'))  # Send OK to client
            print('waiting for READY from client')
            data = conn.recv(BUFFER_SIZE).decode('utf-8')  # Wait for 'READY' from client
            if data == 'READY':
                print('got READY from client')
                MESSAGE = FILE_SIZE.to_bytes(FILE_SIZE.bit_length(), byteorder='big', signed=True)  # Create byte count
                conn.send(MESSAGE)  # Send byte count to client
                data = conn.recv(BUFFER_SIZE).decode('utf-8')  # Wait for 'OK' from client
                if data == 'OK':
                    print('server sending ' + str(FILE_SIZE) + ' bytes')
                    sentBytes = 0
                    with open(FILE, 'rb') as file:
                        while sentBytes < FILE_SIZE:
                            MESSAGE = file.read(1024)
                            conn.send(MESSAGE)
                            sentBytes += 1024
                        file.close()
                    data = 'DONE'
                    conn.send(data.encode('utf-8'))
                    data = ''

        if data.split(' ', 1)[0] == 'DEL':
            FILE = data.split(' ', 1)[1]
            if os.path.exists(FILE):
                try:
                    print('server deleting file:', FILE)
                    os.remove(FILE)
                    data = 'DONE'
                    conn.send(data.encode('utf-8'))  # Send DONE to client, file has been deleted
                except IOError:
                    data = 'ERROR: unable to delete ' + FILE
                    conn.send(data.encode('utf-8'))  # Send ERROR to client, file had a issue deleting
            else:
                data = 'ERROR: ' + FILE + ' does not exist'  # Send ERROR to client, file not existent
                conn.send(data.encode('utf-8'))
            data = ''
