from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

pf1 = Fisica(987, "Jonas", "Bento 1000", "3333-55-66", "123.126.700-21", 35, 77.5, 1.71)

pf1.imprimeCPF()
# pf1.__calculaIMC()

pf1.imprimirNome()
# pf1.__imprimirTelefone()

pj1 = Juridica(741, "Paulo", "Ipiranga 7200", "3216-55-88", "123528788-52"," 879879878-5151515", 87)

pj1.imprimeCNPJ()
# pj1.__emitirNotaFiscal()
