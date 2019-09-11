def soma(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma(lista[1:])

if __name__ == "__main__":
    lista = [int(i) for i in input().split()]
    print(soma(lista))
    