"""
Entendendo Iterators e Iterables

Iterator ->
    - Um objeto que pode ser iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada:

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.


"""
nome = 'Geek'  # É um iterable mas não é um iterator
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable mas não é um iterator

#     Transforma em iterable
it1 = iter(nome)
it2 = iter(numeros)
#     Roda o iterable
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
# ____________
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
# ____________
print('_'*20)
# POR BAIXO DOS PANOS

#            aplica o iter, básicamente o for faz o controle, para nao dar o erro.
for letra in nome:
    print(f'{letra}')
