import os

palavra_secreta = 'montanha'
letras_acertadas = ''
tentativas = 0

while True:

    letra_usuario = input('Digite uma letra: ')

    tentativas += 1

    if len(letra_usuario) > 1:
        print('Digite apenas uma letra')
        continue

    if letra_usuario in palavra_secreta:
        letras_acertadas += letra_usuario

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formatada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU! Parabéns!')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Número de tentativas: {tentativas}')
        letras_acertadas = ''
        tentativas = 0
