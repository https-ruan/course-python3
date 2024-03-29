# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass, asdict, astuple, field, fields


@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome

    def __post_init__(self):  # Executa após init da dataclass (se habilitado)
        print('Pós init')
        self.nome_completo = f'{self.nome} {self.sobrenome}'

    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'

    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = sobrenome


@dataclass(frozen=True)
class PessoaCongelada:
    nome: str = field(
        default='Missing',
    )
    sobrenome: str = 'Not sent'
    idade: int = 0
    lista: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa('Ruan', 'Araujo')
    p1.nome_completo = 'Maria Helena'
    print(p1)
    print(p1.nome_completo)

    p2 = PessoaCongelada()
    # p2.nome = 'X'
    print(p2)

    print(asdict(p1))
    print(astuple(p2))
    print(fields(p1))
