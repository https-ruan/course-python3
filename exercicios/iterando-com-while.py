""" 
Iterando strings com while
"""
#       012345678910
nome = 'Ruan Araujo'  # Iteráveis
tamanho_nome = len(nome)
indice = 0
nova_string = ''

while indice < tamanho_nome:
    nova_string += f'*{nome[indice]}'
    indice += 1

nova_string += '*'
print(nova_string)
