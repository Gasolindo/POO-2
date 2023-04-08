from animal import Animal

class Dog(Animal):

    def __ini__(self,cor_do_pelo,raça,nome,idade,peso):
        self.cor_do_pelo=cor_do_pelo
        self.raça=raça
        super().__init__(nome,idade,peso)

    def mensagem(self):
      return f"Sou um cachorro , me chamo {self.nome},de raça {self.raça}, e tenho pelo {self.cor_do_pelo}! "
    
    def dormir(self):
       return "Cachorro acordado!"
       


