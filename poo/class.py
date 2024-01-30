# class - classes são molder para criar novos objetos
# As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.
# Os objetos gerador pela classe podem usar seus dados internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de classes.

# string = 'Ruan'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome='', sobrenome=''):
        self.nome, self.sobrenome = nome, sobrenome


p1 = Pessoa('Ruan', 'Araujo')


print(p1.nome)
print(p1.sobrenome)
