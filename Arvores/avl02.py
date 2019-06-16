class Node:
    def __init__(self, key, dad=None):
        self.key = key
        self.dad = dad
        self.left = None
        self.right = None
        self.hight = None
        self.balance = None
        self.color = None


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.root.hight = 0
            self.root.balance = 0
        else:
            self.insertAux(key, self.root)
        # self.UpdateBalance(self.root)

    def insertAux(self, key, node):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, node)
                node.left.hight = 0
                node.left.balance = 0
                self.calcBalance(node.left)
            else:
                self.insertAux(key, node.left)

        elif key > node.key:
            if node.right is None:
                node.right = Node(key, node)
                node.right.hight = 0
                node.right.balance = 0
                self.calcBalance(node.right)
            else:
                self.insertAux(key, node.right)
        else:
            print('The key', key, 'is alredy in the tree')

    def insertArray(self, array):
        for i in array:
            self.insert(i)

    def calcBalance(self, node):
        '''Calculate the balance on the isertion'''

        left, right = 0, 0
        if node.left is not None:
            left = node.left.hight+1
        if node.right is not None:
            right = node.right.hight+1
        node.hight = max(left, right)
        node.balance = right-left

        if node.dad is not None:
            self.calcBalance(node.dad)

    def UpdateBalance(self, node):
        '''Calculate all the tree balance'''

        left, right = 0, 0
        if node.left is not None:
            left = self.UpdateBalance(node.left)
        if node.right is not None:
            right = self.UpdateBalance(node.right)

        node.balance = right - left
        node.hight = max(right, left)
        return node.hight+1

    def balance(self, node):
        if abs(node.balance) > 1:
            if node.balance < -1:
                if node.left.right > 0:
                    self.leftRotate(node.left)
                self.rightRotate(node)
            elif node.balance > 1:
                if node.right.left < 0:
                    self.rightRotate(node.right)
                self.leftRotate(node)
            self.UpdateBalance(node)

    def leftRotate(self, node):
        pass
    
    def rightRotate(self, node):
        pass

    def preOrder(self):
        self.preOrderAux(self.root)

    def preOrderAux(self, node):
        print("(", end="")

        print("[{}:{}]".format(node.key, node.balance), end="")

        if node.left is not None:
            self.preOrderAux(node.left)
        else:
            print("@", end="")

        if node.right is not None:
            self.preOrderAux(node.right)
        else:
            print("@", end="")

        print(")", end="")


if __name__ == "__main__":
    tree = AVL()
    tree.insertArray([1,3,2])
    tree.preOrder()
