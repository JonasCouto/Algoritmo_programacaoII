from Pessoa import Pessoa

class Juridica(Pessoa):
    def __init__(self, codigo, nome, endereco, telefone, cnpj, inscricao_estadual, qtd_funcionarios):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__inscricao_estadual = inscricao_estadual
        self.qtd_funcionarios = qtd_funcionarios

    def imprimeCNPJ(self):
        print("CNPJ: ",self.__cnpj)

    def __emitirNotaFiscal(self):
        print("NF nº_________: ")