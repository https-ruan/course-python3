from contas import Conta, Corrente, Poupanca


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: Conta | None = None


if __name__ == '__main__':
    c1 = Cliente('Ruan', 22)
    c1.conta = Corrente(1, 2)
    print(c1)
    print(c1.conta)
    c2 = Cliente('Maria', 19)
    c2.conta = Corrente(2, 3, 100, 50)
    print(c2)
    print(c2.conta)
