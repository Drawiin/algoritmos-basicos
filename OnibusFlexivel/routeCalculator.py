from math import sqrt
from math import factorial
from itertools import permutations
import os


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
    print('')
    print('+----------------------------------------------+')
    print('|                                              |')
    print('|   Pressione Enter para começar               |')
    print('|                                              |')
    print('+----------------------------------------------+')
    input('')

    print('+----------------------------------------------+')
    print('|                                              |')
    print('| Quantos pontos o caminho do ônibus tem ?     |')
    print('|                                              |')
    print('+----------------------------------------------+')
    pathLength = int(input('>'))
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('+----------------------------------------------+')
    print('|                                              |')
    print('| Quantos pontos de passageiros tem ?          |')
    print('|                                              |')
    print('+----------------------------------------------+')
    passangersLength = int(input('>'))

    os.system('cls' if os.name == 'nt' else 'clear')
    print('+----------------------------------------+')
    print('|                                        |')
    print('| Entre com os pontos da rota do ônibus  |')
    print('|                                        |')
    print('+----------------------------------------+')
    print('| | | | | | | | | | | | | | | | | | | | | ')
    print('V V V V V V V V V V V V V V V V V V V V V ')
    print('')
    path = [readPoint(i) for i in range(pathLength)]

    os.system('cls' if os.name == 'nt' else 'clear')
    print('+----------------------------------------------+')
    print('|                                              |')
    print('| Entre com os pontos da rota dos passageiros  |')
    print('|                                              |')
    print('+----------------------------------------------+')
    print('| | | | | | | | | | | | | | | | | | | | | | | | ')
    print('V V V V V V V V V V V V V V V V V V V V V V V V ')
    print('')
    passangers = [readPoint(i) for i in range(passangersLength)]

    os.system('cls' if os.name == 'nt' else 'clear')
    print('+----------------------------------------------+')
    print('|                                              |')
    print('|         pontos do caminho do ônibus          |')
    print('|                                              |')
    print('+----------------------------------------------+')
    print('| | | | | | | | | | | | | | | | | | | | | | | | ')
    print('V V V V V V V V V V V V V V V V V V V V V V V V ')
    print('')
    print(path)
    
    print('')
    print('+----------------------------------------------+')
    print('|                                              |')
    print('|         pontos de passageiros                |')
    print('|                                              |')
    print('+----------------------------------------------+')
    print('| | | | | | | | | | | | | | | | | | | | | | | | ')
    print('V V V V V V V V V V V V V V V V V V V V V V V V ')
    print('')
    print(passangers)

    print('')
    print('+----------------------------------------------+')
    print('|                                              |')
    print('|   Pressione Enter para continuar             |')
    print('|                                              |')
    print('+----------------------------------------------+')
    input('')

    route = path + passangers

    if(len(route) > 8):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('+--------------------------------------------------------------------+')
        print('|                                                                    |')
        print('|    A rota que você está prestes a calcular contem vários pontos    |')
        print('|    isso pode levar vários minutos........ou anos                   |')
        print('|    pressione Enter para continuar                                  |')
        print('|                                                                    |')
        print('+--------------------------------------------------------------------+')
        input('')

    os.system('cls' if os.name == 'nt' else 'clear')
    print('calculando todas as', factorial(len(route)), 'rotas possiveis.................')
    result = calculateBestRoute(route)
    print('+----------------------------------------------+')
    print('|                                              |')
    print('| A melhor rota encontrada foi                 |')
    print('|                                              |')
    print('+----------------------------------------------+')
    print('| | | | | | | | | | | | | | | | | | | | | | | | ')
    print('V V V V V V V V V V V V V V V V V V V V V V V V ')
    print('')
    print(result[0])
    print('')
    print('Com custo de ')
    print(result[1])

    print('')
    print('+----------------------------------------------+')
    print('|                                              |')
    print('|   Pressione Enter para Para Encerrar         |')
    print('|                                              |')
    print('+----------------------------------------------+')
    input('')
