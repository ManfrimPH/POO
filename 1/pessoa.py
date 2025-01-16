from datetime import datetime
from random import randint

class Pessoa:
  
  ano_atual = int(datetime.strftime(datetime.now(),'%Y')) #atributo da classe (feito para valores diferentes para cada instância)

  def __init__(self, nome:str, idade:int, comendo:bool=False, falando:bool=False): #Atributos da instância chama o atributo da classe não podendo usar o sistema de atributos da classe 
    self.nome = nome
    self.idade = idade
    self.comendo = comendo
    self.falando = falando
  
  def comer(self, alimento:str):#Atributos da instância chama o atributo da classe não podendo usar o sistema de atributos da classe 
    if self.comendo:
      print(f'{self.nome} já está comendo.')
      return
    if self.falando:
      print(f'{self.nome} não pode comer enquanto fala.')
      return
    print(f'{self.nome} está comendo {alimento}')
    self.comendo = True

  def parar_comer(self):#Atributos da instância chama o atributo da classe não podendo usar o sistema de atributos da classe 
    if not self.comendo:
      print(f'{self.nome} não está comendo.')
      return
    print(f'{self.nome} parou de comer.')
    self.comendo = False

  def falar(self, fala:str):#Atributos da instância chama o atributo da classe não podendo usar o sistema de atributos da classe 
    if self.falando:
      print(f'{self.nome} já está falando.')
      return
    if self.comendo:
      print(f'{self.nome} não pode falar de boca cheia.')
      return
    print(f'Narador: O {self.nome} está falando:')
    print(fala)
    self.falando = True

  def parar_falar(self):#Atributos da instância chama o atributo da classe não podendo usar o sistema de atributos da classe 
    if not self.falando:
      print(f'{self.nome} não está falando.')
      return
    print(f'{self.nome} parou de falar.')
    self.falando = False

  def ano_nascimento(self):#Atributos da instância chama o atributo da classe não podendo usar o sistema de atributos da classe 
    return self.ano_atual - self.idade
  
  @classmethod
  def por_ano_nascimento(cls, nome,ano_nascimento):#Metodo da Classe chama a classe em si e não a instância o que lhe permite usar atributos da classe
    idade = cls.ano_atual - ano_nascimento
    return cls(nome, idade)
  
  @staticmethod
  def gerar(): #Metodo que não usa nem a classe e nem a instância, mas se mantem na classe por organização
    rand = randint(1000,2000)
    return rand