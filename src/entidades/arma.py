

class Arma:
   def __init__(self, nome, dano, peso, tipo):
       self.nome = nome
       self.dano = dano
       self.peso = peso
       self.tipo = tipo if tipo in ('Espada','Arco','Machado','Adaga','Cajado') else 'Diferente'


   def __str__(self):
       formato = '{:<25} {} {:>6} {} {:>6} {} {:>7} {}'
       arma_formato = formato.format(self.nome, '|' ,self.dano,'|' , f'{self.peso}' +' kg','|' , self.tipo,'|')
       return arma_formato
