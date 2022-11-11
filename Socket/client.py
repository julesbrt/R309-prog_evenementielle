import socket
import time

host = '192.168.43.229'
port = 10000
message = 'hello'
time.sleep(3)
client_socket = socket.socket()
client_socket.connect((host, port))
client_socket.send("arret".encode())
time.sleep(2)
client_socket.send("arret".encode())
data = client_socket.recv(1024).decode()
print(data)
client_socket.close()
