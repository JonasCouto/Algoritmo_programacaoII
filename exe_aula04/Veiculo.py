class Veiculo():
    def __init__(self, marca, qtdRodas, modelo):
    
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade = self.velocidade + valor
    
    def frear(self, valor):
        self.velocidade = self.velocidade - valor                
    

    def imprimirInformacoes(self):
        print("Marca: ",self.marca, "\nRodas: ",self.qtdRodas, "\nModelo: ",self.modelo, "\nVelocidade: ",self.velocidade)


