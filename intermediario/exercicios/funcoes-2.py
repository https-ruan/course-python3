""" 
 Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""


def multiplicador(valor):
    def multiplicar(numero):
        return valor * numero

    return multiplicar


duplica = multiplicador(2)
triplica = multiplicador(3)
quadruplica = multiplicador(4)

print(duplica(2))
print(triplica(2))
print(quadruplica(2))
