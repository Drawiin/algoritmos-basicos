def maior(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        m = maior(lista[1:])
        return m if m > lista[0] else lista[0]

if __name__ == "__main__":
    lista = [int(i) for i in input().split()]
    print(f"O mnaior número é {maior(lista)}")