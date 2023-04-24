""""
nome = input("Qual é seu nome? ")

x = int(input("posição: "))

for indice, arquivo in enumerate(nome):
    print(indice, arquivo)
print(f"Posição:{x} Letra:{nome[x].upper()}")
"""

qtd = int(input('TABUADA DO: '))

for var in range(1, qtd+2, 1):
    #print(f"imprimindo {var}")
    print(f"nume da entrada {qtd} X {var} = {var*qtd}")
