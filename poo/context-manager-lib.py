# Context Manager com função - criando e usando gerenciadores de contexto
from contextlib import contextmanager
from pathlib import Path

FILE_PATH = Path(__file__).parent / 'arquivos-criados' / 'arquivo-teste2.txt'


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open(FILE_PATH, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('With', arquivo)
