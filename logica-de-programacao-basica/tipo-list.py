""" 
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append -> adiciona um item ao final
    insert -> adiciona um item no índice escolhido
    pop -> remove do final ou do índice escolhido 
    del -> apaga um índice
    clear -> limpa a lista
    extend -> estende a lista
    + -> concatena listas

"""

#         01234
#        -54321
# string = 'ABCDE'  # 5 caracteres
# print(bool([])) # falsy
# print(lista, type(lista))

#        0    1      2             3
#       -4   -3     -2            -1
# lista = [123, True, 'Ruan Araujo', 1.2]
# lista[-3] = 'Maria'
# print(lista[1], type(lista[2]))

# * Alterando uma lista com índices
# Create Read Update Delete
# Criar, ler, alterar, apagar = lista[i] (CRUD)
# lista = [1, 2, 3, 4]
# lista[2] = 300
# del lista[2]
# print(lista[2])
# lista.append(5)
# lista.pop()
# print(lista)

# * Inserindo itens em qualquer índice
lista = [1, 2, 3, 4]
lista.insert(0, 5)
print(lista)
