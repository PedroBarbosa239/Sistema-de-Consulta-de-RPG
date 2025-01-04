seres_magicos = {}

def get_seres_magicos():
   return seres_magicos

def set_seres_magicos(ser1):
    global seres_magicos
    seres_magicos = ser1

def inserir_ser_magico(ser_magico):
    nome_ser_magico = ser_magico.nome
    if nome_ser_magico not in seres_magicos.keys():
        seres_magicos[nome_ser_magico] = ser_magico
        return True
    else:
        print('Ser mágico: ' + nome_ser_magico + ' já tem cadastro')
    return False

class SerMagico:
    def __init__(self,nome,habilidade_mágica):
        self.nome = nome
        self.habilidade_mágica = habilidade_mágica

    def __str__(self):
        formato = '{:>11} {} {:>5} {}'
        ser_magico_formato = formato.format(self.nome,'|', self.habilidade_mágica,'|')
        return ser_magico_formato

class Monstro(SerMagico):
    def __init__(self, nome, habilidade_mágica, tipo_fera, fraqueza, origem):
        super().__init__(nome, habilidade_mágica)
        self.tipo_fera = tipo_fera
        self.fraqueza = fraqueza if fraqueza in {'Ruídos estridentes','Magias de gelo','Corte', 'Ar', 'Eletricidade'} else 'Nulo'
        self.origem = origem

    def __str__(self):
        formato = '{:>11} {} {:>5} {} {:>10} {} {:<29} {} {:>16} {}'
        monstro_formato = formato.format(self.nome,'|', self.habilidade_mágica,'|', self.tipo_fera,'|',self.fraqueza,'|',self.origem,'|')
        return monstro_formato

class RaçaInteligente(SerMagico) :
    def __init__(self, nome, habilidade_mágica, tendência, habilidade_unica, habitat):
        super().__init__(nome, habilidade_mágica)
        self.tendência = tendência if tendência in {'Boa','Caótico','Neutra'} else 'Indefinido'
        self.habilidade_unica = habilidade_unica
        self.habitat = habitat

    def __str__(self):
        formato = '{:>11} {} {:>5} {} {:>10} {} {:<29} {} {:>16} {}'
        raca_inteligente_formato = formato.format(self.nome,'|', self.habilidade_mágica,'|', self.tendência,'|',self.habilidade_unica,'|',self.habitat,'|')
        return raca_inteligente_formato

