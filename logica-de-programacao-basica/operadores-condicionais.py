# if / elif / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
    print('Este é o código do if')
elif entrada == 'sair':
    print('Você saiu do sistema')
    print('Este é o código do elif')
else:
    print('Valor inválido')
    print('Este é o código do else')
