"""
Sistemas de Arquivos - Manipulação

"""

import os
import os.path

# DESCOBRINDO se um ARQUIVO ou DIRETORIO EXISTE

#print(os.path.exists(r'C:\Users\Gabriel o Genio\Desktop'))  # Buscando fora da pasta atual
#print(os.path.exists(r'C:\Users\Gabriel o Genio\Desktop\nada.txt'))  # Buscando fora da pasta atual
#print(os.path.exists('texto.txt'))  # Dentro da pasta atual


# Criando ARQUIVOS

# Forma 1
#open('arquivo-teste.txt', 'w').close()

# Forma 2
#open('arquivo-teste2.txt', 'a').close()

# Forma 3
#with open('arquivo-teste3.txt', 'w') as arquivo:
 #   pass

# MELHOR FORMA É ESSA DE CRIAR ARQUIVOS E PASTARS - NAO FUNCIONOU

# os.mknod('arquivo-teste4.txt')  # NO linux funciona normal

# os.mknod(r'C:\Users\Gabriel o Genio\Desktop\criado.txt')

# os.mkdir('funciona')  # já foi criado


# CRIAR ARVORE DE DIRETORIOS

# os.makedirs(r'C:\Users\Gabriel o Genio\Desktop\nova\pasta')  # AQUI SO CRIA OS DIRETORIOS
#                                                          Se existir os diretórios, Não gera ERROR
#os.makedirs(r'C:\Users\Gabriel o Genio\Desktop\nova\pasta', exist_ok=True)

# RENOMEAR ARQUIVOS ou DIRETORIOS

# os.rename(r'C:\Users\Gabriel o Genio\Desktop\nova\pastaNOVA', r'C:\Users\Gabriel o Genio\Desktop\nova\pastaNova2')

# os.remove('frutas.txt')

# os.rmdir(r'C:\Users\Gabriel o Genio\Desktop\nova\pastaNOVA')# apenas diretorio, 'vazrios'

# removendo uma arvore de diretório

#for arquivo in os.scandir(r'C:\Users\Gabriel o Genio\Desktop\nova\pastaNova2\Nova Pasta'):
    #if arquivo.is_file():
        #os.remove(arquivo.path)
  #  if arquivo.is_file():
   #     os.rmdir(arquivo.path)

#Podemos remover uma arvore de diretórios vazios

#os.removedirs(r'C:\Users\Gabriel o Genio\Desktop\nova\pastaNova2\Nova Pasta')
"""
Alguns arquivos ficam na pasta de arquivos temporarios, esse é o motivo de utilizar tempfile(arquivos temporarios)

"""

import tempfile
# Criando um diretorio e um arquivo temporario
# Só existem dentro do if, saiu dele some tudo
"""
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario;.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()
    
with tempfile.TemporaryFile() as tmp:
    # Utilizando o 'b' convertendo a string para binário.
    # Só conseguimos utilizar bits
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())
    
                          OU
    
# igual o de cima, porém sem 'with'

arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()

# Sem o bloco with temos que dar o fechamento manual
"""

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso, utilizamos b


# Não printa o conteudo, mas dica dentro do arquivo
arquivo = tempfile.NamedTemporaryFile()
arquivo.write(b'Geek University')

print(arquivo.name)
print(arquivo.read())
input()
arquivo.close()
