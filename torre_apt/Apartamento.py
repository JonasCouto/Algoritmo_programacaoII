# Para que o aparamento seja criado deve existir 1 torre!
from Torre import Torre

# Classe
class Apartamento():
    def __init__(self):
        self.id = None
        self.numero = None
        self.torre = None
        self.vaga = None
        self.proximo = None
    

    # cadastrar id, numero, vaga, torre
    def cadastrar(self, id, numero, torre, vaga):
         self.id = id
         self.numero = numero
         self.torre = torre
         self.vaga = vaga


    # imprimir apartamento junto com atributos da torre
    def imprimirInformacoes(self):
        print("ID: ",self.id, "\nNumero: ",self.numero, "\nVaga: ",self.vaga,"\nTorre ID: ",self.id,"\nTorre Nome: ",self.torre.nome,"\nTorre Endereço: ",self.torre.endereco)





