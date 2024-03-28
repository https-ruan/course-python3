# sys.argv -> Executando arquivos com argumentos no sistema
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    print(f'Você passou os argumentos {argumentos[1:]}')
    print(f'Faça alguma coisa com {argumentos[1]}')
    print(f'Faça alguma coisa com {argumentos[2]}')
