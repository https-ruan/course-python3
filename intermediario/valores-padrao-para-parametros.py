""" 
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
"""


def soma(x, y, z=0):
    print(f'{x=} {y=} {z=}', x + y + z)


soma(1, 2)
soma(1, 2, 0)
