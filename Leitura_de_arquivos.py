"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(),
que literalmente significa 'abrir'

open() -> Na forma mais simples de utilização nós passamos apenas um parametro de entrada, que neste
caso é o caminho para o arquivo ser lido. Essa função retorna um _io.TextIOwrapper e é com ele
que trabalhamos então.

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então
teremos o erro FileNotFoundError

"""
# Exemplo

arquivo = open('texto.txt')

print(arquivo)

print((type(arquivo)))

# Para ler o conteudo de uma arquivo, após sua abertura, devemos utilizar a função read()
print(arquivo.read())
# Ele não imprime duas vezes
print(arquivo.read())
# OBS: O Python, utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo.


