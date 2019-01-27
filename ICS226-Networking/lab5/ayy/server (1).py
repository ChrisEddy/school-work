# Basic UDP server
# Receives 3 1-byte integers, adds them, and returns the 1-byte result.

# Run: python server.py 12345

import socket
import sys

port = int(sys.argv[1])

# Create the socket object using DGRAM
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the port. Using "" for the interface so it binds to
# all known interfaces, including "localhost".
s.bind(("", port))

# Servers stay open -- they handle a client, then loop back
# to wait for another client.
while True:
    # wait for a client to send a packet
    packet, addr = s.recvfrom(1024)

    # unpack the data. In this case we're just using

    operator = packet[0]
    result = packet[2]
    for x in range(len(packet)):
        if x >= 3:
            if operator == 0:
                result = result - packet[x]
            if operator == 1:
                result = result + packet[x]
            if operator == 2:
                result = result * packet[x]
            if operator == 3:
                result = result / packet[x]

    print('result:', result, 'operator:', operator, 'count:', packet[1])

    # Calculate the result.

    # Pack the result into a 1-element byte array.

    packet = bytearray(1)
    if result >= 0:
        packet[0] = 1
    else:
        packet[0] = 0

    result = abs(int(result))

    if result < 256:
        packet.append(result)
    else:
        while result > 255:
            packet.append(255)
            result = result - 255
        packet.append(result)

    # Send the packet back to the client.
    s.sendto(packet, addr)



