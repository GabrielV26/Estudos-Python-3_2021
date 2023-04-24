"""
Decoradores (Decorators)

O que são decorators?

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions:
- Decorators tem uma sintaxe própria, usando '@' (Syntact Sugar / Açucar Sintático)


/------------------------------------------\
/       Function Decorator                 \
____________________________________________
_______________________________________________
/ /__________________________________________\\
/ /           Função                        \\
/ /__________________________________________\\
_______________________________________________

VOCÊ APRIMIMORA O QUE JÁ TEM, NÃO COPIA.
"""
# Decorators como funções ( Sintaxe não recomendada / Sem Açucar Sintático)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem vindo')

# teste


teste = seja_educado(saudacao)

teste()

"""
A RECOMENDADA É - COM AÇUCAR - o @ 
"""
print('\n_RECOMENDADO_______________\n')


def seja_educado_mesmo(recebi_la_de_baixo):
    def mostrando_o_que_juntei():
        print('Foi um prazer conhecer você')
        recebi_la_de_baixo()
        print('Tenha um bom dia')
    return mostrando_o_que_juntei


@seja_educado_mesmo
def vai_entrar_na_de_cima():
    print('Meu nome é Tatu')


vai_entrar_na_de_cima()
