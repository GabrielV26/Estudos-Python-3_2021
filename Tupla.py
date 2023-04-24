
"""
TUPLAS sao definidas pela virgula e nao pelo uso do parentese
"""
h = (4, 5, 6)

print(f"{h} {type(h)}")

o = 4, 5, 6

print(f"{o} {type(o)}")

i = 4,

print(f"{i} {type(i)}")

# Tuplas sao definidas pela virgula e nao pelo uso do parentese
# modo errado
#ele nao entende o porentese para ser tupla e sim a virgula
u = (4)

print(f"{u} {type(u)}")

#range(inicio, fim, passo)
geratupla = tuple(range(11))

print(geratupla)

#tuplas sao imutaveis, nao podemos fazer adicao e remocao de elementos
# num, num2 = tupla - Nao tem como - NAO EXISTE DESENPACOTAMENTO DE TUPLA
# o * significa= somente valolores inteiros ou reais
# sum* min* max* len

tupla1 = (1, 2, 3)
print(tupla1)

print(sum(tupla1))
print(min(tupla1))
print(max(tupla1))
print(len(tupla1))

#contatenacao de tuplas

tupla2 = 4, 5, 6,

print(tupla1 + tupla2) #ATENCAO - UNIU - APENAS CONTATENOU

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)
print(tupla1)
print(tupla2)

#tuplas sao imutaveis, mas podemos sobrescrever seus valores

tupla1 = tupla1 + tupla2

print(tupla1)

escola = tuple("Geek University")

print(escola.count("e"))

#A unica forma de modificar uma tupla é sobrescrevendo ela.
# LEMBRAR DOS MESES DO ANO

mesesdoano = "Janeiro", "Fevereiro", "Março...",

print(mesesdoano)

#o acesso aos elementos de uma tupla sao semelhantes a de listas

print(mesesdoano[1])

# iterar com while

i = 0

while i < len(mesesdoano):
    print(mesesdoano[i])
    i = i+1

# ENFIM SLICING
#mesesdoano = (inicio, fim, passo)

print(mesesdoano[0:2])
print(mesesdoano[1:])
print(mesesdoano[:1])
print(mesesdoano[:-1])

#  Por que utilizar TUPLAS?
# - tuplas sao mais rapidas
# - tuplas sao mais leves
# - tuplas deixam o codigo mais seguro
# - trabalhar com elementos imutaveis deixa o codigo mais seguro
# - EM tuplas não existe SHALLOW COPY (considerado um problema, segundo o professor)


