"""
Escrevendo em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Está função recebe uma string como parámetro.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado,
caso ele já exista, o anterior será apagado e um novo será criado. Dessa forma, todo o conteudo
no arquivo anterior é perdido.
"""

# Exemplos de ESCRITA
#                     modo escrita WRITE
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil\n')
    arquivo.write('Podemos colocar quantas linha quisermos.\n')
    arquivo.write('Está é a última linha')
with open('novo.txt') as arquivo:
    print(arquivo.read())

with open('frutas.txt', 'w') as arq:
    # o while ta em loop infinito
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            # deixar bonitinho pra nao zuar o arquivotudojunto
            arq.write(fruta)
            arq.write('\n')
        else:
            break  # esse break para tudo que estiver atrás

with open('frutas.txt') as arq:
    print(arq.read())
