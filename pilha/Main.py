from No import No
from Pilha import Pilha

#criar pilha
pilha = Pilha()

pilha.inserir(3)
pilha.inserir(5)
pilha.inserir("Jonas")
pilha.inserir(True)
pilha.inserir(9.5)

print(pilha)
pilha.remover(9.5)
print(pilha)