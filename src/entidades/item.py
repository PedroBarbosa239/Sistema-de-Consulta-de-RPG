itens = {}

def get_itens():
   return itens

def inserir_item(item):
    nome_item = item.nome
    if nome_item not in itens.keys():
        itens[nome_item] = item
        return True
    else:
        print('Item: ' + nome_item + ' já tem cadastro')
    return False


class Item:
   def __init__(self, nome, peso, valor, quantidade):
       self.nome = nome
       self.peso = peso
       self.valor = valor
       self.quantidade = quantidade

   def __str__(self):
       formato = '{:<25} {} {:>6} {} {:>6} {} {:>7} {}'
       item_formato = formato.format(self.nome, '|',f'{self.peso}' +' kg','|',f'{self.valor}' +' RQ','|', self.quantidade,'|')
       return item_formato
