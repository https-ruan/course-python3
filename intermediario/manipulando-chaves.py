# Manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome'
pessoa[chave] = 'Ruan Araujo'
pessoa['sobrenome'] = 'Silva'

print(pessoa['nome'])
print(pessoa[chave])

# del pessoa['sobrenome']
print(pessoa)

# print(pessoa.get('sobrenome', 'Não existe'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
