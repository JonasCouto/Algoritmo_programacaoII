from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, numMarcha, bagageiro):
        super(). __init__(marca, qtdRodas, modelo)

        self.numMarcha = numMarcha
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        print("Marca: ",self.marca, "\nRodas: ",self.qtdRodas, "\nModelo: ",
        self.modelo, "\nVelocidade: ",self.velocidade, "\nMarchas: ",self.numMarcha,"\nBagageiro: ",self.bagageiro)