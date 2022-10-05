from socket import *
serverName = ''
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

number = ""

while not number.isnumeric():
    number = input('Digite um numero para enviar\n')

for message in range(int(number)):
    print("enviando", message)
    clientSocket.send(str(message).encode())

print('encerrando o cliente...')
clientSocket.close()