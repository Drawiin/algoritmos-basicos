ABS_FREQUENCY = 0
RELATIVE_FREQUENCY = 1

class Cell:
    def __init__(self, name):
        self.name = name
        self.values = [0, 0]

    def add(self, value):
        self.values[0] += value

    def show(self):
        print(f"{self.name}    {self.values[ABS_FREQUENCY]}{' '*21}{self.values[RELATIVE_FREQUENCY]}")

class Table:
    def __init__(self, rows=[]):
        self.rows = []
        self.__setTable(rows)
    
    def __setTable(self, rows):
        for i in rows:
            self.rows.append(Cell(i))



    def addOcurrence(self, id, value):
        self.rows[self.findId(id)].add(value)

    def findId(self, id):
        pass

    def show(self):
        print('NAME FREQUÊNCIA ABSOLUTA  FREQUÊNCIA RELATIVA')
        for i in self.rows:
            i.show()


if __name__ == "__main__":
    table = Table(['A', 'B', 'C'])
    table.show()

