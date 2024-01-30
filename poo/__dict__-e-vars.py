# __dic__ e vars para atributos de instância


class Pessoa:
    ANO_ATUAL = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ANO_ATUAL - self.idade


p1 = Pessoa('João', 35)
# print(p1.get_ano_nascimento())
p1.__dict__['nome'] = 'alterei'
print(p1.__dict__)
print(vars(p1))
