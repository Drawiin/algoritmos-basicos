
class BigDigit():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class BigNum():
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return '0'
        string = ''
        current = self.head
        while current is not None:
            string = f'{current}' + string
            current = current.next
        return string

    def insert(self, value):
        if self.head is None:
            self.head = BigDigit(value)
        else:
            oldHead = self.head
            self.head = BigDigit(value)
            self.head.next = oldHead

    def append(self, value):
        if self.head is None:
            self.head = BigDigit(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = BigDigit(value)

    def readNumber(self):
        number = input().strip()
        if not number.isnumeric():
            print('Somente numeros são permitidos')
            exit(0)
        for digit in number:

            self.insert(int(digit))


class BigNumCalculator():
    def __init__(self):
        self.base = 10

    def sumCarry(self, result):
        return result // self.base

    def sumFinalResult(self, result):
        return result % self.base

    def bigSum(self, number1, number2):
        result = BigNum()
        current1 = number1.head
        current2 = number2.head
        carry = 0
        while current1 is not None and current2 is not None:
            parcialResult = current1.value + current2.value + carry
            carry = self.sumCarry(parcialResult)
            finalResult = self.sumFinalResult(parcialResult)

            result.append(finalResult)
            current1 = current1.next
            current2 = current2.next

        while current1 is not None:
            parcialResult = current1.value + carry
            carry = self.sumCarry(parcialResult)
            finalResult = self.sumFinalResult(parcialResult)

            result.append(finalResult)

            current1 = current1.next

        while current2 is not None:
            parcialResult = current2.value + carry
            carry = self.sumCarry(parcialResult)
            finalResult = self.sumFinalResult(parcialResult)

            result.append(finalResult)

            current2 = current2.next

        if carry > 0:
            result.append(carry)

        return result

    def bigSubtraction(self, number1, number2):


number1 = BigNum()
number2 = BigNum()

number1.readNumber()
number2.readNumber()

calculator = BigNumCalculator()
result = calculator.bigSum(number1, number2)

print(result)


# BASE = 10


# def readNumber():
#     string = input()
#     number = []
#     for char in string:
#         number.insert(0, int(char))
#     return number


# def printNumber(number):
#     for digit in number:
#         print(number)


# def getCarry(result):
#     return result // BASE


# def getResult(result):
#     return result % BASE


# def toString(number):
#     string = ""
#     while len(number) > 0:
#         string += str(number.pop())
#     return string


# def printNumber(number):
#     print(toString(number))


# def infinitySum(num1, num2):
#     result = []
#     i = 0
#     carry = 0
#     parcial = 0
#     while i < len(num1) and i < len(num2):
#         parcial = num1[i] + num2[i] + carry
#         result.append(getResult(parcial))
#         carry = getCarry(parcial)
#         i += 1

#     while i < len(num1):
#         parcial = num1[i] + carry
#         result.append(getResult(parcial))
#         carry = getCarry(parcial)
#         i += 1

#     while i < len(num2):
#         parcial = num2[i] + carry
#         result.append(getResult(parcial))
#         carry = getCarry(parcial)
#         i += 1

#     if carry > 0:
#         result.append(carry)

#     return result


# def infinitySubtraction(num1, num2):
#     result = []
#     i = 0
#     carry = 0
#     parcial = 0
#     while i < len(num1) and i < len(num2):
#         parcial = num1[i] - num2[i] - carry
#         if parcial < 0:
#             parcial += BASE
#             carry = 1
#         else:
#             carry = 0
#         result.append(parcial)
#         i += 1

#     while i < len(num1):
#         parcial = num1[i] - carry
#         if parcial < 0:
#             parcial += BASE
#             carry = 1
#         else:
#             carry = 0
#         result.append(parcial)
#         i += 1

#     return result


# def infinityCalculator():
#     firstNumber = readNumber()
#     seconNumber = readNumber()

#     sumResult = infinitySum(firstNumber, seconNumber)
#     print('Soma')
#     printNumber(sumResult)

#     subtractionResult = infinitySubtraction(firstNumber, seconNumber)
#     print('Subtração')
#     printNumber(subtractionResult)

#     # productResult = infinityMultiplication(firstNumber, seconNumber)

#     # quotientResul = infinityDivision(firstNumber, seconNumber)

#     # print('Multiplicação')
#     # printNumber(productResult)

#     # print('Divuisão')
#     # printNumber(quotientResul)


# if __name__ == "__main__":
#     infinityCalculator()
