import socket

host = '127.0.0.1'
port = 10000
message = input(str('Entrez votre message: '))
client_socket = socket.socket()

    
if __name__ == '__main__':
    client_socket.connect((host, port))
    while message != 'bye' or message != 'arret':
        message = input(str('Entrez votre message: '))
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)
    else:
        client_socket.close()




    

    """if __name__ == '__main__':
    if message == 'bye' or message == 'arret':
        client_socket.close()
    else:
        client_socket.connect((host, port))
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)"""
    