"""
    CONJUNTOS

    - CONJUNTOS EM QUALQUER LINGUAGEM DE PROGRAMACAO, ESTAMOS FAZENDO REFERENCIA A TEORIA DOS CONJUNTOS DA MATEMATICA
    - AQUI NO PYTHON OS CONJUNTOS SAO CHAMADOS DE SETS

    DITO ISTO, DA MESMA FORMA QUE NA MATEMATICA

    - SETS (CONJUNTOS) NAO POSSUEM VALORES DUPLICADOS
    - SETS (CONJUNTOS) NAO POSSUEM VALORES ORDENADAS
    - ELEMENTOS NAO SAO ACESSADOS VIA INDICE, OU SEJA, CONJUNTOS NAO SAO INDEXADOS

CONJUNTOS SAO BONS PARA SE UTILIZAR QUANDO PRECISAMOS ARMAZENAR ELEMENTOS
MAS NAO NOS IMPORTAMOS COM A ORDENACAO DELES. QUANDO NAO PRECISAMOS SE PREOCUPAR COM CHAVES, VALORES E ITENS DUPLICADOS.

OS CONJUNTOS (SETS) SAO REFERENCIADOS EM PYTHON COM CHAVES{}

DIFERENÇAS ENTRE CONJUNTOS(SETS) E MAPAS(DICIONARIOS) EM PYTHON

    - UM DICIONARIOS CHAVE/VALOR
    - UM CONJUNTOS TEM APENAS VALOR

"""

#Definindo um conjunto
#FORMA 1

s = set({1, 2, 3, 4, 5, 5, 6})

# o conjunto ignora itens repetidos

print(s)
print(type(s))

#FORMA 2 - mais comum

x = {1, 2, 3, 4, 5, 5, 6}

print(x)
print(type(x))


#APRENDIDOS - REPARA QUE DICIONARIOS E CONJUTOS NAO REPETEM
#LEMBRANDO QUE é ACEITO QUALQUER ELEMENTO 14,j,1.4,'w',

print('___________')

#LISTAS aceitam valores duplicados - 6
lista = [1, 2, 3, 4, 1, 5]
print(f"dicionario: {lista} tamanho: {len(lista)}")

#TUPLAS aceitam valores duplicados - 6
tupla = (1, 2, 3, 4, 1, 5)
print(f"dicionario: {tupla} tamanho: {len(tupla)}")

#DICIONARIOS não aceitam chaves duplicadas - 5 - o conjunto faz sua propria ordenacao
dicionario = {}.fromkeys([1, 2, 3, 4, 1, 5], "ss")
print(f"dicionario: {dicionario} tamanho: {len(dicionario)}")

#CONJUNTOS não aceitam valores duplicados - 5
conjunto = {1, 2, 3, 4, 1, 5}
print(f"dicionario: {conjunto} tamanho: {len(conjunto)}")

print('___________')

s = {1, 2, 3}

#remover elementos de um conjunto
#nao é indice, pois os conjuntos nao sao indexados.
s.remove(2)
#O VALOR REMOVIDO NAO RETORNA
#SE O VALOR NAO FOR ENCONTRADO GERA UM KeyError

print(s)

#Forma 2

#DISCARD NAO RETORNA ERRO SE O VALOR NAO FOR ENCONTRADO
s.discard(1)

print(s)

#COPIANDO UM CONJUNTO PARA OUTRO
#FOMRA 1 DEEP COPY
print("________Deep Copy________\n")

novo = s.copy()
novo.add(4)

print(novo)
print(s)

print('_')
u = {3}

print("______Shalow Copy______\n")

novoo = u
novoo.add(4)

print(u)
print(novo)

print('______unindo__conjuntos_____')
tumarA = {'gabriel', 'henrique', 'intruso'}
turmaB = {'Leandro', 'oliveira'}

#FORMA 1 - recomendada
#LEMBRAR QUE CONJUNTOS NAO REPETEM VALORES
unindoConjuntosF1 = tumarA.union(turmaB)

print(unindoConjuntosF1)

#FORMA 2 - com pipe |

unindoConjuntosF2 = tumarA | turmaB

print(unindoConjuntosF2)

#UNINDO APENAS OS IGUAIS
#FORMA 1
print('_______________')
turmaD = {'gabriel', 'henrique', 'intruso', 'Leandro'}
turmaC = {'Leandro', 'oliveira'}

ambos = turmaC.intersection(turmaD)

print(ambos)

print('_____________')
#FORMA 2 - UTILIZANDO O &

ambos2 = turmaC & turmaD

print(ambos2)

print('______')

print(f'TUMAC: {turmaC}')
print(f'TUMAD: {turmaD}')

# GERA UM CONJUNTO DE ALUNOS QUE NÃO ESTA NA TURMA D
# QUEM DA TURMA C NAO ESTA NA TURMA D
soC = turmaC.difference(turmaD)

print(soC)

with open('C:\\Users\\Gabriel\\Desktop\\manipula\\ARQUIVINHO.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(str(conteudo))
