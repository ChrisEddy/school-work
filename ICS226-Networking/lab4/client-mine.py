# py -3 client.py localhost 12345 PUT EMMA.txt
# py -3 client.py localhost 12345 GET CHRIS.txt
# py -3 client.py localhost 12345 DELETE ayyy.txt


# client sending file <filename> (<NNN> bytes)

# !/usr/bin/env python

import socket
import sys
import os

BUFFER_SIZE = 1024
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ACTION = sys.argv[3]
FILE = sys.argv[4]
MESSAGE = ''

try:
    print(FILE)
    FILE_SIZE = os.path.getsize(FILE)
    print('filesize:', FILE_SIZE)
except IOError:
    FILE_SIZE = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = s.recv(BUFFER_SIZE).decode('utf-8')

if data == 'READY':

    if ACTION == 'PUT':
        MESSAGE = 'PUT ' + str(FILE)
        print('client sending file', str(FILE), '(' + str(FILE_SIZE), 'bytes)')
        s.send(MESSAGE.encode('utf8'))  # Send command to server
        data = s.recv(BUFFER_SIZE).decode('utf-8')
        if data == 'OK':
            MESSAGE = FILE_SIZE.to_bytes(FILE_SIZE.bit_length(), byteorder='big', signed=True)  # Create byte count
            s.send(MESSAGE)  # Send byte count to server
            data = s.recv(BUFFER_SIZE).decode('utf-8')  # Wait for an 'OK'
            if data == 'OK':
                f = open(FILE, "rb")  # open file for bytes streaming to server
                amountSent = 0
                while amountSent < FILE_SIZE:
                    MESSAGE = f.read(1024)
                    s.send(MESSAGE)
                    amountSent += 1024
                data = s.recv(BUFFER_SIZE).decode('utf-8')  # Wait for 'DONE'
                if data == 'DONE':
                    print('Complete')

    if ACTION == 'GET':
        MESSAGE = 'GET ' + str(FILE)
        s.send(MESSAGE.encode('utf8'))  # Send command
        data = s.recv(BUFFER_SIZE).decode('utf-8')  # Wait for 'OK' from server
        if data == 'OK':
            MESSAGE = 'READY'
            s.send(MESSAGE.encode('utf8'))  # Send READY to server
            data = s.recv(BUFFER_SIZE)  # Wait for byteCount of fileSize from server
            byteCount = int.from_bytes(data, byteorder='big')  # convert to byte count to int
            MESSAGE = 'OK'
            s.send(MESSAGE.encode('utf8'))  # Send OK to server
            amountReceived = 0
            print('client receiving file ' + FILE + ' (' + str(byteCount) + ' bytes)')
            with open(FILE, 'wb') as file:
                while amountReceived < byteCount:
                    data = s.recv(BUFFER_SIZE)  # Receive file packets from server
                    if b'DONE' in data:
                        data = data[:-4]
                        file.write(data)
                        amountReceived += 1024
                    else:
                        file.write(data)
                        amountReceived += 1024
                file.close()
                print('Complete')

    if ACTION == 'DEL':
        print('client deleting file ' + FILE)
        MESSAGE = 'DEL ' + str(FILE)
        s.send(MESSAGE.encode('utf8'))
        data = s.recv(BUFFER_SIZE).decode('utf-8')
        if data == 'DONE':
            print('Complete')
        else:
            print(data)  # Print the ERROR response from server

s.close()

