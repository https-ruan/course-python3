""" 
Introdução às funções (def) em Python
Funções são trechos de código usado para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções python retornam None (nada).
"""


""" def imprimir(a, b, c):
    print(a, b, c)


imprimir('Olá', 'Teste', 'Ab')
imprimir(1, 2, 3) """


def saudacao(nome='Fulano'):
    print(f'Olá {nome}!')


saudacao('Ruan Araujo')
saudacao()
