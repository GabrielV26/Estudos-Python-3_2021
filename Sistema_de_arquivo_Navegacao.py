"""
Sistemas de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso
do módulos os.

os -> Operating System - Sistema Operacional

"""

# Fazer o import

import os
import platform


# getcwd() -> pega o current wor directory - diretório de trabalho corrente

print(os.getcwd())

# Para mudar o diretório, podemos utilizar o chdir('..')

os.chdir('..')

print(os.getcwd())

# Podemos checar se um diretório é ABsoluto ou RElarivo
# USE O PREFIXO R antes do CAMINHO OU DUAS BARRAS C:\\Users\\Gabriel o Genio\\PycharmProjects\\guppe
print(os.path.isabs(r'C:\Users\Gabriel o Genio\Envs\guppe\Scripts\python.exe'))

# ATENCAO AO CRIAR UM PROGRAMA PARA VARIOS SISTEMAS OPERACIONAIS

# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix = linux e mac | nt = windows

# Podemos ter mais detalher no sistema operacional no LINUX(os.uname())
# NO windows é diferente
unameinfo = platform.uname()

print(unameinfo)

"""
PARTE ESTRANHA - no LINUX

print(os.getcwd()) #caminho atual

res = os.path.join(os.getcwd(), 'geek', 'university') # juntando diretórios.

os.chdir(res)

print(os.getcwd())

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o diretório atual e o segundo o
# diretório que será juntado ao atual.


"""

# Podemos listar os arquivos e diretórios com o listdir()
print(os.listdir())
print(os.listdir('C:\\'))
print(len(os.listdir('C:\\')))  # posso ver o tamanho ainda!@#

# Podemos listar os arquivos e diretórios com mais detalher com scandir()

print(os.scandir('C:\\'))  # Ele gera um iterador
print(list(os.scandir('C:\\')))  # EU POSSO FAZER UMA BAGULHO MUITO LOCO COM ISSO ^^^^^^^^^

print('_'*20)
# OLHA

arquivos = list(os.scandir())

print(arquivos)

print(dir(arquivos[0]))

# FUNCIONA MAS FICA ASSIM
print('ARMAZENEI OS CAMINHOS DO DIRETORIO')
print('__________________________________')

print(arquivos[0].inode())  # ??
print(arquivos[0].is_dir())  # É um diretório? False ou true
print(arquivos[0].is_file())  # É um arquivo? True ou False
print(arquivos[0].is_symlink())  # É um link simbólico? False ou True
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)  # Caminho até o arquivo
print(arquivos[0].stat())  # ???

# OBS: Quando utilizamos a função scandir() nós precisamos fecha-la, assim quando abrirmos um arquivo.
print('\nPADRAO FIFA\n')
scanner = os.scandir()

arquivos_pradao_fifa = list(scanner)

print(arquivos_pradao_fifa[0].inode())  # ??
print(arquivos_pradao_fifa[0].is_dir())  # É um diretório? False ou true
print(arquivos_pradao_fifa[0].is_file())  # É um arquivo? True ou False
print(arquivos_pradao_fifa[0].is_symlink())  # É um link simbólico? False ou True
print(arquivos_pradao_fifa[0].name)  # Nome do arquivo
print(arquivos_pradao_fifa[0].path)  # Caminho até o arquivo
print(arquivos_pradao_fifa[0].stat())  # ???

scanner.close()
