from Autor import Autor
from Livro import Livro




#criar Autor
a1 = Autor(1, " João")

# criar Livro
l1 = Livro(3, "Brasil Campeão", a1)


#criar pilha
pilha = Pilha()

# Inserir na pilha
pilha.inserir(l1)

# pilha = Pilha()
print(pilha)
