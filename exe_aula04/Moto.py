from Automovel import Automovel

class Moto(Automovel):

    def __init__(self, marca, qtdRodas, modelo, potenciaMotor, partidaEletrica):
        super().__init__(marca, qtdRodas, modelo, potenciaMotor)
        self.partidaEletrica = partidaEletrica


    def imprimirInformacoes(self):
        print("Marca: ",self.marca, "\nRodas: ",self.qtdRodas, "\nModelo: ",self.modelo, "\nVelocidade: ",
        self.velocidade, "\nPotencia: ",self.potenciaMotor, "\nPartida Eletrica: ", self.partidaEletrica)

