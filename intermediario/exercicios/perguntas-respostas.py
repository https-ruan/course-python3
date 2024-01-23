# Sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertou = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    print('Opções:')

    alternativas = pergunta['Opções']
    for i, alternativa in enumerate(alternativas):
        print(f'{i}) {alternativa}')

    resposta = input('Escolha uma opção: ')
    if alternativas[int(resposta)] == pergunta['Resposta']:
        print('Acertou 👌🏻')
        acertou += 1
    else:
        print('Você errou... 😬')

    print()

print(f'Você acertou {acertou} de {len(perguntas)} perguntas.')
