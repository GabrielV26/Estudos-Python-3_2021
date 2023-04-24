"""
Geradores

- Geradores (Generators) são Iterators (Iteradores):

OBS: O contrário não é verdadeiro, Ou seja, nem todo iterator é um generator.

Outras informações:

- Generatores podem ser criados com função geradores;
- Funções geradores utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (funções geradiras)

________________________________________________________________________________
| Funções                             | Generator Functions                   |
________________________________________________________________________________
| Utilizam return                     | Utilizam yield                        |
________________________________________________________________________________
| retorna uma vez                     | Podem utilizar yield multiplas vezes  |
________________________________________________________________________________
| retorna None ou valor               | quando executada, retorna um generator|
________________________________________________________________________________

"""
# Exemplo Função Geradora (Generator Function)


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        # com yield não saimos da função - ficamos parado aqui - até uma função next aparecer.
        # aguarda o proximo next
        yield contador
        contador = contador + 1


# OBS: Uma Generator Function não é um Genarator. Ela gera um generator, ok?

gen = conta_ate(5)

# interessante
print(next(gen))  # 1

print('observe que inicia no 2')
for num in gen:
    print(num)

# olha que legal

gen = list(conta_ate(5))

print(gen)
