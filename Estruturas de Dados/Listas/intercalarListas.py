def intercalaEmOrdem(lista1, lista2):
    intercalada = []
    lista1.sort()
    lista2.sort()

    while len(lista1) > 0 and len(lista2) > 0:
        if lista1[0] < lista2[0]:
            intercalada.append(lista1.pop(0))
        else:
            intercalada.append(lista2.pop(0))

    if len(lista1) > 0:
        intercalada += lista1
    if len(lista2) > 0:
        intercalada += lista2

    return intercalada


lista1 = [2, 4, 6, 8, 10]
lista2 = [1, 3, 5, 7, 9]

print(intercalaEmOrdem(lista1, lista2))
