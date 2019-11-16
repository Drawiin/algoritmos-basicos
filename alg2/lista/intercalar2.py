lista1 = [int(i) for i in input().split()]
lista2 = [int(i) for i in input().split()]
listaIntercalada = []
lista1.sort()
lista2.sort()
i, j = 0, 0

while i < len(lista1) and j < len(lista2):
    if lista1[i] < lista2[j]:
        listaIntercalada.append(lista1[i])
        i += 1
    else:
        listaIntercalada.append(lista2[i])
        j += 1

while i < len(lista1):
    listaIntercalada.append(lista1[i])
    i += 1

while j < len(lista2):
    listaIntercalada.append(lista2[j])
    j += 1

print(listaIntercalada)
