import json

caminho = 'D:\\Desenvolvimento\\Git\\course-python3\\intermediario\\arquivos-criados\\arquivo-json.json'

# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open(caminho, 'w', encoding='utf8') as arquivo:
#     json.dump(
#         pessoa, 
#         arquivo,
#         ensure_ascii=False,
#         indent=2
#     )

with open(caminho, 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)