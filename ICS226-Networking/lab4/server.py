# py -3 server.py 12345 -v
#!/usr/bin/env python

import socket
import sys
import os
import threading
import collections
import time

class Manager(threading.Thread):
    def __init__(self, client, addr, CLIENT_COUNT):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr
        self.CLIENT_COUNT = CLIENT_COUNT
        self.q = collections.deque()
        self.running = set()
        self.q.append(self.client)
        print(self.q)


    def run(self):
        print('manager running')
        print('server connected to client at', str(self.addr[0]) + ':' + str(self.addr[1]))
        while True:
            kick = []
            for t in self.running:
                if not t.is_alive():
                    kick.append(t)
                    print('kicked dead client:', t)
            for t in kick:
                self.running.remove(t)
                print('removed thread:', t)
            if len(self.q) == 0:
                time.sleep(1)
                print('queue empty:', self.q)
                break
            if len(self.q) > 0:
                if len(self.running) < self.CLIENT_COUNT:
                    t = ClientHandler(self.q.pop(), self.addr, self.CLIENT_COUNT)
                    t.start()
                    print('adding:', t)
                    self.running.add(t)
                    time.sleep(1)
                    print('popped new client from queue')


class ClientHandler(threading.Thread):
    def __init__(self, client, addr, CLIENT_COUNT):
        threading.Thread.__init__(self)
        self.client = client
        self.addr = addr
        self.CLIENT_COUNT = CLIENT_COUNT

    def run(self):
        byteCount = 0
        FILE = ''
        print('server waiting on port', TCP_PORT)
        data = 'READY'
        self.client.send(data.encode('utf-8'))  # echo
        data = self.client.recv(BUFFER_SIZE).decode('utf-8')

        if data != '':
            print('server receiving request:', data)

            if data.split(' ', 1)[0] == 'PUT':
                FILE = data.split(' ', 1)[1]
                data = 'OK'
                self.client.send(data.encode('utf-8'))  # Send OK to client, server wants file size in byteCount
                data = self.client.recv(BUFFER_SIZE)  # Wait for byte count from client
                byteCount = int.from_bytes(data, byteorder='big')  # convert byte count to int
                print('server receiving ' + str(byteCount) + ' bytes')
                data = 'OK'
                self.client.send(data.encode('utf-8'))  # Send OK to client, server is ready to receive data
                with open(FILE, 'wb') as file:
                    bytesReceived = 0
                    while bytesReceived < byteCount:
                        data = self.client.recv(BUFFER_SIZE)  # Get a packet of bytes from client
                        file.write(data)  # Write packet to file
                        bytesReceived += 1024
                data = 'DONE'
                self.client.send(data.encode('utf-8'))
                data = ''
                print('PUT finished')

            if data.split(' ', 1)[0] == 'GET':
                FILE = data.split(' ', 1)[1]
                FILE_SIZE = os.stat(FILE).st_size
                data = 'OK'
                self.client.send(data.encode('utf-8'))  # Send OK to client
                print('waiting for READY from client')
                data = self.client.recv(BUFFER_SIZE).decode('utf-8')  # Wait for 'READY' from client
                if data == 'READY':
                    print('got READY from client')
                    MESSAGE = FILE_SIZE.to_bytes(FILE_SIZE.bit_length(), byteorder='big', signed=True)  # Create byte count
                    self.client.send(MESSAGE)  # Send byte count to client
                    data = self.client.recv(BUFFER_SIZE).decode('utf-8')  # Wait for 'OK' from client
                    if data == 'OK':
                        print('server sending ' + str(FILE_SIZE) + ' bytes')
                        sentBytes = 0
                        with open(FILE, 'rb') as file:
                            while sentBytes < FILE_SIZE:
                                MESSAGE = file.read(1024)
                                self.client.send(MESSAGE)
                                sentBytes += 1024
                            file.close()
                        data = 'DONE'
                        self.client.send(data.encode('utf-8'))
                        data = ''

            if data.split(' ', 1)[0] == 'DEL':
                FILE = data.split(' ', 1)[1]
                if os.path.exists(FILE):
                    try:
                        print('server deleting file:', FILE)
                        os.remove(FILE)
                        data = 'DONE'
                        self.client.send(data.encode('utf-8'))  # Send DONE to client, file has been deleted
                    except IOError:
                        data = 'ERROR: unable to delete ' + FILE
                        self.client.send(data.encode('utf-8'))  # Send ERROR to client, file had a issue deleting
                else:
                    data = 'ERROR: ' + FILE + ' does not exist'  # Send ERROR to client, file not existent
                    self.client.send(data.encode('utf-8'))
                data = ''

TCP_IP = '127.0.0.1'
TCP_PORT = int(sys.argv[1])
BUFFER_SIZE = 1024
CLIENT_COUNT = int(sys.argv[2])

print(TCP_IP, TCP_PORT, CLIENT_COUNT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(0)

def startManager():
    while True:
        client, addr = s.accept()
        manager = Manager(client, addr, CLIENT_COUNT)
        manager.start()

startManager()

