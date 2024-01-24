# isinstance -> para saber se o objeto é de determinado tipo
lista = ['a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'Luiz'}]

for item in lista:
    print(
        f'{item=}',
        f'is {str(type(item)).split('\'')[1]} ? ->',
        isinstance(item, type(item)),
    )
