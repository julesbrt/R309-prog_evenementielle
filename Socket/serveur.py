import socket

host = '127.0.0.1'
port = 10000
reply = 'got it'
server_socket = socket.socket()


if __name__ == '__main__':
    server_socket.bind((host, port))
    while reply != 'bye' or reply != 'arret':
        server_socket.listen(1)
        print("En attente d'un message...")
        conn, address = server_socket.accept()
        data = conn.recv(1024).decode()
        print(data)
        conn.send(reply.encode())

    else:
        server_socket.close()




    """if reply == 'bye' or reply == 'arret':
        server_socket.close()
    else:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print("En attente d'un message...")
        conn, address = server_socket.accept()
        data = conn.recv(1024).decode()
        print(data)
        conn.send(reply.encode())"""