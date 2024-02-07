# @property + @setter - getter e setter no modo Pythonico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começam com um ou dois underlines não devem ser usados fora da classe
class Caneta:
    def __init__(self, cor):
        # private - protected - public
        self._cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('PROPERTY')
        return self._cor

    @cor.setter
    def cor(self, nova_cor):
        print('ESTOU NO SETTER')
        self._cor = nova_cor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, nova_cor):
        self._cor_tampa = nova_cor


caneta = Caneta('Azul')
# getter -> obter valor
print(caneta.cor)
print(caneta.cor_tampa)
# setter -> alterar valor
caneta.cor = 'Vermelha'
caneta.cor_tampa = 'Preta'
print(caneta.cor)
print(caneta.cor_tampa)
