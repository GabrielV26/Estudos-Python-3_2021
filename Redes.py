import socket

print(socket.getservbyname("domain"))
print(socket.getservbyname("http"))
print(socket.getservbyname("ftp"))

resp = "S"

while(resp == "S"):
    url = input("Digite uma url: ")
    ip = socket.gethostbyname(url)
    print("O IP referente à url informada é: ", ip)
    resp = input("Digite <s> para continuar: ").upper()

from socket import *
servidor = "127.0.0.1"
porta = 43210
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor, porta))
obj_socket.listen(2)
print(obj_socket)
print("Aguardando cliente....")
while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah cliente'
        con.send(msg_enviada)
        break
    con.close()
