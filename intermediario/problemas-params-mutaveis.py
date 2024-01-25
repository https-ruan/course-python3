# Problemas dos parâmetros mutáveis em funções
def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
        
    lista.append(nome)
    return lista

clientes1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', clientes1)
print(clientes1)

clientes2 = adiciona_clientes('ruan')
print(clientes2)
