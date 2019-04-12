'''
    Essa implementação usa R-L para
    calcular o fator de balanceamento
'''


class Node():
    '''
        essa é a classe nó ela é a nossa unidade básica de construção
    '''
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


class AVL():
    '''
            Classe AVL ela é a árvore em si
    '''
    def __init__(self):
        self.node = None
        self.hight = -1
        self.balance = 0

    def insert(self, key):
        '''
            Insere um elemnto na árvore
        '''
        # se a sub-árvore for vazia insere nela
        if self.node is None:
            self.node = Node(key)
            self.node.left = AVL()
            self.node.right = AVL()
            print("inserindo ", key)
        # se ela não for continua na busca para inserção binária
        else:
            if key < self.node.key:
                self.node.left.insert(key)
            elif key > self.node.key:
                self.node.right.insert(key)
            else:
                print("Elemento já está na árvore")

        self.rebalance()

    def isDesbalance(self):
        '''
            Verifica se uma sub-árvore está desbalanceada
        '''
        if abs(self.balance) > 1:
            return True
        else:
            return False

    def rebalance(self):
        '''
            Rebalanceia a árvore
        '''
        # atualiza a aultura e o fator de balanceamento
        self.updadateHight(False)
        self.updateBalance(False)
        # verifica se está desbalanceada
        while self.isDesbalance():
            # verifica se está desbalanceada a esquerda
            if self.balance < -1:
                # verifica se é um desbalanceamento esquerda direita
                if self.node.left.balance > 0:
                    self.node.left.leftRotate()
                    self.updadateHight()
                    self.updateBalance()
                self.rightRotate()
                self.updadateHight()
                self.updateBalance()

            # verifica se está desbalanceada a direita
            if self.balance > 1:
                # verifica se é um desbalanceamento direita esquerda
                if self.node.right.balance < 0:
                    self.node.right.rightRotate()
                    self.updadateHight()
                    self.updateBalance()
                self.leftRotate()
                self.updadateHight()
                self.updateBalance()

    def rightRotate(self):
        '''
            Realiza a rotação a direita
        '''
        # Rotação a direita de A ao redor de B
        A = self.node
        B = self.node.left.node
        T = B.right.node
        print("Rotação a direita de ", A.key, " ao redor de ", B.key)
        self.node = B
        B.right.node = A
        A.left.node = T

    def leftRotate(self):
        '''
            Realisa a rotação a esquerda
        '''
        # rotação a esquerda de A ao redor de B
        A = self.node
        B = self.node.right.node
        T = B.left.node
        print("Rotação a esquerda de ", A.key, " Ao redor de ", B.key)
        self.node = B
        B.left.node = A
        A.right.node = T

    def updadateHight(self, recurse=True):
        '''
            Calcula a altura de um árvore ou sub-árvore
        '''
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.updadateHight()
                if self.node.right is not None:
                    self.node.right.updadateHight()
            # calcula a altura da árvore
            self.hight = max(self.node.left.hight,
                             self.node.right.hight) + 1
        # se a sub árvore for vazia a sua altura é -1
        else:
            self.hight = -1

    def updateBalance(self, recurse=True):
        '''
            Atualiza o fator de balanceamento da árvore
        '''
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.updateBalance()
                if self.node.right is not None:
                    self.node.right.updateBalance()

            self.balance = self.node.right.hight - self.node.left.hight
        # se a subárvore for vazia seu fator de balanceamento é 0
        else:
            self.balance = 0

    def delete(self, key):
        if self.node is not None:
            print("tentando deletar no nó ", self.node.key)
            if self.node.key == key:
                print("deletando o nó ", key)
                # verifica se é um nó folha
                if self.node.left.node is None and self.node.right.node is None:
                    self.node = None

                # verifica se tem apenas uma sub-árvore
                elif self.node.left.node is None:
                    self.node = self.node.right.node
                elif self.node.right.node is None:
                    self.node = self.node.left.node

                # verifica se o nó tem duas sub-árvores
                else:
                    replacement = self.logicalSuccessor(self.node)
                    if replacement is not None:
                        print("sucessor lógico achado ", key, " -> ", replacement.key)
                        self.node.key = replacement.key 

                        # subistituiu agora deleta
                        print("deletando o sucessor")
                        self.node.right.delete(replacement.key)

                # faz o rebalanceamento
                self.rebalance()
                return
            # se não achou o nó continua procurando
            elif key < self.node.key:
                self.node.left.delete(key)
            elif key > self.node.key:
                self.node.right.delete(key)
            else:
                print("nó", key, "não encontrado")

            self.rebalance()
        else:
            return

    def logicalSuccessor(self, node):
        '''
            Acha o sucessor lógico do nó a ser removido
        '''
        node = node.right.node
        if node is not None:
            # procura o sucessor
            while node.left is not None:
                print("Procurando o sucessor de", node.key)
                if node.left.node is None:
                    return node
                else:
                    node = node.left.node
        return node

    def show(self):
        self.inOrder(self.node)
        pass

    def inOrder(self, node):
        if node is not None:
            print("(", end="")
            print(node.key, end="")
            self.inOrder(node.left.node)
            self.inOrder(node.right.node)
            print(")", end="")
        print('.', end="")
        pass


if __name__ == "__main__":
    numbers = [22, 10, 36, 44, 33, 46, 45, 13, 1]
    tree = AVL()
    for i in numbers:
        tree.insert(i)
        print("=="*20)
    tree.show()
    numbers = [33, 1, 0, 2, 46]
    for i in numbers:
        tree.delete(i)
        print("=="*20)
    tree.show()

    pass
