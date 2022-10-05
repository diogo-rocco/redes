import socket
import select
import sys
import multiprocessing

#define a localizacao do servidor
HOST = ''
PORTA = 12000

input_list = [sys.stdin]

def startServer():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #default AF_INET e SOCK_STREAM
    sock.bind((HOST, PORTA))
    input_list.append(sock)
    print('server started')
    return sock

def answerRequest(client_sock):
    message, clientAddress = client_sock.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    client_sock.sendto(modifiedMessage.encode(), clientAddress)

def server():
    sock = startServer()
    while True:
        #print(input_list)
        read, write, excep = select.select(input_list, [], [])
        for ready in read:
            if ready == sock:
                print('message recieved')
                client = multiprocessing.Process(target=answerRequest, args=((sock,)))
                client.start()
            
            elif ready == sys.stdin:
                comand = input()
                if comand == 'fim':
                    sock.close
                    return

server()