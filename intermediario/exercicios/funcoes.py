""" 
Exercício com funções

Crie uma função que multiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.

Crie uma função fala se o número é par ou ímpar.
Returne se o número é par ou ímpar
"""


def multiplicacao(*args):
    total = 1

    for num in args:
        total *= num

    return total


resultado = multiplicacao(1, 2, 3)
print(resultado)
print(1*2*3)


def par_ou_impar(num):
    return f'{num} é par' if num % 2 == 0 else f'{num} é ímpar'


print(par_ou_impar(resultado))
