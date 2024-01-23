""" 
Argumentos nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


# def soma(x, y):
#     # Definição
#     print(f'{x=} {y=}', '|', 'x + y = ', x + y)


# soma(1, 2)
# soma(y=2, x=1)


# * Vários argumentos de forma simples
# *args -> empacotamento e desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


def soma(*args):
    total = 0

    for arg in args:
        total += arg

    return total


soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

numeros = 1, 2, 3, 4, 5, 6, 7
print(soma(*numeros))
