magias = {}

def get_magias():
    return magias

def inserir_magia(magia):
    nome_magia = magia.nome
    if nome_magia not in magias.keys():
        magias[nome_magia] = magia
        return True
    else:
        print('Magia: ' + nome_magia + ' já tem cadastro')
    return False


class Magia:
   def __init__(self, nome, nível_dificuldade, dano, utiliza_componente):
       self.nome = nome
       self.nível_dificuldade =  nível_dificuldade if nível_dificuldade >= 0 and nível_dificuldade <= 5 else 666
       self.dano = dano
       self.utiliza_componente = utiliza_componente


   def __str__(self):
       formato = '{:<13} {} {:>3} {}{:>4}{} {:>12} {}'
       magia_formato = formato.format(self.nome,'|', self.nível_dificuldade,'|', self.dano,'|', componente(self.utiliza_componente),'|')
       return magia_formato


def componente(componente):
    if componente:
        return 'utiliza'
    else: return 'Não utiliza'