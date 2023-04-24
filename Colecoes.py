"""
Dicionarios sao entre {} e voce define o indice

_
Chave e valor sao separados por :
tanto chave e valor podem ser de qualquer tipo de dado chave:valor
podemos misturar tipos de dados;

_
"""
#forma mais comum - criacao de dicionarios
dicionario = {"barco": 1, 2: 4, 6: "prato"}

print(dicionario)

#forma dois

paises = dict(br="Brasil", eua="Estados Unidos")

print(paises)
print(type(paises))

#acessamdo elementos

#forma 1 - via chave

print(paises["br"])
print(dicionario[2])

#caso o valor Nao seja encontrado o valor retornado é KeyError

#forma 2 - vira get - forma recomendada

print(dicionario.get(2))
print(paises.get("br"))

#Usando .get se a chave procurada nao for encontrada o retorno é NONE
#OOOOOOOOOOOBBBBBBBBBBBBBBBBSSSSSSSSSSSSSSSSSS::::
# SOBRE NONE
#Podemos utilizar None quando queremos criar uma variavel e inicializala com um tipo sem tipo, antes
#de recebermos um valor final. O tipo no none = NoneType -
#O TIPO NONE ««é sempre considerado Falso

numeros = None
print(type(numeros))

#_____________________

#retorna um valor falso, pois entendese como None e None e o valor após a virgula é adicionado no lugar

#PROBLEMA ele SUBESCREVE TODO O DICIONARIO

paises = paises.get("ru", "nao encontrado")

#nao funcionou da forma esperada ele nao preenche a lacuna ou cria uma nova

# esse modo funciona, porem nao é indicado
#paises["ru"] = "encontrado"
#COLOCANDO NOVOS ITENS
#indeice = input("indice: ")
#item = input("item: ")
#paises[indeice] = item
print(paises)

paises1 = {"br": "Brasil", "usa": "Estados Unidos da América", 1: 2}


#FORMA CORRETA DE LOCALIZACAO(CHAVE), MAS ELE NAO ENCONTRA STRING DA FORMA .get DE INSERIR DADOS
print("br" in paises1)
#a forma correta é buscar pela chave, abaixo está errado.
print("br" in paises)


paises1.update({"w": "u"})
print(paises1)

#ADICINAR NO DICIONARIO
#forma 1
paises1["w"] = 1253
print(paises1)
#forma 2
paises1.update({"w": 25})
print(paises1)

#CONCLUSAO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma.
#CONCLUSAO 2: Em dicionarios nao podemos ter chaves repetidas (entendeu?) nao da pra repetir chavex: 1:5 1:7 nao existe
# ele apenas atualiza

#REMOVER DO DICIONARIO
#FORMA 1
retorno = paises1.pop("br")
print(retorno)
print(paises1)

# OBS 1: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor da chave é retornado.

#FORMA 2

del paises1["w"]
print(paises1)
#OBS: Neste caso não é retornado o valor da chaves

#LOJINHA ARMAZENADAS DENTRO DE UMA [LISTA]={COLECAO}

carrinho = []

produto1 = {'nome': 'Play 4', 'quantidade': 1, 'preco': 2300}
produto2 = {'nome': "Good of War 4 ", 'quantidade': 1, 'preco': 230}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#É a melhor forma, mas da pra adicionar tupla dentro do dicionario.

# criando Chave automaticamente com fromkeys

gatos = {}.fromkeys(range(1, 30), 'vazio')

print(gatos)

#MODIFICANDO UM DICIONARIO = MAPAS
gatos.update({1: 'algo'})

print(gatos)
