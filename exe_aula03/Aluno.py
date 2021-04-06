class Aluno:
    def __init__(self, cod, nome, matricula):
        self.cod = cod
        self.nome = nome
        self.matricula = matricula
        #self.Imprimir()

    def Imprimir(self):
        print("Codigo: ",self.cod, "\nNome: ",self.nome, "\nMatricula: ",self.matricula)