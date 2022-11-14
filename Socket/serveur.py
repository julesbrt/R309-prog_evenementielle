import socket

host = '127.0.0.1'
port = 10000
reply = 'got it'

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
conn, address = server_socket.accept()
data = conn.recv(1024).decode()
print(data)
conn.send(reply.encode())
conn.close()