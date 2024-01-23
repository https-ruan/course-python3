""" 
A função lambda é uma função como qualquer outra em python. Porém, são funções anônimas que contém apenas uma linha, ou seja, tudo deve ser contigo dentro de uma única expressão.
"""


# lista = [4, 231, 23, 21, 43, 65, 3, 4, 1]
# lista.sort()
# sorted(lista) # shallow copy


lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Ruan', 'sobrenome': 'Araujo'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Izabelly', 'sobrenome': 'Santana'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
]


def exibir(lista):
    for item in lista:
        print(item)


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
