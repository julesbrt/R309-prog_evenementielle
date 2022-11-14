import socket

host = '127.0.0.1'
port = 10000
message = 'hello'

client_socket = socket.socket()
client_socket.connect((host, port))
client_socket.send(message.encode())
data = client_socket.recv(1024).decode()
print(data)
client_socket.close()
