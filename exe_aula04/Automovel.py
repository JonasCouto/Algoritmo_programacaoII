from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, potenciaMotor):
        super().__init__(marca, qtdRodas, modelo)
        self.potenciaMotor = potenciaMotor

    def imprimirInformacoes(self):
        print("Marca: ",self.marca, "\nRodas: ",self.qtdRodas, "\nModelo: ",self.modelo, "\nVelocidade: ",self.velocidade, "\nPotencia: ",self.potenciaMotor)
