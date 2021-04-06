from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def __init__(self, cod, nome, matricula, ano):
       # Aluno.__init__(self, cod, nome, matricula)
        super().__init__(cod, nome, matricula)
        self.ano = ano
        self.Imprimir()

    def Imprimir(self):
        print("Codigo: ",self.cod, "\nNome: ",self.nome, "\nMatricula: ",self.matricula, "Ano: ", self.ano)