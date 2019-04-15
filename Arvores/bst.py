class Node:
    def __init__(self, key, dad):
        self.key = key
        self.dad = dad
        self.left = None
        self.right = None
        self.hight = 0
        self.balance = 0


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            print("Inserindo", key, "na raiz")
            self.root = Node(key, self)
            self.calculeBalance(self.root.balance, self.root)
        else:
            self.insertAux(key, self.root)

    def calculeHight(self, node):
        left, right = 0, 0
        if node.left is None and node.right is None:
            pass
        if node.left is not None:
            left = self.calculeHight(node.left) + 1
        if node.right is not None:
            right = self.calculeHight(node.right) + 1
        node.hight = max(left, right)
        node.balance = right - left
        return node.hight

    def calculeBalance(self, hight, node):
        if node.right is not None:
            right = node.right.hight + 1
        else:
            right = 0
        if node.left is not None:
            left = node.left.hight + 1
        else:
            left = 0

        if node.dad != self :
            node.hight = max(hight, node.hight)
            node.balance = right - left
            self.balance(node)
            # print(node.key, right, left)
            self.calculeBalance(hight + 1, node.dad)
        else:
            node.hight = max(hight, node.hight)
            node.balance = right - left
            self.balance(node)
            # print(node.key, right, left)

    def balance(self, node):
        while abs(node.balance) > 1:
            if node.balance > 1:
                if node.right.balance < 0:
                    self.rightRotate(node.right)
                    self.calculeHight(node.right)
                self.leftRotate(node)
                self.calculeHight(node)
            if node.balance < -1:
                if node.left.balance > 0:
                    self.leftRotate(node.right)
                    self.calculeHight(node.right)
                self.rightRotate(node)
                self.calculeHight(node)
         

    def rightRotate(self, node):
        A = node
        B = node.left
        T = B.right
        print("Rotação a direita de", A.key, "ao redor de", B.key)
        if A.dad == self:
            self.root = B
            B.dad = A.dad
            B.right = A
            A.dad = B
            A.left = T
            if T is not None:
                T.dad = A
        elif A.dad.key > A.key:
            A.dad.left = B
            B.dad = A.dad
            B.right = A
            A.dad = B
            A.left = T
            if T is not None:
                T.dad = A
        else:
            A.dad.right = B
            B.dad = A.dad
            B.right = A
            A.dad = B
            A.left = T
            if T is not None:
                T.dad = A



    def insertAux(self, key, node):
        print("tentando inserir", key, "no nó", node.key)
        if key < node.key:
            if node.left is None:
                node.left = Node(key, node)
                self.calculeBalance(node.left.balance, node.left)
            else:
                self.insertAux(key, node.left)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, node)
                self.calculeBalance(node.right.balance, node.right)
            else:
                self.insertAux(key, node.right)
        else:
            print("O valor", key, "já está na arvore")

    def inOrder(self):
        if self.root is None:
            print("Impossivel imprimir arvore vazia")
        else:
            self.inOrderAux(self.root)

    def inOrderAux(self, node):
        if node is None:
            print("@", end="")
        else:
            print("(", end="")
            self.inOrderAux(node.left)
            print("[key:{} b:{} h:{}]".format(node.key, node.balance, node.hight,), end="")
            self.inOrderAux(node.right)
            print(")", end="")


if __name__ == "__main__":
    tree = AVL()
    for i in [3, 2, 1]:
        tree.insert(i)
    print()
    # tree.calculeHight(tree.root)
    tree.inOrder()
