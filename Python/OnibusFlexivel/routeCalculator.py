from math import sqrt
from math import factorial
from itertools import permutations


def calculateDistance(pointA, pointB):
    deltaX = float((pointA[0] - pointB[0])**2)
    deltaY = float((pointA[1] - pointB[1])**2)
    return sqrt(deltaX + deltaY)


def calculateRouteLength(route):
    routeLength = float(0)
    for index in range(len(route) - 1):
        routeLength += calculateDistance(route[index], route[index + 1])
    return routeLength


def calculateBestRoute(route):
    bestRoute = []
    bestRouteLength = float("inf")
    for permutation in permutations(route):
        currentRouteLenght = calculateRouteLength(permutation)
        if(currentRouteLenght < bestRouteLength):
            bestRoute = list(permutation)
            bestRouteLength = currentRouteLenght
    return (bestRoute, bestRouteLength)


def readPoint(index):
    return tuple([int(i) for i in input('ponto {} entre com x e y separados por espaço: '.format(index + 1)).split(' ')])


if __name__ == "__main__":
    pathLength = int(input('Quantos pontos o caminho do ônibus tem ? '))
    passangersLength = int(input('Quantos pontos de passageiros tem ?'))
    print('Entre com os pontos da rota do ônibus')
    path = [readPoint(i) for i in range(pathLength)]
    print('Entre com os pontos dos passageiros')
    passangers = [readPoint(i) for i in range(passangersLength)]

    print("pontos  da rota do ônibus")
    print(path)

    print("pontos  da rota dos passageiros")
    print(passangers)

    input('Pressione enter para continuar')

    route = path + passangers

    if(len(route) > 8):
        input('A rota que você está prestes a calcular contem vários pontos\nisso pode levar vários minutos ........ ou anos\npressione enter para continuar')
    print('calculando......', factorial(len(route)), 'rotas possiveis')
    result = calculateBestRoute(route)
    print('A melhor rota encontrada foi')
    print(result[0])
    print('Com custo de ')
    print(result[1])
