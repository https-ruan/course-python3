# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
from genericpath import exists
import os
import shutil

# HOME = os.path.expanduser('~')
CURRENT_FOLDER = os.path.split(__file__)[0]
PASTA_ORIGINAL = os.path.join(CURRENT_FOLDER, 'Arquivos')
NOVA_PASTA = os.path.join(CURRENT_FOLDER, 'Nova-pasta')

# os.makedirs(NOVA_PASTA, exist_ok=True)


# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_)
#         print(dir_)
#         os.makedirs(NOVA_PASTA, exist_ok=True)

#     for file in files:
#         caminho_arquivo = os.path.join(root, file)
#         caminho_novo_arquivo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file)

#         shutil.copy(caminho_arquivo, caminho_novo_arquivo)

# * Apagando, copiando, movendo e renomeando
shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
shutil.move(NOVA_PASTA + '-2', NOVA_PASTA)
