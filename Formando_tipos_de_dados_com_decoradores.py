"""
Forçando tipos de dados com decoradores

"""


def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))  # aqui está acomtecendo um CAST- conversao de valores
            return funcao(*novo_args, **kwargs)
        return converter
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


repete_msg('geek', '3')
dividir(1, 5)

# O PROFESSOR TA MOSCANDO, MAS ELE ARRUMOU
