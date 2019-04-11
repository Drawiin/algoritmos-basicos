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

    def getHight(self):
        '''
            Retorna a altura da árvore ou
            sub-árvore
        '''
        if self.node is not None:
            return self.hight
        else:
            return 0

    def isLeaf(self):
        '''
            Verifica se a sub-árvore é um folha
        '''
        if self.hight == 0:
            return True
        else:
            return False

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
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.updadateHight()
                if self.node.right is not None:
                    self.node.right.updadateHight()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def updateBalance(self, recurse=True):
        if self.node is not None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.updateBalance()
                if self.node.right is not None:
                    self.node.right.updateBalance()

            self.balance = self.node.right.height - self.node.left.height
        else: 
            self.balance = 0


    def delete(self, key):
        print("tentando deletar no nó ", self.node.key)
        if self.node is not None: 
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
                        print("sucessor lógico achado ",key, " -> "replacement.key)
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

            self.rebalance()
        else: 
            return 

    def logical_successor(self, node):
        ''' 
            Acha o sucessor lógico do nó a ser removido
        '''
        node = node.right.node  
        if node is not None: # just a sanity check  
            
            while node.left is not None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self is None or self.node is None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 

    def display(self, level=0, pref=''):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''        
        self.update_heights()  # Must update heights before balances 
        self.update_balances()
        if(self.node != None): 
            print ('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' '    )
            if self.node.left != None: 
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')

# Usage example
if __name__ == "__main__": 
    a = AVLTree()
    print ("----- Inserting -------")
    #inlist = [5, 2, 12, -4, 3, 21, 19, 25]
    inlist = [7, 5, 2, 6, 3, 4, 1, 8, 9, 0]
    for i in inlist: 
        a.insert(i)
         
    a.display()
    
    print ("----- Deleting -------")
    a.delete(3)
    a.delete(4)
    # a.delete(5) 
    a.display()
    
    print ()
    print ("Input            :", inlist )
    print ("deleting ...       ", 3)
    print ("deleting ...       ", 4)
    print ("Inorder traversal:", a.inorder_traverse())

    pass
