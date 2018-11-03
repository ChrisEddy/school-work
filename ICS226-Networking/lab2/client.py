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

# parse operator into first byte
if operator == '+':
    operator = 0b00000000 | 0b0000001
if operator == '-':
    operator = 0b00000000 | 0b0000010
if operator == '*':
    operator = 0b00000000 | 0b0000100

numbers = []
numbers.append(operator)  # append operator
numbers.append(len(sys.argv) - 4)  # append count

# Create infinite length arg list of numbers to calculate.
i = 4
for x in range(len(sys.argv) - 4):
    numbers.append(int(sys.argv[i]))
    i = i + 1

print('numbers length: ', len(numbers))

print('Calculating with:', numbers)
print('Operator symbol:', bin(numbers[0]))
print('Integer count:', bin(numbers[1]))
print('First number:', bin(numbers[2]))
print('Second number:', bin(numbers[3]))

# 1. create the socket using DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# py -3 client.py localhost 12345 + 2 2

# 2. build the packet.
packet = bytearray()
packet.append(numbers[0])  # add operator to packet
packet.append(numbers[1])  # add count to packet
i = 2
for x in range(int((len(numbers) - 2) / 2)):
    firstByte = numbers[i] << 8
    i = i + 1
    secondByte = numbers[i] >> 4 | numbers[i] << 4
    i = i + 1
    print('1st byte:', bin(firstByte))
    print('2nd byte:', bin(secondByte))
    fullByte = bin(firstByte | secondByte)[:10]
    print('fullbyte:', int(fullByte, 2), fullByte)
    packet.append(int(fullByte, 2))
print(packet)

# py -3 client.py localhost 12345 + 9 1

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
