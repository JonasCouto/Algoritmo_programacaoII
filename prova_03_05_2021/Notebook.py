from Computador import Computador

class Notebook(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__tempoDeBateria = tempoDeBateria

    
    def getInformacoes(self):
        print("O Preço do computador é: ", self.preco,"\nModelo: ",self.modelo, "\nCor: ",
        self.cor, "\nPreco: ",self.preco, "\nPotencia da Fonte: ", self.potenciaDaFonte,"\nTempo de Bateria: ", self.tempoDeBateria)