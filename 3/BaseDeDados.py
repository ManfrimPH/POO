"""
public = acessados dentro e fora da classe(metodos e atributos)
protected = acessados dentro da classe ou de suas filhas (atributos)
private = acessados apenas dentro da classe (atributos ou metodos)

python não tem modificadores de acesso
mas utiliza-se _ para atributos protegidos 
e __ para atributos privados

o _ é uma mudança apenas de convenção, ou seja, não impede que o atributo seja acessado fora da classe

já o __ é um modificador de acesso que faz com que o atributo ou método seja privado e realmente não consegue acessar fora da classe
"""

class BaseDeDados:
  def __init__(self):
    self.__dados = {}

  def inserir_cliente(self, id, nome):
    if 'clientes' not in self.__dados:
      self.__dados['clientes'] = {id: nome}
    else:
      self.__dados['clientes'].update({id: nome})

  def lista_clientes(self):
    for id, nome in self.__dados['clientes'].items():
      print(id, nome)

  def apaga_cliente(self, id):
    del self.__dados['clientes'][id]

  @property
  def dados(self):
    return self.__dados