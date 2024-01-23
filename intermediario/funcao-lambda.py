""" 
A função lambda é uma função como qualquer outra em python. Porém, são funções anônimas que contém apenas uma linha, ou seja, tudo deve ser contigo dentro de uma única expressão.
"""


# lista = [4, 231, 23, 21, 43, 65, 3, 4, 1]
# lista.sort()
# sorted(lista) # shallow copy


# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'Miranda'},
#     {'nome': 'Ruan', 'sobrenome': 'Araujo'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Izabelly', 'sobrenome': 'Santana'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
# ]


# def exibir(lista):
#     for item in lista:
#         print(item)


# l1 = sorted(lista, key=lambda item: item['nome'])
# l2 = sorted(lista, key=lambda item: item['sobrenome'])

# exibir(l1)
# exibir(l2)

# * lambda complexo
def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
    executa(soma, 2, 3),
    soma(2, 3)
)


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(2))


print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)
