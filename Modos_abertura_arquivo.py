"""
Modos de abertura de arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista
x -> Abre para escrita - apenas se o arquivo não existir ##FODA##
a -> Abre para escrita - escreve no final do arquivo
+ -> Abre para o modo leitura e escrita

"""
#  USANDO O x Abre para escrita - apenas se o arquivo não existir ##FODA##
try:
    with open('university.txt', 'x') as arquivo:
        arquivo.write('teste de conteudo')
except FileExistsError:
    print('Arquivo já existe')

#  USANDO O a Abre para escrita - escreve no final do arquivo
"""
EXEMPLO escrever na ultima linha
"""
with open('frutas.txt', 'a') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

with open('frutas.txt') as arquivo:
    print(arquivo.read())

"""
ESCREVER NA LINHA DO TOPO
"""
#                       ele substitui as primeiras linhas
with open('frutas.txt', 'r+') as arquivo:
    while True:
        fruta = input('Informe um fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break

with open('frutas.txt') as arquivo:
    print(arquivo.read())

