from datetime import datetime

class Pessoa:
  
  ano_atual = int(datetime.strftime(datetime.now(),'%Y'))

  def __init__(self, nome:str, idade:int, comendo:bool=False, falando:bool=False):
    self.nome = nome
    self.idade = idade
    self.comendo = comendo
    self.falando = falando
  
  def comer(self, alimento):
    if self.comendo:
      print(f'{self.nome} já está comendo.')
      return
    if self.falando:
      print(f'{self.nome} não pode comer enquanto fala.')
      return
    print(f'{self.nome} está comendo {alimento}')
    self.comendo = True

  def parar_comer(self):
    if not self.comendo:
      print(f'{self.nome} não está comendo.')
      return
    print(f'{self.nome} parou de comer.')
    self.comendo = False

  def falar(self, fala):
    if self.falando:
      print(f'{self.nome} já está falando.')
      return
    if self.comendo:
      print(f'{self.nome} não pode falar de boca cheia.')
      return
    print(f'Narador: O {self.nome} está falando:')
    print(fala)
    self.falando = True

  def parar_falar(self):
    if not self.falando:
      print(f'{self.nome} não está falando.')
      return
    print(f'{self.nome} parou de falar.')
    self.falando = False

  def ano_nascimento(self):
    return self.ano_atual - self.idade
