from socket import *
from pickle import dumps

serverName = ''
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    user = input('Digite o nome de usuario\n')
    password = input('Digite a senha\n')

    msg = {'user': user, 'password': password}
    msg_encoded = dumps(msg)

    clientSocket.send(msg_encoded)

    response = clientSocket.recv(1024)

    print(response.decode())

    while True:
        new_search = input('deseja fazer um novo login? (s/n): ')
        if new_search == 's' or new_search == 'n': break
    
    if new_search == 'n': break
    print('\n')

print('encerrando o cliente...')
clientSocket.close()