from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo=0.0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float): ...

    def depositar(self, valor: float):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO: {valor: .2f})')

    def detalhes(self, msg=''):
        print(f'O seu saldo é: {self.saldo:.2f} {msg}')
        print('-' * 50)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class Poupanca(Conta):
    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE: {valor: .2f})')
            return

        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO: {valor: .2f})')


class Corrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE: {valor: .2f})')
            return

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {limite_maximo: .2f}')
        self.detalhes(f'(SAQUE NEGADO: {valor: .2f})')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, '\
            f'{self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    cc1 = Poupanca(111, 222)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    print('#' * 50)
    cc1 = Corrente(111, 222, limite=100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(100)
    cc1.sacar(1)
