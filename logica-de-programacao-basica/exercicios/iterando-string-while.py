frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_letras = frase.count(letra_atual)

    if letra_atual == ' ':
        i += 1
        continue

    if apareceu_mais_vezes < qtd_letras:
        apareceu_mais_vezes = qtd_letras
        letra_apareceu_mais_vezes = letra_atual

    i += 1

print(f'A letra \'{letra_apareceu_mais_vezes}\' apareceu {
      apareceu_mais_vezes} dentro da frase.')
