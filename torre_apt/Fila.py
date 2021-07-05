# Importar classes torre e apartamento
from Torre import Torre 
from Apartamento import Apartamento

# Classe
class Fila():
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    # Adiciona na FILA
    def adicionaAPT(self, apt):
        apt = Apartamento(apt)

        if self.tamanho == 0:
            self.primeiro = apt
            self.ultimo = apt

        else:
            self.ultimo.proximo = apt
            self.ultimo = apt

        self.tamanho = self.tamanho + 1

    # Remover da fila
    def removerFila(self):
        # verifica se a primeira posição da fila esta vazia.
        if self.tamanho > 0:
            apt = self.primeiro.vaga
            self.primeiro = self.primeiro.proximo
            self.tamanho = self.tamanho - 1
            return apt

        else:
            return print("Fila esta vazia! ")

    # retornar vagas
    def retornaVaga(self):
        if self.tamanho > 0:
            apt = self.primeiro.vaga
            return apt
    

    # percorre a fila 
    def __repr__(self):
        r = ""
        ponteiro = self.primeiro
        # enquanto a fila não for vazia percorre ela até a ultima possição
        while(ponteiro):
            r = r + str(ponteiro.vaga) + " "
            ponteiro = ponteiro.proximo
        return r

    # Imprime a Fila
    def __str__(self):
        return self.__repr__()
