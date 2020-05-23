BASE = 10


def readNumber():
    string = input()
    number = []
    for char in string:
        number.insert(0, int(char))
    return number


def printNumber(number):
    for digit in number:
        print(number)


def getCarry(result):
    return result // BASE


def getResult(result):
    return result % BASE


def toString(number):
    string = ""
    while len(number) > 0:
        string += str(number.pop())
    return string


def printNumber(number):
    print(toString(number))


def infinitySum(num1, num2):
    result = []
    i = 0
    carry = 0
    parcial = 0
    while i < len(num1) and i < len(num2):
        parcial = num1[i] + num2[i] + carry
        result.append(getResult(parcial))
        carry = getCarry(parcial)
        i += 1

    while i < len(num1):
        parcial = num1[i] + carry
        result.append(getResult(parcial))
        carry = getCarry(parcial)
        i += 1

    while i < len(num2):
        parcial = num2[i] + carry
        result.append(getResult(parcial))
        carry = getCarry(parcial)
        i += 1

    if carry > 0:
        result.append(carry)

    return result


def infinitySubtraction(num1, num2):
    result = []
    i = 0
    carry = 0
    parcial = 0
    while i < len(num1) and i < len(num2):
        parcial = num1[i] - num2[i] - carry
        if parcial < 0:
            parcial += BASE
            carry = 1
        else:
            carry = 0
        result.append(parcial)
        i += 1

    while i < len(num1):
        parcial = num1[i] - carry
        if parcial < 0:
            parcial += BASE
            carry = 1
        else:
            carry = 0
        result.append(parcial)
        i += 1

    return result


def infinityCalculator():
    firstNumber = readNumber()
    seconNumber = readNumber()

    sumResult = infinitySum(firstNumber, seconNumber)
    print('Soma')
    printNumber(sumResult)

    subtractionResult = infinitySubtraction(firstNumber, seconNumber)
    print('Subtração')
    printNumber(subtractionResult)

    # productResult = infinityMultiplication(firstNumber, seconNumber)

    # quotientResul = infinityDivision(firstNumber, seconNumber)

    # print('Multiplicação')
    # printNumber(productResult)

    # print('Divuisão')
    # printNumber(quotientResul)


if __name__ == "__main__":
    infinityCalculator()
