def pares(lista):
    if len(lista) == 1:
        return 1 if lista[0] % 2 == 0 else 0
    else:
        n = pares(lista[1:])
        return n+1 if lista[0] % 2 == 0 else n

if __name__ == "__main__":
    lista = [int(i) for i in input().split()]
    print(pares(lista))
    