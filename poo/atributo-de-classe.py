# Atributos de classe


class Pessoa:
    ANO_ATUAL = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ANO_ATUAL - self.idade


# Pessoa.ANO_ATUAL = 2024

p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)
print(Pessoa.ANO_ATUAL)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
