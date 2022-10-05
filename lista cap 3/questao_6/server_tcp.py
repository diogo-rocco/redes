import socket
import select
import sys
import multiprocessing

#define a localizacao do servidor
HOST = ''
PORTA = 12000

input_list = [sys.stdin]
client_list = []

def startServer():
    sock = socket.socket() #default AF_INET e SOCK_STREAM
    sock.bind((HOST, PORTA))
    sock.listen(5)
    sock.setblocking(False)
    input_list.append(sock)
    return sock

def acceptConection(sock):
    client_sock, address = sock.accept()
    return client_sock, address

def endConection(client_sock, address):
    print('encerrando conexao com', address)
    client_sock.close()

def answerRequest(client_sock, address):
    try:

        msg = client_sock.recv(1024).decode()
        if not msg:
            endConection(client_sock, address)
            return
        client_sock.send("Ola! Bem-vindo! Qual o seu nome?".encode())

        name = client_sock.recv(1024).decode()
        if not name:
            endConection(client_sock, address)
            return
        client_sock.send("Certo {name}! Como posso te ajudar?\nDigite o numero que corresponde a opcao desejada:\n1 - Agendar um horario de monitoria\n2 - Listar as proximas atividades da disciplina\n3 - E-mail do professor".format(name=name).encode())

        option = client_sock.recv(1024).decode()
        if not option:
            endConection(client_sock, address)
            return
        if option == '1':
            client_sock.send("Para agendar uma monitoria, basta enviar um e-mail para cainafigueiredo@poli.ufrj.br".encode())
        if option == '2':
            client_sock.send("Fique atento para as datas das proximas atividades. Confira o que vem por ai!\nP1: 26 de maio de 2022\nLista 3: 29 de maio de 2022".encode())
        if option == '3':
            client_sock.send("Quer falar com o professor?\nO e-mail e sadoc@decc.ufrj.br".encode())

        client_sock.send("Obrigado por utilizar nossos servicos!\nAte logo!".encode())
        endConection(client_sock, address)


    except:
        endConection(client_sock, address)
        return

def server():
    sock = startServer()
    print('pronto para receber conexoes...')
    while True:
        #print(input_list)
        read, write, excep = select.select(input_list, [], [])
        for ready in read:
            if ready == sock:
                client_sock, address = acceptConection(sock)
                print('estabelecendo conexao com', address)
                client = multiprocessing.Process(target=answerRequest, args=(client_sock, address))
                client_list.append(client)
                client.start()
            
            elif ready == sys.stdin:
                comand = input()
                if comand == 'fim':
                    for c in client_list:
                        c.join()
                    sock.close
                    return

server()