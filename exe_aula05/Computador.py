class Computador():
    def __init__(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco

    def cadastrar(self):
        self.modelo = input("Modelo do computador: ")
        self.cor = input("Cor: ")
        self.preco = int(input("Preço: ")
        )

    def getInformacoes(self):
        print("O Preço do computador é: ", self.preco)