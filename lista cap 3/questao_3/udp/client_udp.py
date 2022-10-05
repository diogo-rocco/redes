from socket import *
serverName = ''
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Digite a mensagem que deseja enviar\n')
    clientSocket.sendto(message.encode(),(serverName, serverPort))

    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

    print(modifiedMessage.decode())

    while True:
        new_search = input('deseja fazer uma nova busca? (s/n): ')
        if new_search == 's' or new_search == 'n': break
    
    if new_search == 'n': break
    print('\n')

print('encerrando o cliente...')
clientSocket.close()