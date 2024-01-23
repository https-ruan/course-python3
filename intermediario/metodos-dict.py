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
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900
}

pessoa.setdefault('idade', None)

# print(len(pessoa))
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())
# print(pessoa['idade'])


# for valor in pessoa.items():
#     print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)
