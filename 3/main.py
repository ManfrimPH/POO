from BaseDeDados import BaseDeDados

bd = BaseDeDados()

bd.inserir_cliente(1, 'Otávio')
bd.inserir_cliente(2, 'Miranda')
bd.inserir_cliente(3, 'Rose')
bd.__dados = 'teste'
bd.apaga_cliente(2)
bd.lista_clientes()
print(bd.__dados) # por algum motivo ele cria um novo atributo __dados e não acessa o atributo privado da classe
print(bd._BaseDeDados__dados) # acessando o atributo privado da classe diretamente, o verdadeiro atributo privado
                              # e não o que foi criado a partir da tentativa de acesso direto ao atributo privado
print(bd.dados) # acessando o atributo privado da classe através do método getter @property