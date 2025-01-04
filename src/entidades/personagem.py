from entidades.caminho_mágico import get_caminhos, dificuldade
from entidades.bolsa import get_bolsas, dano_arma, peso_item
from entidades.ser_mágico import get_seres_magicos, Monstro, RaçaInteligente
personagens = []

def get_personagens():
  return personagens

def set_personagens(personagens1):
    global personagens
    personagens = personagens1

def inserir_personagem(personagem):
    if personagem not in personagens:personagens.append(personagem)
    else:print('Personagem  já tem cadastro --- ' + str(personagem))

def criar_personagem(nome_personagem, nivel_personagem, classe_personagem, pontos_vida_personagem
                            , pontos_forca_personagem, id_bolsa,nome_caminho_magico, nome_ser_magico):
    bolsa = get_bolsas()[id_bolsa]
    if bolsa is None:
        print('Bolsa ' + id_bolsa + ' não cadastrada')
        return

    caminho = get_caminhos()[nome_caminho_magico]
    if caminho is None:
        print('Caminho mágico: ' + nome_caminho_magico + ' não cadastrado')
        return

    ser = get_seres_magicos()[nome_ser_magico]
    if ser is None:
        print('Ser mágico: ' + nome_ser_magico + ' não cadastrado')
        return

    return Personagem(nome_personagem, nivel_personagem, classe_personagem, pontos_vida_personagem, pontos_forca_personagem, bolsa,caminho, ser)




def filtrar_personagens(nivel_max , peso_max_bolsa ,magia_tipo_caminhoMágico, nivel_max_dificuldade_magia,
                           dano_max_arma, peso_max_itens, habilidade_max_ser_magico , fraqueza_monstro ,
                           tendencia_raca_inteligente):
    personagens_selecionados = []
    for personagem in personagens:
        if nivel_max is not None and personagem.nivel > nivel_max: continue
        if magia_tipo_caminhoMágico is not None and personagem.caminho_magico.magia_tipo != magia_tipo_caminhoMágico: continue
        if peso_max_bolsa is not None and personagem.bolsa.peso_max > peso_max_bolsa: continue
        if nivel_max_dificuldade_magia is not None and not dificuldade(personagem.caminho_magico, nivel_max_dificuldade_magia): continue
        if dano_max_arma is not None and not dano_arma(personagem.bolsa,dano_max_arma): continue
        if peso_max_itens is not None and not peso_item(personagem.bolsa, peso_max_itens): continue

        if habilidade_max_ser_magico is not None and personagem.ser_magico.habilidade_mágica > habilidade_max_ser_magico: continue
        if isinstance(personagem.ser_magico, Monstro):
            if fraqueza_monstro is not None and personagem.ser_magico.fraqueza != fraqueza_monstro: continue
        elif isinstance(personagem.ser_magico, RaçaInteligente):
            if tendencia_raca_inteligente is not None and personagem.ser_magico.tendência != tendencia_raca_inteligente: continue

        personagens_selecionados.append(personagem)
    return personagens_selecionados




class Personagem:
    def __init__(self, nome, nivel, classe, pontos_vida, pontos_forca, bolsa,caminho_magico, ser_magico):
        self.nome = nome
        self.nivel = nivel
        self.pontos_vida = pontos_vida
        self.pontos_forca = pontos_forca
        self.classe = classe if classe in ('Insano','Mago','Feiticeiro','Inventor','Guerreiro') else 'Indefinido'
        self.bolsa = bolsa
        self.caminho_magico = caminho_magico
        self.ser_magico = ser_magico

    def __str__(self):
        formato1 = '{:<19}  {} {:<12} {} {:<3} {} {:<3} {} {:<3} {} {:<23} {} {:<13} {}'
        return formato1.format(self.nome, '|', self.classe, '|', self.pontos_vida, '|', self.pontos_forca, '|', self.bolsa.id, '|',self.caminho_magico.nome, '|', self.ser_magico.nome, '|')

    def str_filtro(self):
        if isinstance(self.ser_magico, Monstro):
            atributo_especifico = self.ser_magico.fraqueza
        elif isinstance(self.ser_magico, RaçaInteligente):
            atributo_especifico = self.ser_magico.tendência
        else: atributo_especifico = ''

        formato = '{:>2} {} {:<7} {} {:<9} {} {:<3} {} {:<18} {} '
        filtro_formatado = formato.format(str(self.nivel),'|', f'{self.bolsa.peso_max:3d}' + ' kg', '|',self.caminho_magico.magia_tipo, '|',self.ser_magico.habilidade_mágica, '|', atributo_especifico, '|')
        return self.__str__() + filtro_formatado