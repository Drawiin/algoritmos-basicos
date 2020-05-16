def empilhaExpressao(expressao):
    operadores = ['/', '*']
    pilha = []
    for i in expressao:
        if i.isnumeric():
            if len(pilha) > 0:
                if len(pilha) > 0 and pilha[-1].isnumeric():
                    pilha[-1] += i
                else:
                    if pilha[-1] in operadores:
                        if pilha[-1] == '*':
                            pilha.pop()
                            pilha[-1] = str(int(pilha[-1]) * int(i))
                        if pilha[-1] == '/':
                            pilha.pop()
                            pilha[-1] = str(int(pilha[-1]) // int(i))
                    else:
                        pilha.append(i)
            else:
                pilha.append(i)
        elif i != ')':
            pilha.append(i)
        else:
            pilha = resolveParenteses(pilha)
            novoTopo = pilha.pop()
            if pilha[-1] in operadores:
                if pilha[-1] == '*':
                    pilha.pop()
                    pilha[-1] = str(int(pilha[-1]) * int(novoTopo))
                if pilha[-1] == '/':
                    pilha.pop()
                    pilha[-1] = str(int(pilha[-1]) // int(novoTopo))
            else:
                pilha.append(novoTopo)
    return pilha


def desempilhaExpressao(pilha):
    acumulador = 0
    if len(pilha) == 1:
        return int(pilha[-1])
    while len(pilha) > 0:
        topoDaPilha = pilha.pop()
        if topoDaPilha.isnumeric():
            if pilha[-1] == '+':
                pilha.pop()
                acumulador += int(topoDaPilha) + int(pilha.pop())
            else:
                pilha.pop()
                acumulador += int(pilha.pop()) - int(topoDaPilha) 
        else:
            if topoDaPilha == '+':
                acumulador += int(pilha.pop())
            if topoDaPilha == '-':
                acumulador -= int(pilha.pop())
    return acumulador


def resolveParenteses(pilha):
    expressao = ''
    while pilha[-1] != '(':
        expressao += pilha.pop()
    pilha[-1] = str(desempilhaExpressao(empilhaExpressao(expressao)))
    return pilha


pilha = empilhaExpressao(input())
resultado = desempilhaExpressao(pilha)

print(resultado)
