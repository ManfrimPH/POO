class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcentagem):
        self.preco = self.preco - (self.preco * (porcentagem / 100))

    #Getter
    @property
    def preco(self): #sempre que chamar o preco, ele vai chamar o getter para maior segurança
        return self._preco
    
    #Setter
    @preco.setter #modifica a variavel antes de setala, para não ter erros de valors invalidos na variavel
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()