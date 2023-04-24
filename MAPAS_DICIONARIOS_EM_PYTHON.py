"""
MAPAS CONHECIDOS EM PYTHON COMO DICIONARIOS

DICIONARIOS EM PYTHON SAO REPRESENTADOS COM {}

"""

nada = {'sim': 'cuidado', 'nao': 'cuidado', 'meio': 'cuidado'}

#como iterar sobre os nossos dicionarios - LOOP

for chave in nada:
    print(chave)

for chave in nada:
    print(nada[chave])

for chave in nada:
    print(f"{chave}: {nada[chave]}")

print('ssssssssssssss')

print(nada.keys())

#modo PYTHONICO - Acessando as CHAVES
for chave in nada.keys():
    print(f"{chave}: {nada[chave]}")
#ACESSANDO VALORES

for chave in nada.values():
    print(chave)

#DESENPACOTAMENTO DE DICIONARIOS

for chave, valor in nada.items():
    print(f"chave: {chave} valor: {valor}")

# SOMA*, Valor Maximo*, Valor Minimo*, Tamanho*
# SE os valores forem inteiros  e reais.

receita = {'pra': 5, 'pri': 6, 'pro': 7}

print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))
print(len(receita))
