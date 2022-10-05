from socket import *
from pickle import loads

serverPort = 12000
HOST = ''

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("starting connection...")

    while True:
        message = connectionSocket.recv(1024)
        if not message: #sai do loop quando o cliente para de enviar mensagens
            break
        
        message = loads(message)
        if(message['user'] == 'admin' and message['password'] == 'admin'):
            connectionSocket.send("Login efetuado com sucesso".encode())
        else:
            connectionSocket.send("Falha ao efetuar o login".encode())
        

    connectionSocket.close()
    print("closing connection...")