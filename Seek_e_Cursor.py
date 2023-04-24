"""
Seek e cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.

"""

arquivo = open('texto.txt')

print(arquivo.read())  # podemos limitar a quantidade de caracteres colocando parametros na funcao
# .read(quantidade_de_caracteres)

#  seek() -> A função seek() é utilizada oara movimentação do cursor pelo arquivo. Ela recebe um
#  parametro que indica onde queremos colocar o cursor.

#  Movimentando o cursor pelo arquivo com a função seek()

arquivo.seek(0)

#  Sempre que o cursor for resetado, nós colocamos deve mos chamar o read()
print('\n')
print(arquivo.read())

arquivo.seek(22)
print('\n')
print(arquivo.read())


#  FUNCAO READLINE - função que lê o arquivo linha a linha.
arquivo.seek(22)
print('\n')
print(arquivo.readline())  # ELE

print(arquivo.readline())  # LÊ LINHA A LINHA

ret = arquivo.readline()  # É retornado uma string

print(type(ret))

print(ret)
#  cria uma lista através do split, cada espaço em branco é uma separação. FOD-ce
print(ret.split(' '))

print('_______________________________')
#  FUNCAO READLINES - readlines()

o_mesmo_arquivo = open('texto.txt')
#  Coloca Todo arquivo em uma lista de string
#  Cada linha como sendo um item da lista
print(o_mesmo_arquivo.readlines())

o_mesmo_arquivo.seek(0)

linhas = o_mesmo_arquivo.readlines()  # criando uma lista com a quantidade de linhas
#  contar quantas linha tem um arquivo
print(len(linhas))

"""
Quando abrimos um arquivo com a função open() é criado uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar 
os trabalho com o arquivo devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com um aruivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo;


"""
print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado - Retorna True ou False

arquivo.close()
o_mesmo_arquivo.close()

print(arquivo.closed)  # Aqui está True
