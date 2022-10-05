from socket import *

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
        message = connectionSocket.recv(1024).decode()
        if not message: #sai do loop quando o cliente para de enviar mensagens
            break
        modifiedMessage = message.upper()
        connectionSocket.send(modifiedMessage.encode())

    connectionSocket.close()
    print("closing connection...")