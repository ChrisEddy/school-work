#!/usr/bin/python

import sys
import socket
from urllib.parse import urlparse
import html2text

response = ''

URL = sys.argv[1]  # accept the URL arg from user

o = urlparse(URL)  # parse URL into objects
host = o.netloc
print('host: ', host)
resource = o.path
print('resource: ', resource)
if resource == '':
    print('No path given, defaulting to /')
    resource = '/'

request = 'GET ' + resource + ' HTTP/1.1\r\nHost: ' + host + '\r\n\r\n'  # create string with data
request = request.encode('utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # start socket
s.connect((host, 80))
s.sendall(request)  # send the request

trigger = True
while trigger:
    response += s.recv(1024).decode('latin-1')  # print the response
    if '\r\n0\r\n\r\n' in response:
        print('Raw HTTP Response: ', response)
        print('Response Complete :)')
        s.close()  # close socket
        trigger = False

print(html2text.html2text(response))

