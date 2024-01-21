""" 
split e join com list e str
slip -> divide uma string (list)
join -> une uma string
strip -> remove os espaços do inicio e do fim das strings (se tiver)
"""
frase = 'Olha só que, coisa interessante'
lista_palavras = frase.split(',')
print(lista_palavras)

frases_unidas = '-'.join(lista_palavras)
print(frases_unidas)
