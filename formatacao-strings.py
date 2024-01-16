nome = 'Ruan'
altura = 1.67
peso = 80
imc = peso / (altura * altura)

# * f-strings
linha_1 = f'{nome} tem {altura: .2f} de altura'
linha_2 = f'pesa {peso}, quilos e seu IMC é{imc: .2f}'

print(linha_1)
print(linha_2)

# * função format()
a = 'AAA'
b = 'BBBB'
c = 1.1
string = 'a={0}, b={1}, c={nome3: .2f}'
formato = string.format(a, b, nome3=c)
print(formato)
