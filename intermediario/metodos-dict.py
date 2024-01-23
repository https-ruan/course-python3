""" 
Métodos úteis dos dicionários

len -> quantas chaves
keys -> iterável com as chaves
values -> iterável com os valores
items -> iterável com chaves e valores
setdefault -> adiciona valor se a chave não existe
copy -> retorna uma cópia rasa (shallow copy)
get -> obtém uma chave
pop -> Apaga um item com a chave especificada (del)
popitem -> Apaga o último item adicionado
update -> Atualiza um dicionário com outro
"""
import copy

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
    'lista': [1, 2, 3]
}

# pessoa.setdefault('idade', None)

# print(len(pessoa))
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())
# print(pessoa['idade'])
# print(pessoa.get('nome'))

# print(pessoa.pop('nome'))
# print(pessoa)
# print(pessoa.popitem())
# print(pessoa)

# pessoa.update({
#     'lista2': [4, 5, 6]
# })
# pessoa.update(lista2=[4, 5, 6])
# pessoa.update((('lista3', [7, 8, 9]), ('idade', 22)))
# pessoa.update([['lista3', [7, 8, 9]], ['idade', 22]])
print(pessoa)


# for valor in pessoa.items():
#     print(valor)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# * Shallow copy e Deep copy
# pessoa2 = pessoa.copy()
# pessoa2 = copy.deepcopy(pessoa)
# pessoa2['nome'] = 'Ruan Araujo'
# pessoa2['lista'][0] = 12
# print(pessoa2)
# print(pessoa)
