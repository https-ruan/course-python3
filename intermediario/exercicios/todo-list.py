# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
lista_tarefas = []
lista_desfeitos = []


def listar():
    print()
    
    if not lista_tarefas:
        print('Nenhuma tarefa para listar')
        print()
        return
    
    print('TAREFAS:')
    print(*lista_tarefas, sep='\n')
    print()
    
def desfazer():
    print()
    
    if not lista_tarefas:
        print('Nada a desfazer')
        print()
        return
        
    lista_desfeitos.append(lista_tarefas.pop())
    listar()
        
def refazer():
    if not lista_desfeitos:
        print()
        print('Nada a refazer')
        print()
        return
    
    lista_tarefas.append(lista_desfeitos.pop(0))
    listar()
    
def adicionar(tarefa):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        print()
        return
    
    lista_tarefas.append(tarefa)
    listar()

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou comando: ') 
    
    comandos = {
        'listar': lambda: listar(),
        'desfazer': lambda: desfazer(),
        'refazer': lambda: refazer(),
        'adicionar': lambda: adicionar(tarefa)
    }
    
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
    comando()
     
    # if comando == 'listar':
    #     listar()
    #     continue
    # elif comando == 'desfazer':
    #     desfazer()  
    #     continue
    # elif comando == 'refazer':
    #     refazer()
    #     continue
    # else:
        # adicionar(comando)
        # continue