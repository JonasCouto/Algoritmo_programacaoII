from Computador import Computador

class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo, cor, preco)
        self.potenciaDaFonte = potenciaDaFonte

    
    def getInformacoes(self):
        print("O Preço do computador é: ", self.preco,"\nModelo: ",self.modelo, "\nCor: ",
        self.cor, "\nPreco: ",self.preco, "\nPotencia da Fonte: ", self.potenciaDaFonte)