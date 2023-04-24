#iterando (repetindo) listas

blabla = list(range(8))
lista2 = [5, 4, 3, 55, 20]
tipostring = ['h' ,'h' , 'e', 'f']

#exemplo 1 - com for
print(blabla)
#tudo depende do tipo de dado
soma = 0
for elemento in blabla:
    print(elemento)
    soma = soma + elemento
print(soma)
print("----------------------------------")
soma2 = " "

for elemento2 in tipostring:
    print(elemento2)
    soma2 = soma2 + elemento2
print(soma2)

#exelmplo 2 ultilizando while

contador = 'online'
somador = 0
incre = 0

print(f"elementos da lista {blabla} somados:")
while contador == 'online':

    incre = blabla.pop()
    somador = somador + incre

    if blabla == [0]:
        contador = 'offline'

print(somador)
print(blabla)
