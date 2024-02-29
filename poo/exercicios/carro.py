# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
fusca.fabricante = volkswagen
motor_1_0 = Motor('1.0')
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

uno = Carro('Uno')
fiat = Fabricante('Fiat')
uno.fabricante = fiat
motor_1_0 = Motor('1.0')
uno.motor = motor_1_0
print(uno.nome, uno.fabricante.nome, uno.motor.nome)

focus = Carro('Focus')
ford = Fabricante('Ford')
focus.fabricante = ford
motor_2_0 = Motor('2.0')
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)
