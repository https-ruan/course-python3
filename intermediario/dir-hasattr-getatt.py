""" 
dir -> trás todos os atributos dentro da string
hasattr -> verifica se o objeto TEM um método x
getattr -> obtém o método de um objeto
"""
string = 'Ruan'
metodo = 'upper'

print(hasattr(string, metodo))
print(getattr(string, metodo)())
