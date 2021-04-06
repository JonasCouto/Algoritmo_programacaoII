from Aluno import Aluno

class AlunoGraduacao(Aluno):
    def __init__(self, cod, nome, matricula, semestre):
        Aluno.__init__(self,cod, nome, matricula)
        self.semestre = semestre
        self.Imprimir()


    def Imprimir(self):
        print("Codigo: ",self.cod, "\nNome: ",self.nome, "\nMatricula: ",self.matricula, "Semestre: ",self.semestre)