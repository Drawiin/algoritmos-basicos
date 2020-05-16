import heapq


def compression(data):
    key = dict()
    encoded = str()
    corp = dict()

    for char in data:
        corp[char] = corp.get(char, 0) + 1

    print(corp)


if __name__ == "__main__":
    data = 'ABRACADABRA!'
    compression(data)
