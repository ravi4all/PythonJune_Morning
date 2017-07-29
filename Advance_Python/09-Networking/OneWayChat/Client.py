import socket

s = socket.socket()

port = 9999
s.connect(('127.0.0.1', port))

def main():

    while True:

        message = input("Your message:")
        s.send(message.encode())
        data = s.recv(1024).decode()
        print(data)

    s.close()

main()