""" 
Repetiçõews
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim

break -> finaliza o laço de repetição
continue -> pula o restante do bloco do laço e retorna ao inicio
"""

""" contador = 0

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
"""

# * While com while
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1

    linha += 1

print('Acabou')
