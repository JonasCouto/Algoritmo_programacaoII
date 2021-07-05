from Torre import Torre
from Apartamento import Apartamento
# from Fila import Fila

t1 = Torre()
t1.cadastrar(8, "A", "Ipiranga")
t1.imprimirInformacoes()

ap = Apartamento()
ap.cadastrar(1, "555C", 12, t1)
ap.imprimirInformacoes()

# f1 = Fila()
# f1.adicionaAPT(ap)
# f1.imprimir()