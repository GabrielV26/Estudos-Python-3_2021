"""
produto = ' '
listadecompras = []

print("informe o produto desejado, a qualquer momento você pode SAIR\n")
while produto != 'sair':
    produto = input()

    if produto != 'sair':
        listadecompras.append(produto)

print("Seus produtos")
print(listadecompras)
print("foram adicionados")

#interessante
#pense na lista como uma RODA na hora de inverter

print(f" podemos inverter a ordem da lista\n"
      f"[-1] ultima posicao: {listadecompras[-1]}")
print(f"[0] primeira posicao: {listadecompras[0]} ")
"""
#pesquisa de itens em uma lista
listadepesquisa = [5, 5, 5, 6, 7, 555, 5, 8, 9, 5, 10, 20]
#contei o tamanho da listadepesquisa para criar um range de pesquisa
#
print(listadepesquisa)

numero = int(input("Número pesquisado: "))
listadepesquisa.append(numero)
tamanhodalista = int(len(listadepesquisa))
print(tamanhodalista)

#print(listadepesquisa.index(numero))
#logo abaixo está o range definido exatamente no tamanho da listadepesquisa
pesquisador = list(range(1, tamanhodalista))
print(pesquisador)
#eu quero mostrar que seja retornado apenas 1 numero encontrado, ainda nao sei como fazer tal coisa.
listaauxiliar = [0]
listafinal = [0]
locutor = [0]
b = []

for i, d in enumerate(listadepesquisa):
    x = listadepesquisa.index(numero, i)
    listaauxiliar.append(x)
    b = set(listaauxiliar).copy()

#sempre vai existir a resposta 0 e ultimo, mesmo que nao tenho o numero na lista
#nao consigo eliminar o ultimo valor da lista
setada = str(b)

print(f"Está na posição considere os numeros entre 0 e o ultimo: {setada.replace(', 12}','')}")
