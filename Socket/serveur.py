import socket

host = '127.0.0.1'
port = 10000
reply = 'got it'
data = ''
bye = 'bye'
arret = 'arret'
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)



if __name__ == '__main__':
    while data != arret and reply != arret:
        client_socket, address = server_socket.accept()
        data = reply = ''
        print('Connexion établie avec: ', str(address))
        while data != bye and reply != bye and data != arret and reply != arret:
            data = client_socket.recv(1024).decode()
            print(data)
            reply = input('Entrez votre réponse: ')
            client_socket.send(reply.encode())
        client_socket.close()
    server_socket.close()


