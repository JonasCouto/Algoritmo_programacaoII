#####################################################################################################################
lstprodutos = []
lstpreco = []
lstqtd = []

def cadastra():
    produto = input("Digite o nome do Produto: ")
    lstprodutos.append(produto)
    preco = float(input("Digite o valor do Produto: "))
    lstpreco.append(preco)
    qtd = int(input("Digite a Quantidade: "))
    lstqtd.append(qtd)

def imprimi():
    pergunta = input("Imprimir qual produto da lista? ")
    for i in lstprodutos:
        if pergunta == i:
            print(i)
def deleta():
    print(lstprodutos)
    pergunta = input("Deletar qual produto da lista? ")
    for i in lstprodutos:
        if pergunta == i:
            lstprodutos.pop(pergunta)


while True:
    escolhe = input('--MENU--\n'
                    '0' ' - Finalizar \n'
                    '1' ' -	Cadastrar Produtos \n'
                    '2' ' -	Imprimir Produtos \n'
                    '3' ' -	Deleta Produtos \n'
                    'Escolha:  ')
    if escolhe == '0':
        break
    if escolhe == '1':
        cadastra()
    if escolhe == '2':
        imprimi()
    if escolhe == '3':
        deleta()