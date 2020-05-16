import os


def selecionaOpcao():
    print('1 - Quero entrar na fila')
    print('2 - Quem está na fila ?')
    print('3 - Proximo')
    print('4 - Sair')
    op = int(input())
    os.system('clear')
    return op


op = selecionaOpcao()

fila = []
filaPrioritaria = []

while op != 4:
    if op == 1:
        elemeto = input('Quem vai entrar na fila ? ')
        idade = int(input('Informe sua idade: '))
        if idade >= 60:
            filaPrioritaria.append(elemeto)
        else:
            fila.append(elemeto)

    elif op == 2:
        if len(filaPrioritaria) != 0:
            print('Prioritária')
            for i in filaPrioritaria:
                print(i)

        if len(fila) != 0:
            print('Fila Comum')
            for i in fila:
                print(i)
        else:
            print('Não tem ninguem na fila')

    elif op == 3:
        if len(filaPrioritaria) != 0:
            print(filaPrioritaria.pop(0) + ' chegou sua vez de sair da fila')

        elif len(fila) != 0:
            print(fila.pop(0) + ' chegou sua vez de sair da fila')

        else:
            print('Não tem ninguem na fila')

    if op == 4:
        break

    op = selecionaOpcao()
