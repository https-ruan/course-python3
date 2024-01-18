""" Calculadora com while """
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    n1_float = 0
    n2_float = 0
    numeros_validos = None

    try:
        n1_float = float(numero1)
        n2_float = float(numero2)
        numeros_validos = True
    except Exception as error:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')
    if operador == '+':
        print(n1_float + n2_float)
    elif operador == '-':
        print(n1_float - n2_float)
    elif operador == '/':
        print(n1_float / n2_float)
    elif operador == '*':
        print(n1_float * n2_float)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair:
        break
