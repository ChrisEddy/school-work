# Basic UDP Client
# Sends 3 1-byte integers to the server. Receives a 1-byte response
# and prints it (in base-10).

# Run: python client.py localhost 12345 + 40 20

import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])
operator = sys.argv[3]

print('Host:', host, 'Port:', port, 'Operator:', operator)

# parse operator into byte array acceptable format
if operator == '-':
    operator = 0
if operator == '+':
    operator = 1
if operator == '*':
    operator = 2
if operator == '/':
    operator = 3

# Create infinite length arg list of numbers to calculate.
numbers = []
numbers.append(operator)  # append operator
numbers.append(len(sys.argv) - 4)  # append count
i = 4
for x in range(len(sys.argv) - 4):
    numbers.append(sys.argv[i])
    i = i + 1

print('Calculating with:', numbers)
print('Operator symbol:', numbers[0])
print('Integer count:', numbers[1])

# 1. create the socket using DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 2. build the packet.
packet = bytearray(len(numbers))
for x in range(len(numbers)):
    packet[x] = int(numbers[x])

# 3. send the packet.
s.connect((host, port))
s.send(packet)

# 4. receive the response
data = s.recv(1024)
print('Received packet from server...')
print('Length of packet: ', len(data))
for x in range(len(data)):
    print('Packet index #' + str(x), '=', data[x])

# 5. unpack the byte array to a meaningful value.

value = 0

for x in range(len(data)):
    if x >= 1:
        value = value + data[x]

if data[0] == 1:
    print('result:', value)

if data[0] == 0:
    print('result:',  0 - value)
