from No import No

# inserir na pilha
# remover na pilha

class Pilha:
    def __init__(self):
        self.tamanho = 0
        self.topo = None
        self.fim = None
    
    def inserir(self, valor):
        elem = No(valor)

        # se a pilha estiver vazia
        if self.topo == None:
            self.topo = elem
            self.fim = elem

        else:                        
            # proxíma posição recebe o que era o primeiro
            elem.proximo = self.topo

            #primeira posição recebe o valor inserido
            self.topo = elem

            #aumenta o tamanho da pilha
            self.tamanho = self.tamanho + 1

    def remover(self, valor2):
        if self.tamanho > 0:
            #recebe o valor do topo
            valor2 = self.topo

            #topo recebe o valor que era o proximo abaixo do primeiro
            self.topo = self.topo.proximo

            #diminui o valor da pilha 
            self.tamanho = self.tamanho - 1
            return valor2

        else:
            print("Pilha esta vazia !!!")
    
    def __repr__(self):
        r = ""
        ponteiro = self.topo
        while(ponteiro):
            r = r + str(ponteiro.dado) + "\n"
            ponteiro = ponteiro.proximo
        return r

    def __str__(self):
        return self.__repr__()