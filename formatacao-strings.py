
# * f-strings
# nome = 'Ruan'
# altura = 1.67
# peso = 80
# imc = peso / (altura * altura)
# linha_1 = f'{nome} tem {altura: .2f} de altura'
# linha_2 = f'pesa {peso}, quilos e seu IMC é{imc: .2f}'

# print(linha_1)
# print(linha_2)

# * f-strings pt2
"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel:$<10}.')
print(f'{variavel:0^10}.')
print(f'{1000.231231241234:0>+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'{variavel!r}')

# * função format()
# a = 'AAA'
# b = 'BBBB'
# c = 1.1
# string = 'a={0}, b={1}, c={nome3: .2f}'
# formato = string.format(a, b, nome3=c)
# print(formato)

# * interpolação básica com %
# s - string
# d / i - int
# f - float
# x / X - Hexadecimal (ABCDEF0123456789)
# nome = 'Ruan'
# preco = 1000.92131342
# variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
# print(variavel)
# print('O hexadecimal de %d é %08X' % (1523, 1523))
