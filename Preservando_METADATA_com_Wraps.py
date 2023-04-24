"""
Preservendo metadatas com wraps

Metadados -> São dados intrinsecos em arquivos.

wraps -> São funções que envolvem elementos com diversas finalizadas

"""
from functools import wraps
# Problemas


def ver_log(funcao):
    # DESBUGAMOS O DECORATOR
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando: {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, *kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois númeors"""
    return a + b


print(soma(10, 30))

"""
Atenção com esse bug

*Se você criar um módulo e o metadado dele estiver bugado vai ficar igual está abaixo a documentação

- PARA RESOLVER usamos: from functools import wraps
"""
print(soma.__name__)
print(soma.__doc__)
