"""
O bloco with

Passo para se trabalhar com arquivos

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo - Encerrar a conexão com o PC

O Block with é utilizado para criar um conjunto de trabalho onde os recursos utilizados
são fechados após o bloco with

"""

# O Bloco with

# O quer dizer:
# with(COM) abra(open) o ('texto.txt') e chame-ele(as) de aquivo:
#     <trabalhe com ele aqui dentro>
with open('texto.txt') as arquivo:
    print(arquivo.readlines())
#   Depois que sair do with jaera(o arquivo é fechado)

# ___-----------É A FORMA PYTONICA
