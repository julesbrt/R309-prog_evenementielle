import socket

host = '127.0.0.1'
port = 8081
reply = 'got it'
data = ''
bye = 'bye'
arret = 'arret'



if __name__ == '__main__':
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    while data != arret and reply != arret:
        conn, address = server_socket.accept()
        data = reply = ''
        print('Connexion établie avec: ', str(address))
        while data != bye and reply != bye and data != arret and reply != arret:
            data = conn.recv(1024).decode()
            print(data)
            reply = input('Entrez votre réponse: ')
            conn.send(reply.encode())
        conn.close()
    server_socket.close()