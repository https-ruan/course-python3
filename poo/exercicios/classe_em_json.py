# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
# __dic__ e vars para atributos de instância
import json

CAMINHO = 'D:\\Desenvolvimento\\Git\\course-python3\\poo\\arquivos-criados\\classe-em-json.json'


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 21)
p3 = Pessoa('Joana', 11)
bd = [vars(p1), p2.__dict__, vars(p3)]

if __name__ == '__main__':
    with open(CAMINHO, 'w', encoding='utf8') as arquivo:
        print('FAZENDO DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)
