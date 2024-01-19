""" 
Cuidados com dados mutáveis
= -> copiado o valor (imutáveis)
= -> aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Ruan'
# noutra_variavel = nome
# nome = 'João'
# print(nome)
# print(noutra_variavel)

lista_a = ['Ruan', 'Maria']
lista_b = lista_a.copy()

print(id(lista_a))
print(id(lista_b))
lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
