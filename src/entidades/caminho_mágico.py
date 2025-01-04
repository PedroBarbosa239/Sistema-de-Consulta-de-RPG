from entidades.magia import get_magias

caminhos = {}

def set_caminhos(caminhos1):
    global caminhos
    caminhos = caminhos1

def dificuldade(caminho,dif):
    check = False
    for dificuldade in caminho.magias.values():
        if not(int(dif) > dificuldade.nível_dificuldade):
            check = True
    return check

def get_caminhos(): return caminhos

def inserir_caminho(caminho):
    nome_caminho = caminho.nome
    if nome_caminho not in caminhos.keys():
        caminhos[nome_caminho] = caminho
        return True
    else:
        print('Caminho mágico: ' + nome_caminho + ' já tem cadastro')
        return False

class CaminhoMagico:
    def __init__(self, nome, magia_tipo):
        self.nome = nome
        self.magia_tipo = magia_tipo if magia_tipo in ('água', 'terra', 'fogo', 'ar', 'estranha') else 'Indefinida'
        self.magias = {}

    def __str__(self):
        formato = '{:<23} {} {:>9} {}'
        caminho_formato = formato.format(self.nome,'|', self.magia_tipo,'|')
        return caminho_formato

    def inserir_magias(self, magia):
        nome_magia = magia.nome
        if nome_magia not in self.magias.keys():
            self.magias[nome_magia] = magia
        else:
            print('magia ' + nome_magia + ' já tem cadastro no Caminho')


