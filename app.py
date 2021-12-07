from imposto import Imposto

educacao = Imposto()
educacao.aliquota = 0.15
livro = educacao.CalculaImposto(200)

informatica = Imposto()
informatica.aliquota = 0.10
mouse = informatica.CalculaImposto(50)

cozinha = Imposto()
cozinha.aliquota = 0.20
faca = cozinha.CalculaImposto(15)

caderno = educacao.CalculaImposto(30)

prato = cozinha.CalculaImposto(25)