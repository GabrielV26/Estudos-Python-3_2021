"""
POO - Heranca (Inheritance)

A ideia de heranca é a de reaproveitar código. Tambem extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Pergunta: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos
comuns a outras entidades?

OBS: quando uma classe herda de outra classe.
Ela Herda Todos os atributos e Métodos da classe herdada.

______________________________________________________________________________
Quando uma classe herda de outra classe, a classe herdada é conhecida por:

                        [Pessoa]
                        - Super Classe;
                        - Classe Mãe;
|é tudo a mesma coisa|  - Classe Pai;
   NOMECLATURAS         - Classe Base;
                        - Classe Genérica;

Qunado uma classe herda de outra classe, ela é chamada;
   NOMECLATURAS         [Cliente, Funcionario]
                        - Sub Classe;
|é tudo a mesma coisa|  - Classe Filha;
                        - Classe Especificad;
______________________________________________________________________________

# Sobrescrita de métodos, ocorre quando rescrevemos/reimplementamos um método presente na super classe
em classes filhas
"""


class Pessoa:
    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


#             heranca
class Cliente(Pessoa):
    """Cliente herda de pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda):
        # super() -> Usado para chamar os métodos da classe herdade.
        # Podemos chamar qualquer método.
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda


#   super().nome_completo() já ta salvo isso aqui


#             heranca
class Funcionario(Pessoa):
    """Funcionario herda de pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        # TEM QUE CHAMAR O SUPER
        super().__init__(nome, sobrenome, cpf)
        # ou Pessoa.__init__(self, nome, sobrenome, cpf)
        self._Pessoa__nome = nome + ' ' + sobrenome
        self.__matricula = matricula

    # GABRIEL GENIO - TEM QUE COLOCAR OS PARAMETROS TUDO CERTINHO
    def nome_completo(self):
        # print(super().nome_completo())
        #                                            LEMBRA QUE É PRIVADO
        return f'Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}'


#  Sobrescrita de Métodos (Overriging) - Linha 43(método) foi junto na heranca
cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
