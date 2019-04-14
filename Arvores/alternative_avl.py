class Noh:
    def __init__(self, v, pai):
        self.campo = v
        self.subEsq = None
        self.subDir = None
        self.pai = pai
        self.fb = 0

class BST:
    def __init__(self):
        self.raiz = None

    def setRaiz(self, v, pai):
        self.raiz = Noh(v, None)

    def insereVetor(self, vetor):
        for i in vetor:
            self.insere(i)

    def insere(self, campo):
        if (self.raiz is None):
            self.setRaiz(campo, None)
        else:
            self.insereNoh(self.raiz, campo, self.raiz)

    def insereNoh(self, nohAtual, campo, pai):
        if (campo < nohAtual.campo):
            if(nohAtual.subEsq):
                self.insereNoh(nohAtual.subEsq, campo, nohAtual)
            else:
                nohAtual.subEsq = Noh(campo, nohAtual)
        elif(campo > nohAtual.campo):
            if(nohAtual.subDir):
                self.insereNoh(nohAtual.subDir, campo, nohAtual)
            else:
                nohAtual.subDir = Noh(campo, nohAtual)
        else:
            print("Valor já está na árvore!")

    def minimo(self, nohAtual):
        while nohAtual.subEsq is not None:
            nohAtual = nohAtual.subEsq
        return nohAtual

    def maximo(self, nohAtual):
        while nohAtual.subDir is not None:
            nohAtual = nohAtual.subDir
        return nohAtual

    def sucessor(self, nohAtual):
        if nohAtual.subDir is not None:
            return self.minimo(nohAtual.subDir)
        y = nohAtual.pai
        while y is not None and nohAtual is y.subDir:
            nohAtual = y
            y = y.pai
        return y
    
    def antecessor(self, nohAtual):
        if nohAtual.subEsq is not None:
            return self.maximo(nohAtual.subEsq)
        y = nohAtual.pai
        while y is not None and nohAtual is y.subEsq:
            nohAtual = y
            y = y.pai
        return y

    def removeAux(self, campo):
        temp = self.busca(campo)
        if temp==None:
            print("Valor não existe na raiz")
        else:
            self.remove(temp) 

    def remove(self, nohAtual):
        if nohAtual.subEsq == None and nohAtual.subDir == None: #folha
           if nohAtual.pai.subEsq !=None:
              if nohAtual.pai.subEsq.campo == nohAtual.campo:
                  nohAtual.pai.subEsq = None
           if nohAtual.pai.subDir !=None:
              if nohAtual.pai.subDir.campo == nohAtual.campo:
                  nohAtual.pai.subDir = None
        elif nohAtual.subEsq != None and nohAtual.subDir == None: # tem só filho esquerdo
              if nohAtual.pai.subEsq != None:   # o pai tem filho esquerdo? 
                 if nohAtual.pai.subEsq.campo == nohAtual.campo: # ele é o filho esquerdo ? XD
                    nohAtual.subEsq.pai = nohAtual.pai # pai dele vira pai do filho dele 
                    nohAtual.pai.subEsq = nohAtual.subEsq # pai aponta para o filho 
              if nohAtual.pai.subDir != None:   # o pai tem filho direito?
                 if nohAtual.pai.subDir.campo == nohAtual.campo: # ele é o filho direito?
                    nohAtual.subEsq.pai = nohAtual.pai # pai dele vira pai do filho dele
                    nohAtual.pai.subDir = nohAtual.subEsq # pai dele aponta para o filho dele
        elif nohAtual.subDir != None  and nohAtual.subEsq == None: # tem só filho direito
              if nohAtual.pai.subEsq != None:
                 if nohAtual.pai.subEsq.campo == nohAtual.campo:
                    nohAtual.subDir.pai = nohAtual.pai  
                    nohAtual.pai.subEsq = nohAtual.subDir
              if nohAtual.pai.subDir != None:
                 if nohAtual.pai.subDir.campo == nohAtual.campo:
                    nohAtual.subDir.pai = nohAtual.pai 
                    nohAtual.pai.subDir = nohAtual.subDir
        else:
             temp = self.sucessor(nohAtual)
             nohAtual.campo = temp.campo
             self.remove(temp)
            
    def busca(self, campo):
        if self.raiz!=None:
            return self.buscavalor(self.raiz, campo)
        else:
            return None

    def buscavalor(self, nohAtual, campo):
        if campo == nohAtual.campo:
            return nohAtual
        elif campo<nohAtual.campo and nohAtual.subEsq!=None:
            return self.buscavalor(nohAtual.subEsq, campo)
        elif campo>nohAtual.campo and nohAtual.subDir!=None:
            return self.buscavalor(nohAtual.subDir, campo)
        else:
            return None
           
    def emOrdemAuxNum(self, noh, v):
        if noh is None:
            print("@", end="")
        else:
            print("(", end="")
            self.emOrdemAuxNum(noh.subEsq, v)
            if noh == self.raiz:
               print(noh.campo, end="")
            else:
               print(noh.campo, noh.pai.campo, end="")
            self.emOrdemAuxNum(noh.subDir, v)
            print(")", end=""),

    def emOrdemAux(self, noh):
        if noh is None:
            print("@"),
        else:
            print("("),
            self.emOrdemAux(noh.subEsq)
            print(noh.campo),
            self.emOrdemAux(noh.subDir)
            print(")"),

    def preOrdemAux(self, noh):
        if noh is None:
            print("@"),
        else:
            print("("),
            print(noh.campo),
            self.preOrdemAux(noh.subEsq)
            self.preOrdemAux(noh.subDir)
            print(")"),

    def posOrdemAux(self, noh):
        if noh is None:
            print("@"),
        else:
            print("("),
            self.posOrdemAux(noh.subEsq)
            self.posOrdemAux(noh.subDir)
            print(noh.campo),
            print(")"),

    def posOrdem(self):
        self.posOrdemAux(self.raiz)

    def preOrdem(self):
        self.preOrdemAux(self.raiz)

    def emOrdem(self):
        self.emOrdemAux(self.raiz)

   
arvore = BST()
arvore.insereVetor([4, 99, 3, 12, 13, 8, 1, 2, 7, 6, 5, 9, 33, 93, 46])
# arvore.emOrdemAuxNum(arvore.raiz, 0)
arvore.removeAux(12)
arvore.emOrdemAuxNum(arvore.raiz, 0)

# arvore.emOrdem()
# ( ( ( @ 1 @ ) 2 @ ) 3 ( ( ( @ 6 @ ) 7 @ ) 8 ( @ 9 @ ) ) )
# print("\n")
# arvore.preOrdem()
# ( 3 ( 2 ( 1 @ @ ) @ ) ( 8 ( 7 ( 6 @ @ ) @ ) ( 9 @ @ ) ) )
# print("\n")
# arvore.posOrdem()
# ( ( ( @ @ 1 ) @ 2 ) ( ( ( @ @ 6 ) @ 7 ) ( @ @ 9 ) 8 ) 3 )
