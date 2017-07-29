import socket

s = socket.socket()

port = 9999

s.bind(('', port))
print("Socket bind at",port)
s.listen(5)

print("Waiting for connections...")

message = "Hello User..."
# print(message.encode('utf-8'))
client, addr = s.accept()
print("Connection established with", addr)
def main():

    while True:

        data = client.recv(1024).decode()
        print("From User",data)

        client.send(data.encode())

    client.close()

main()