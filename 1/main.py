from pessoa import Pessoa

p1 = Pessoa('Pedro',19)
p2 = Pessoa('Luiz', 25)
p3 = Pessoa('Jean', 27)

print('\n')

p1.comer('Pizza')
p1.parar_comer()
p1.parar_comer()
p1.comer('Pão')

print('\n')

p2.falar('Você ta loco?')
p2.parar_falar()
p2.parar_falar()
p2.falar('Cheiro bom.')

print('\n')

p3.comer('Pizza')
p3.falar('Cheiro bom.')
p3.parar_comer()
p3.falar('Você ta loco?')
p3.comer('Pão')

print('\n')

print(f'{p1.nome} nasceu no ano de {p1.ano_nascimento()}')
print(f'{p2.nome} nasceu no ano de {p2.ano_nascimento()}')
print(f'{p3.nome} nasceu no ano de {p3.ano_nascimento()}')

print('\n')