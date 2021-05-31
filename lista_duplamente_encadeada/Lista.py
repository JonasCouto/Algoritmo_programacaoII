
from No import No

class Lista:
    def __init__(self):
        self.tamanho = 0
        self.inicio = None
        self.fim = None

    def adicionar(self, valor):
        aux = No(valor)

        if self.inicio == None:
            self.inicio = aux
            self.fim = aux

        else:
            ultimo = self.fim

            aux.anterior = ultimo

            ultimo.proximo = aux

            self.fim = aux

        self.tamanho += 1

    def imprimir(self):
        if self.inicio is None:
            print("A lista está vazia")
        else:
            aux = self.inicio
            while aux:
                print(aux.no)
                aux = aux.proximo

            print("Tamanho: ", self.tamanho)
            print('1° valor:', self.inicio.no)
            print('Último valor:', self.fim.no)

    def imprimir_inverso(self):
        if self.inicio is None:
            print("A lista vazia")
        else: 
            aux = self.fim
            while aux:
                print(aux.no)
                aux = aux.anterior
