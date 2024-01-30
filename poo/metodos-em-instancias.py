# Métodos em instâncias de classes python
class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

    def frear(self):
        print(f'{self.nome} está freando...')


carro = Carro('Fusca')
print(carro.nome)
carro.acelerar()
carro.frear()
