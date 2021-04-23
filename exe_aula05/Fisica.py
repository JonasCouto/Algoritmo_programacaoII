from Pessoa import Pessoa

class Fisica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cpf, idade, peso, altura):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idade = idade
        self.peso = peso
        self.altura = altura
        

    def imprimeCPF(self):
        print("CPF: ",self.__cpf)

    def __calculaIMC(self):
        imc = self.peso / (self.altura ** 2)
        return imc
