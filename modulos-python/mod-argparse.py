# argparse.ArgumentParses para argumentos mais complexos
# Tutorial oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help="Mostra \"Olá mundo\" na tela",
    # type=str, # Tipo do argumento
    metavar='',
    # default='Olá mundo', # Valor padrão
    required=False,
    action='append'  # Recebe o argumento mais de uma vez
    # nargs='+' # Recebe mais de um valor
)

parser.add_argument(
    '-v', '--verbose',
    help="Mostra logs",
    action='store_true'  # Verifica se argumento foi passado
)
args = parser.parse_args()

if args.basic is None:
    print('Você não passou o valor de b.')
else:
    print('O valor de b:', args.basic)

print(args.verbose)
