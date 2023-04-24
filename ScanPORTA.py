import sys
import socket
# ou comando no CMD python 'nome do arquivo' IP
ipAddress = sys.argv[1]

for ports in range(1, 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s. connect_ex((ipAddress, ports)) == 0:
        print(f'Porta {ports} Aberta')
        s.close()
