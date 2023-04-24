"""
StringIO

ATENÇÃO: Para ler ou escrever dados em arquivos do sistema operacional o software precisa
ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de Escrita -> Para escrever o arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória.
"""

#PRIMEIRO FAZEMOS O IMPORT

from io import StringIO

mensagem = 'Este é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto
# depois

#FICA NA MEMORIA, NAO É .TXT
arquivo = StringIO(mensagem)
arquivo_dois = StringIO('POSSO ESCREVER DIRETO')

print(arquivo.read())

# Escrevendo outros textos
arquivo.write(' Outro texto')

# Podemos inclusive movimentar o cursor - WTF
arquivo.seek(0)

print(arquivo.read())
print(arquivo_dois.read())
