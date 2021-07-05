

# Classe Torre
class Torre():
    def __init__(self):
        self.id = None
        self.nome = None
        self.endereco = None

    # cadastrar torre id, nome e endereco
    def cadastrar(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    # imprimir informaçoes da torre
    def imprimirInformacoes(self):
        print("ID: ",self.id, "\nNome: ",self.nome, "\nEndereco: ",self.endereco)
