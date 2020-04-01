def menu():
    print('''
    1- converter decimal para binário
    2- converter binario para decimal
    3- converter decimal para hexadecimal
    4- converter hexadecimal para decimal
    5- sair
    ''')
    op = int(input())
    return op


def decBinario(n):
    numeroBinario = ''
    while n != 0:
        numeroBinario += str(n%2)
        n = n // 2 
    return numeroBinario[::-1]


def binarioDecimal(n):
    numeroDecimal = 0
    n = n[::-1]
    for i in range(len(n)):
        if n[i] == '1':
            numeroDecimal += 2 ** i
    return numeroDecimal


def decHexa(n):
    hex = [0,1,2,3,4,5,6,7,8,9, 'A', 'B', 'C', 'D', 'E', 'F']
    r = ''
    while n > 0:
        r += (str(hex[n%16]))
        n = n //16
    return r[::-1]


def hexaDec(n):
    numeroDecimal = 0
    hex = ['0','1','2','3','4','5','6','7','8','9', 'A', 'B', 'C', 'D', 'E', 'F']
    n = n[::-1]
    for i in range(len(n)):
        numeroDecimal +=  hex.index(n[i]) * 16 ** i
    return numeroDecimal



op = menu()
while op != 5:
    if op == 1:
        n = int(input('digite um numero decimal'))
        print(decBinario(n))
        op = menu()
    elif op == 2:
        n = input('digite um numero binário')
        print(binarioDecimal(n))
        op = menu()
    elif op == 3:
        n = int(input('digite um numero decimal'))
        print(decHexa(n))
        op = menu()
    elif op == 4:
        n = input('digite um numero hexadecimal')
        print(hexaDec(n))
        op = menu()
    else:
        op = 5 