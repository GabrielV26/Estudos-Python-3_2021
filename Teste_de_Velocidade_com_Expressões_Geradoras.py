"""
Teste de Velociadde  com Expressões Geradoras

"""
import time

# FORMAS DIFERENTES DE SE FAZER A MESMA COISA
# Generators


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()

print(ge1)  # Generator

print(next(ge1))
print(next(ge1))
print(next(ge1))
# ...

# Generator Expression

ge2 = (num for num in range(1, 10))

print(ge2)  # Generation Expression

print(next(ge2))
print(next(ge2))
print(next(ge2))

# Realizando o teste de velocidade

# Generator Expression

gen_inicio = time.time()
print(sum(num for num in range(100000000)))  # 100 milhões - 46 seg com 1B
gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()
print(sum([num for num in range(100000000)]))  # 100 milhões - 3 Min e 37 seg
list_tempo = time.time() - list_inicio

print(f'Generator Expression levou: {gen_tempo}')
print(f'List Comprehesion levou: {list_tempo}')
