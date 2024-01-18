""" 
Repetiçõews
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

break -> finaliza o laço de repetição
continue -> pula o restante do bloco do laço e retorna ao inicio
"""

contador = 0

while contador < 100:
    contador += 1

    if contador == 6:
        print('Não vou mostrar o 6.')
        continue

    if contador >= 10 and contador <= 27:
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')
