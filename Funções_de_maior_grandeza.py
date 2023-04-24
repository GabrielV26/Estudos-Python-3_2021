"""
Funções de Maior Grandeza - Higher Order Functions - HDF

O que isso significa?

- Quanto uma linguagem de programação suporta HDF, indica que podemos ter funções
que retornam outras funções como resultado ou mesmo que podemos passar funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
no nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções em Pyhon são Cidadões de primeira classe
"""
from random import choice
# EXEMPLO - DIFININDO AS FUNÇÕES


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções - TOP


print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# NESTED FUNCTIONS - Funções Aninhadas

"""
Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested Functions
ou também Inner Functions (Funções Internas).
"""


def cumprimento(pessoa):
    def humor():
        return choice(('Suma daqui', 'Eu gosto muito de você', 'Bom dia'))
    return humor() + pessoa


print(cumprimento(' Gabriel'))

# EXEMPLO USANDO FUNCAO DENTRO DE FUNCAO


def faz_me_rir():
    def rir():
        return choice(('kk', 'ahshsa', 'hehe'))
    return rir()


print(faz_me_rir())

# Inner Functions (Funções Internas / Nested Functions) podem acessar
# o escopo de funções mais externas.


def fa_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('kk', 'ahshsa', 'hehe'))
        return f'{risada} {pessoa}'
    return dando_risada()

# TESTANDO


print(fa_me_rir_novamente('cara'))
