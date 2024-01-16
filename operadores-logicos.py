# Operadores lógicos
# and (e) or (ou) not (não) in (entre) not in (nao entre)

# and - Todas as condições precisam ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False

# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdadeiro,
# a expressão inteira será avaliada naquele valor.

# not - usado para inverter expressões
# not True = False
# not False = True

# in -
#  0 1 2 3
#  R u a n
# -4-3-2-1

# not in -
#
#

# Também existe o tipo None que é
# usado para representar um não valor


# * and - or - not
""" entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida and not not 0:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print((True and 0 and True))
print(True or False) """

# * in - not in
# nome = 'Ruan'
# print(nome[2])
# print(nome[-4])
# print('a' in nome)
# print('z' in nome)
# print('b' not in nome)
nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
