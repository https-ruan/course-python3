""" 
Introdução ao desempacotamento + tuples (tuplas)

Tipo tupla -> Uma lista imutável
"""
_, nome2, *_ = ['Maria', 'Helena', 'Ruan']
print(nome2, _)

# * tupla
tupla = ('Maria', 'Helena', 'Ruan')
tupla = tuple(['Maria', 'Helena', 'Ruan'])
lista = list(tupla)
print(tupla)
