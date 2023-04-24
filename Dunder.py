"""
Dunder name e Dunder Main

Dunder -> Doble Under

Dunder Name -> __name__

Dunder Main -> __main__

Em Python são utilizados dunter para criar funções, atributos, propriedade e etc utilizando
Double Under para não gerar conflito com os nomes desse elementos na programação.

__________________________

Ele que explicar que em Python não precisamos colocar o MAIN no inicio do programa.
__________________________
# Na linguamge C, temos um programa da seguinte forma:

int main(){
   return 0;
}

# Na linguegem Java, temos um programa da seguinte forma:

public static void main(String[] args){

}

___________

# Em Python, se executarmos um módulo Python diretamente na linha de comando, internamente
o Python atribuirá á variávek __name__ o valor __main__ indicando que este módulo é o de
execução principal.

Básicamente é tipo o main() do C

Quando importar algo você deve especificar que não deve executar as outras linhas, pois o arquivo 
importado nunca deve executar nada sem a autoridade __main__

####OLHA ESSA POHA E SE LEMBRA

EU fui importado

def prazer():
   return 'eu vou ser executado, pois fui chamado pelo __main__'

if __name__ == '__main__'
    print('nao sou o arquivo principal')
    print ('Essa linha de codigo nao vai ser executada.')
"""

import primeiro
import segundo

