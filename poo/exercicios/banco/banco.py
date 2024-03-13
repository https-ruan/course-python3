from contas import Conta, Corrente, Poupanca
from pessoas import Cliente, Pessoa


class Banco:
    def __init__(
        self,
        agencias: list[int] = [],
        clientes: list[Cliente] = [],
        contas: list[Conta] = [],
    ):
        self.agencias = agencias
        self.clientes = clientes
        self.contas = contas

    def _chega_agencia(self, conta: Conta):
        if conta.agencia in self.agencias:
            print(Banco._chega_agencia.__name__, True)
            return True
        print(Banco._chega_agencia.__name__, False)
        return False

    def _chega_cliente(self, cliente: Pessoa):
        if cliente in self.clientes:
            print(Banco._chega_cliente.__name__, True)
            return True
        print(Banco._chega_cliente.__name__, False)
        return False

    def _chega_conta(self, conta: Conta):
        if conta in self.contas:
            print(Banco._chega_conta.__name__, True)
            return True
        print(Banco._chega_conta.__name__, False)
        return False

    def _checa_se_conta_e_do_cliente(self,  cliente: Cliente, conta: Conta,):
        if conta is cliente.conta:
            print(Banco._checa_se_conta_e_do_cliente.__name__, True)
            return True
        print(Banco._checa_se_conta_e_do_cliente.__name__, False)
        return False

    def autenticar(self, cliente: Cliente, conta: Conta):
        return self._chega_agencia(conta) and \
            self._chega_conta(conta) and \
            self._chega_cliente(cliente) and \
            self._checa_se_conta_e_do_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'


if __name__ == '__main__':
    c1 = Cliente('Ruan', 22)
    cc1 = Corrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = Cliente('Maria', 18)
    cp1 = Poupanca(222, 333, 100)
    c2.conta = cp1

    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)
