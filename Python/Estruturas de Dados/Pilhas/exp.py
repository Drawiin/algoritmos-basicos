exp = input()
pilha = []

exp = exp.replace(" ", "")

for i in exp:
    if i.isnumeric():
        if len(pilha) > 0 and pilha[-1].isnumeric():
            pilha[-1] += i
        else:
            pilha.append(i)
    elif i == '+' or i == '-' or i == '(':
        pilha.append(i)
    elif i == ')':
        break
        while pilha[-1] != '(':
            pass

print(pilha)
