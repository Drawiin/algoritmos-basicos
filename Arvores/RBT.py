class Node:
    RED = True
    BLACK = False

    def __init__(self, key, color=RED):
        if not type(color) == bool:
            raise TypeError(
                "Valor de cor do nó incorreto esperado True/False e foi passado", color)
        self.color = color
        self.key = key
        self.left = NilNode.instance()
        self.right = NilNode.instance()
        self.parent = NilNode.instance()

    def __nonzero__(self):
        return True

    def __bool__(self):
        return True


class NilNode(Node):
    __instance__ = None

    @classmethod
    def instance(self):
        if self.__instance__ is None:
            self.__instance__ = NilNode()
        return self.__instance__

    def __init__(self):
        self.color = Node.BLACK
        self.key = None
        self.left = None
        self.right = None
        self.parent = None

    def __nonzero__(self):
        return False

    def __bool__(self):
        return False


class RBT:
    def __init__(self):
        self.root = NilNode.instance()
        self.size = 0

    def __add(self, key):
        self.__insert(Node(key))

    def __insert(self, x):
        # insere o nó na arvore
        self.__insertHelper(x)

        while x != self.root and x.parent.color == Node.RED:
            # se o pai for filho a esquerda do avô
            if x.parent == x.parent.parent.left:
                # y é o tio
                y = x.parent.parent.right
                # Tio vermelho Inverte
                if y and y.color == Node.RED:
                    x.parent.color = Node.BLACK
                    y.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    print("!!!Recolorindo P[{}] P[{}] V[{}]".format(x.parent.key, y.key, x.parent.parent.key))
                    # passa a responsa pro avô
                    x = x.parent.parent
                # tio preto rotaciona
                else:
                    if x == x.parent.right:
                        x = x.parent
                        self.__leftRotate(x)
                    x.parent.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    self.__rightRotate(x.parent.parent)
            else:
                y = x.parent.parent.left
                if y and y.color == Node.RED:
                    x.parent.color = Node.BLACK
                    y.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    x = x.parent.parent
                else:
                    if x == x.parent.left:
                        x = x.parent
                        self.__rightRotate(x)
                    x.parent.color = Node.BLACK
                    x.parent.parent.color = Node.RED
                    self.__leftRotate(x.parent.parent)
        self.root.color = Node.BLACK

    def __leftRotate(self, x):
        if not x.right:
            raise "x.right é nullo!"
        y = x.right
        x.right = y.left
        if y.left:
            y.left.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        print("[Rotação a esquerda de {} ao redor de {}]".format(x.key, y.key))
        y.left = x
        x.parent = y

    def __rightRotate(self, x):
        if not x.left:
            raise "x.left is nil!"
        y = x.left
        x.left = y.right
        if y.right:
            y.right.parent = x
        y.parent = x.parent
        if not x.parent:
            self.root = y
        else:
            if x == x.parent.left:
                x.parent.left = y
            else:
                x.parent.right = y
        print("[Rotação a direita de {} ao redor de {}]".format(x.key, y.key))
        y.right = x
        x.parent = y

    def __insertHelper(self, z):
        ''' Insere um nó na árvore '''
        y = NilNode.instance()
        x = self.root
        # anda até um nó folha
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        # seta o pai do nó que vai ser inserido
        z.parent = y
        # se a arvore etiver vazia o nó a ser inserido vira a raiz
        if not y:
            self.root = z
            print("--->inserindo {} na raiz".format(z.key))
        # se a árvore não for vazia ele verifica se o nó será inserido na esquerda ou na direita
        else:
            if z.key < y.key:
                y.left = z
                print("--->Inserindo {} a esquerda de {}".format(z.key, y.key))
            else:
                y.right = z
                print("--->Inserindo {} a direita de {}".format(z.key, y.key))

        self.size += 1

    def insere(self, key):
        self.__add(key)

    def insereVetor(self, array):
        for i in array:
            self.insere(i)

    def emOrdem(self):
        self.__inOrder(self.root)

    def __inOrder(self, node):
        if not node:
            print("@", end="")
        else:
            print("(", end="")
            self.__inOrder(node.left)
            print(node.key, end="")
            self.__inOrder(node.right)
            print(")", end="")

    def preOrdem(self):
        self.__preOrder(self.root)

    def __preOrder(self, node):
        if not node:
            print("@", end="")
        else:
            print("(", end="")
            print(node.key, end="")
            self.__preOrder(node.left)
            self.__preOrder(node.right)
            print(")", end="")

    def posOrdem(self):
        self.__preOrder(self.root)

    def __posOrder(self, node):
        if not node:
            print("@", end="")
        else:
            print("(", end="")
            print(node.key, end="")
            self.__posOrder(node.left)
            self.__posOrder(node.right)
            print(node.key, end="")
            print(")", end="")



if __name__ == "__main__":
    tree = RBT()
    numbers = [1,2,3,4,5,6,7,8,9,10]
    tree.insereVetor(numbers)
    print("\n","="*20,"Em Ordem","="*20, end="\n\n")
    tree.emOrdem()
    print("\n", "="*20,"Pré Ordem","="*20, end="\n\n")
    tree.preOrdem()
    print("\n", "="*20,"Pós Ordem","="*20, end="\n\n")
    tree.posOrdem()

