
tabelanomes = [1, 2, 2, 2, 3, 4, 6, 5, 7, 8, 9]

print(tabelanomes)

tabelanomes.append(5)

print(tabelanomes)

tabelanomes.append([8, 8, 8, 6, 18])

print(tabelanomes)
#o .count não acha o elemento que adicionei no .append
print(tabelanomes.count(8))
#existe a possibilidade de armazenar-mos as listas dentro de listas.
#Mas não podemos encontrar um elemento só, apenas o conjunto.
#Deve-se usr .extend para ficar dentro da lista.
if [8, 8, 8, 6, 18] in tabelanomes:
    print("sim")
else:
    print("não")

tabelanomes.extend([55, 65, 95, "r", "m"])

print(tabelanomes)
#com .extend podemos encontrar apenas um elemento da lista
#ATENCAO GABRIEL, EM PYTHON PODEMOS ADICIONAR QUALQUER TIPO DE DADO NAS LISTAS
if "m" in tabelanomes:
    print("sim")
else:
    print("não")

#usamos .insert para selecionarmos uma posição na lista

tabelanomes.insert(2, "estou na posição 2")

print('1- ', tabelanomes)

new = list(range(5))

jj = new + tabelanomes

print("2- ", jj)

new.extend(tabelanomes)

print("3- ", new)

jj.extend(new)

print("4- ", jj)

print("5- ", new)

print("6- ", tabelanomes)

print("7- ", new)

print("8- ", jj)

#tem como inverter uma lista

tabelanomes.reverse()

print(tabelanomes)
#ou slice
#no caso do slice apenas muda a exibição não salve nada
print(tabelanomes[::-1])

print(tabelanomes)

#podemos usar .copy para copiar toda um lista em lugar de outra

nova = [1, 2]
jj = nova.copy()

print(jj)

print(tabelanomes)

print(jj)

#usamos len(list) para contar os elementos dela

print(f"existe {len(tabelanomes)} elementos")
print("existe", len(tabelanomes), "elementos")
#remove o ultimo elemento e retorna o elemento, da pra fazer uma transferencia especial. Bem maluca da minha forma.
tabelanomes.pop()

print(tabelanomes)

#remove o elemento na posicao 2, os elementos sao delocados para esquerda, a posicao do lado absorvida na remosao. *cui*dado*Genio*
tabelanomes.pop(2)

print(tabelanomes)
#SEM COMANDOS
#.clear limpa toda a lista

#___________________#

palavras = ["Geek", "Gabriel", "Oliviera"]

print(palavras)
# .join com "qualque coisa no meio da aspas" - coloca um separador entre os elementos e vira string.
cursioso = "=+=".join(palavras)

print(cursioso)

tudoispossive = [True, 4, "k", "belo", 2.4, [1, 2, 3], 564444645645648421]

print(tudoispossive)
