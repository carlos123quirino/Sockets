import socket
host = '127.0.0.1'
port = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1' ,port))
data = sock.recv(4096)
sock.close()

print(data.decode())




