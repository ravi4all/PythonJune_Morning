import socket
import sys

s = socket.socket()

port = 9999

s.bind(('', port))
print("Socket bind at",port)
s.listen(5)

print("Waiting for connections...")

message = "Thankyou for connecting with us..."
# print(message.encode('utf-8'))
while True:
    client, addr = s.accept()
    print("Connection established with", addr)

    client.send(message.encode('utf-8'))

    client.close()