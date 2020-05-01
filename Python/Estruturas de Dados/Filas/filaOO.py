class Pessoa:
    def __init__(self, nome, prioridade=0):
        self.nome = nome
        self.prioridade = prioridade


class FilaPrioritaria:
    def __init__(self):
        self.fila = []

    def remove(self):
        if not self.fila.isEmpty():
            return self.fila.pop(0)

    def isEmpty(self):
        return not len(self.fila) > 0


class filaComum:
    def __init__(self):
        self.fila = []

    def remove(self):
        if not self.fila.isEmpty():
            return self.fila.pop(0)

    def isEmpty(self):
        return not len(self.fila) > 0


class Fila:
    def __init__(self):
        self.filaComum = []
        self.filaPrioritaria = []

    def insere(self, nome, prioridade=0):
        if prioridade == 0:
            self.filaComum.append(Pessoa(nome, prioridade))
        elif prioridade == 1:
            self.filaPrioritaria.append(Pessoa(nome, prioridade))
        else:
            print('Prioridade Inválida')

    def chamaPessoa(self):
        if len(self.filaPrioritaria) > 0:
            print('Atendendo:', self.filaPrioritaria.pop(0).nome)
            self.imprimeFila()

        elif len(self.filaComum) > 0:
            print('Atendendo', self.filaComum.pop(0).nome)
            self.imprimeFila()

        else:
            print('Fila vazia :/')

    def imprimeFila(self):
        for pessoa in self.filaPrioritaria:
            print('nome:', pessoa.nome)

        for pessoa in self.filaComum:
            print('nome:', pessoa.nome)


if __name__ == "__main__":
    fila = Fila()
    for i in range(10):
        fila.insere('roger'+str(i))

    for i in range(3):
        fila.insere('Altair'+str(i), 1)

    for i in range(10):
        print('-'*20)
        fila.chamaPessoa()
    
