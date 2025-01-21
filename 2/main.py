from produto import Produto

p1 = Produto('Camiseta', 50)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca', 15)
p2.desconto(10)
print(p2.preco)

p3 = Produto('Caneca', 'R$15')
p3.desconto(10)
print(p3.preco)

p4 = Produto('CAMISETA', 50)
print(p4.nome)

p5 = Produto('CANECA', 50)
print(p5.nome)