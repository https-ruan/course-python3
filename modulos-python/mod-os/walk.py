# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('C:\\Users', 'Ruan', 'OneDrive', 'Desktop')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual:', root)

    for dir_ in dirs:
        print('  ', the_counter, 'DIR:', dir_)

    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)
        print('  ', the_counter, 'File:', caminho_completo_arquivo)
        # os.unlink(dir) #remove tudo da pasta
