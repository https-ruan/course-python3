""" 
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índice inexcistentes da lista.
"""
import os

lista_usuario = []

while True:
    opcao = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar: ')

    if len(opcao) > 1:
        print('Digite apenas uma letra.')

    if opcao == 'i':
        os.system('clear')
        item = input('Digite o item: ')
        lista_usuario.append(item)
    elif opcao == 'a':
        if (bool(lista_usuario) is False):
            print('Não há itens para apagar.')
            continue

        indice = input('Escolha o índice para apagar: ')

        try:
            item_apagado = lista_usuario[int(indice)]
            print(f'O item: "{item_apagado}", foi deletado com sucesso!')
            del item_apagado
        except ValueError:
            print('Por favor digite um número inteiro.')
        except IndexError:
            print('Índice não existe na lista.')
        except:
            print('Erro desconhecido')

    elif opcao == 'l':
        os.system('clear')

        if bool(lista_usuario) is False:
            print('Nada para listar')

        for idx, item in enumerate(lista_usuario):
            print(idx, item)
    else:
        print('Opção inválida.')
