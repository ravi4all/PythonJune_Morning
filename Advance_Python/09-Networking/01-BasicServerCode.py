import socket

# Socket Object
# socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connection Established")

except socket.error as err:
    print("Error",err)

port = 80
hostip = socket.gethostbyname('www.google.com')

try:
    s.connect((hostip, port))
    print("Ping to google successfull")

except socket.gaierror as err:
    print("Failed because",err)



