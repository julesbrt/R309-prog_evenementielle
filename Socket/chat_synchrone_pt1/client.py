import socket
import threading

host = '127.0.0.1'
port = 8081
message = ''
client_socket = socket.socket()
bye = 'bye'
arret = 'arret'
data = ''
client_socket.connect((host, port))

def reception(client_socket):
    data = ''
    while message != bye and data != bye and message != arret and data != arret:
        message = input(str('Entrez votre message: '))
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)
    data = '?????'
    print(data)

if __name__ == '__main__':
    t1 = threading.Thread(target=reception, args=(client_socket,))
    t1.start()
    t1.join()

    print('Fermeture du client')
    client_socket.close()
