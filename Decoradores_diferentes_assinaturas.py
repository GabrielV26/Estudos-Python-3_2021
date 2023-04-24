"""
Decorators com diferentes assinaturas


A Assinatura de uma função é representada pelo seu retorn, nome e parâmetro de entrada.
"""
# FODA


def gritar(funcao):
    #            diferentes assinaturas - ENTRADAS
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal} acompanhado de {acompanhamento}, por favor'


print(saudacao('Felicity'))

print(ordenar('Picanha', 'Batata Frita'))


# OBS: Vale lembrar que podemos utilizar parâmetros nomeados
#             nomeado                     nomeado
print(ordenar(acompanhamento='maracuja', principal='banana'))

print("\n___________________________________________________\n")

"""
Decorators com argumentos
"""


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


# com argumento obrigatório
@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)


# com argumento obrigatório
@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# TESTANDO


print(soma_dez(10, 12))

#  ERRO o primeiro parametro tem que ser OBRIGATORIAMENTE 10 - linha 60 - e não 1
print(soma_dez(1, 21))


print(comida_favorita('pizza', 'churrasco'))

#  ERRO o primeiro parametro tem que ser OBRIGATORIAMENTE pizza - linha 54 - e não 1
print(comida_favorita('feijao', 'pizza'))
