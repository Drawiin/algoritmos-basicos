exp = input()
pilha = []

exp = exp.replace(" ", "")

for i in exp:
    if i.isalnum():
        if len(pilha) > 0 and pilha[-1].isalnum():
            pilha[-1] += i
        else:
            pilha.append(i)
    elif i == '+' or i == '-' or i == '(':
        pilha.append(i)
    elif i == ')':
        while pilha[-1] != '(':
            pass

print(pilha)
