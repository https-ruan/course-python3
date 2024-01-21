import random

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

multiplicador_1 = 10
multiplicador_2 = 11
resultado_digito_1 = 0
resultado_digito_2 = 0

# * Primeiro Digito
for digito1 in nove_digitos:
    resultado_digito_1 += int(digito1) * multiplicador_1
    multiplicador_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# * Segundo Digito
dez_digitos = nove_digitos + str(digito_1)
for digito2 in dez_digitos:
    resultado_digito_2 += int(digito2) * multiplicador_2
    multiplicador_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'
print(cpf_gerado)
