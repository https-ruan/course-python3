# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

class A:
    atributo_a = 'valor'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('EI, burlei o sistema.')

    def metodo(self):
        super().metodo()  # B
        super(B, self).metodo()  # A
        # super(A, self).metodo()  # object
        print('C')


c = C('Atributo C', 'Outra coisa')

# print('A mro ->', A.mro())
# print('B mro ->', B.mro())
# print('C mro->', C.mro())

# print(c.atributo_c)
print(c.atributo)
print(c.outra_coisa)
# c.metodo()
