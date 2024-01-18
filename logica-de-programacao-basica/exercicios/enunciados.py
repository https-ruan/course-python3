"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero = input('Digite um número inteiro: ')

# if numero.isdigit():
#     par_impar = int(numero) % 2 == 0

#     if par_impar:
#         print(f'O número {numero} é par.')
#     else:
#         print(f'O número {numero} é ímpar.')
# else:
#     print(f'O número {numero} não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada = input('Digite a hora atual (ex: 12): ')

# try:
#     hora_atual = int(entrada)
#     hora_maior_que_zero = hora_atual >= 0
#     esta_de_manha = hora_maior_que_zero and hora_atual <= 11
#     esta_de_tarde = hora_maior_que_zero and not esta_de_manha and hora_atual <= 17
#     esta_de_noite = hora_maior_que_zero and not esta_de_tarde and hora_atual <= 23

#     if esta_de_manha:
#         print('Bom dia')
#     elif esta_de_tarde:
#         print('Boa tarde')
#     elif esta_de_noite:
#         print('Boa noite')
#     else:
#         print('Hora inválida')
# except:
#     print('Por favor, digite apenas números inteiros')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')
letras_nome = len(nome)

if letras_nome <= 4:
    print('Seu nome é curto')
elif letras_nome <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
