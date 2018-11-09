# python client.py localhost 12345 PUT test.txt

# client sending file <filename> (<NNN> bytes)

# !/usr/bin/env python

import socket
import sys
import os
import io

BUFFER_SIZE = 1024
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ACTION = sys.argv[3]
FILE = sys.argv[4]
MESSAGE = ''

FILE_STATS = os.stat(FILE)
FILE_SIZE = FILE_STATS.st_size

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

data = s.recv(BUFFER_SIZE).decode('utf-8')

if data == 'READY':
    if ACTION == 'PUT':
        MESSAGE = 'PUT ' + str(FILE)
        print('client sending file', str(FILE), '(' + str(FILE_SIZE), 'bytes' + ')')
        s.send(MESSAGE.encode('utf8'))  # Send command to server
        data = s.recv(BUFFER_SIZE).decode('utf-8')
        if data == 'OK':
            MESSAGE = FILE_SIZE.to_bytes(FILE_SIZE.bit_length(), byteorder='big', signed=True)  # Create byte count
            s.send(MESSAGE)  # Send byte count to server
            data = s.recv(BUFFER_SIZE).decode('utf-8')  # Wait for an 'OK'
            if data == 'OK':
                print('SENDING FILE BYTES')  # Begin sending File
                f = open(FILE, "rb")
                amountSent = 0
                while amountSent < FILE_SIZE:
                    MESSAGE = f.read(1024)
                    s.send(MESSAGE)
                    print(MESSAGE)
                    amountSent += 1024

    if ACTION == 'GET':
        MESSAGE = 'GET ' + str(FILE)
        s.send(MESSAGE.encode('utf8'))
        print('client receiving file ' + FILE + '(101 bytes)')
        data = s.recv(BUFFER_SIZE).decode('utf-8')
    if ACTION == 'DELETE':
        print('client deleting file ' + FILE)
        MESSAGE = 'DELETE ' + str(FILE)
        s.send(MESSAGE.encode('utf8'))
        data = s.recv(BUFFER_SIZE).decode('utf-8')

s.close()

