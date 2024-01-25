import modulos
import importlib
print(modulos.variavel_modulo)

for i in range(10):
    importlib.reload(modulos)
    print(i)

print('Fim')
