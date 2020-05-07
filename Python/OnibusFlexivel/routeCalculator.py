from math import sqrt
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


if __name__ == "__main__":
    path = [(0, 0), (2, 2), (5, 4), (6, 3), (8, 3), (10, 10)]
    passangers = [(5, 2), (6, 2), (4, 5), (7, 6), (8, 6)]
    print(calculateBestRoute(path))
