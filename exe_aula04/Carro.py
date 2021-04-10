from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaMotor, qtdPortas):
        super(). __init__(marca, qtdRodas, modelo, potenciaMotor)
        self.qtdPortas = qtdPortas

    def imprimirInformacoes(self):
        print("Marca: ",self.marca, "\nRodas: ",self.qtdRodas, "\nModelo: ",self.modelo, "\nVelocidade: ",
        self.velocidade, "\nPotencia: ",self.potenciaMotor, "\nPortas: ", self.qtdPortas)

