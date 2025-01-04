from entidades.item import get_itens
    
bolsas = {}

def get_bolsas(): return bolsas

def set_bolsas(bolsa1):
    global bolsas
    bolsas = bolsa1
def inserir_bolsa(bolsa):
    bolsa_id = bolsa.id
    if bolsa_id not in bolsas.keys():
        bolsas[bolsa_id] = bolsa
        return True
    else:
        print('Bolsa com o id: ' + bolsa_id + ' já tem cadastro')
        return False

def dano_arma(bolsa,dif):
    check = False
    for arma in bolsa.armas.values():
        if not(int(dif) > arma.dano):
            check = True
    return check

def peso_item(bolsa,dif):
    check = False
    for item in bolsa.itens.values():
        if dif > item.peso:
            check = True
    return check
class Bolsa:
    def __init__(self,id, peso_max):
        self.id = id
        self.peso_max = peso_max
        self.itens = {}
        self.armas = {}

    def __str__(self):
        formato = '{:<2} {} {:>5} {}'
        bolsa_formato = formato.format(self.id,'|', f'{self.peso_max}' + ' kg','|')
        return bolsa_formato

    def inserir_itens(self, item):
            nome_item = item.nome
            if nome_item not in self.itens.keys():
                self.itens[nome_item] = item
            else:
                print('Item ' + nome_item + ' já tem cadastro na bolsa')

    def inserir_arma(self, arma):
        nome_arma = arma.nome
        if nome_arma not in self.armas.keys():
            self.armas[nome_arma] = arma
        else:
            print('Arma ' + nome_arma + ' já tem cadastro')



