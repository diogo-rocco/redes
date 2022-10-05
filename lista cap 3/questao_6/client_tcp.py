from socket import *
import select
import sys

serverName = ''
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Digite a mensagem que deseja enviar")
fim = False
while True:
    read, write, excep = select.select([clientSocket, sys.stdin], [], [])
    for ready in read:
        if ready == clientSocket:
            response = clientSocket.recv(1024).decode()
            print(response)
            if response == "Obrigado por utilizar nossos servicos!\nAte logo!":
                fim = True
                break
        elif ready == sys.stdin:
            message = input()
            print("\n")
            clientSocket.send(message.encode())
    
    if fim:
        break



print('encerrando o cliente...')
clientSocket.close()