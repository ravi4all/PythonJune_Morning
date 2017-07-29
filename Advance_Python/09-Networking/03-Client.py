import socket

s = socket.socket()

port = 9999

s.connect(('127.0.0.1', port))

# limit 1024 bytes...
data = s.recv(1024)
print(data)

s.close()