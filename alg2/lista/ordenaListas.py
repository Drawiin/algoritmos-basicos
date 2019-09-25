def mesclaListas(lista1, lista2):
    lista1.sort()
    lista2.sort()
    listaMesclada = []
    i = 0
    for i in lista2:
        if lista1[0] < i:
            listaMesclada.append(lista1.pop(0))

    for i in lista1:
        if lista2[0] < i:
            listaMesclada.append(lista2.pop(0))

    print(lista1, lista2)

    return listaMesclada


lista1 = [int(i) for i in input().split()]
lista2 = [int(i) for i in input().split()]
listaNova = mesclaListas(lista1, lista2)


print(listaNova)
