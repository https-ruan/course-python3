""" 
Exiba os índices da lista
"""

lista = ['Maria', 'Helena', 'Ruan']

for nome in lista:
    indice = lista.index(nome)
    print(indice, lista[indice], type(lista[indice]))
