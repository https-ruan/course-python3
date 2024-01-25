# Try, except, else e finally

""" try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    # c = a / b
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome não está definido.')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('NOME:', error.__class__.__name__)
except Exception:
    print('Erro desconhecido.') """


try:
    print('ABRIR ARQUIVO')
except:
    ...
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')  # Executa independente do resultado
