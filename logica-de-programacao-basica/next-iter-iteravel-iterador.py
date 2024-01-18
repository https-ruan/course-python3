""" 
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
"""

# texto = iter('Ruan')  # __iter__()
# print(next(texto))  # __next__()
# print(next(texto))  # __next__()
# print(next(texto))  # __next__()
# print(next(texto))  # __next__()

# for letra in texto
texto = 'Ruan'  # iteravel
iterador = iter(texto)  # iterador

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
