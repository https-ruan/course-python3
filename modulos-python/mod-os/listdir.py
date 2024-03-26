# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('C:\\Users', 'Ruan', 'OneDrive', 'Desktop')

for item in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, item)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for item2 in os.listdir(caminho_completo_pasta):
        print(item2)
