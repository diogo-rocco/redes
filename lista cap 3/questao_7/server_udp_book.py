from socket import *

serverPort = 12000
HOST = ''

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((HOST, serverPort))
print("The server is ready to receive")
while True:
 message, clientAddress = serverSocket.recvfrom(2048)
 print("mensagem recebida de", clientAddress)
 modifiedMessage = message.decode().upper()
 serverSocket.sendto(modifiedMessage.encode(), clientAddress)