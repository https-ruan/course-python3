# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):  # factory method
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):  # factory method
        return cls("Anônima", idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Maria')
p3 = Pessoa.criar_sem_nome(23)
print(p2.idade)
print(p3.nome)
# Pessoa.metodo_de_classe()
