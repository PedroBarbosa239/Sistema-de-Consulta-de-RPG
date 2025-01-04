from entidades.arma import Arma
from entidades.item import  inserir_item, Item
from entidades.magia import inserir_magia, Magia
from entidades.bolsa import get_bolsas, inserir_bolsa, Bolsa
from entidades.caminho_mágico import get_caminhos, inserir_caminho, CaminhoMagico
from entidades.ser_mágico import inserir_ser_magico, Monstro, RaçaInteligente,get_seres_magicos
from entidades.personagem import get_personagens, inserir_personagem,  criar_personagem, filtrar_personagens
from util.gerais import imprimir_objetos, imprimir_objetos_internos, imprimir_objetos_associação_filtros,imprimir_objeto

def loop_opções_execução():
    sair_loop = False
    cabeçalho_bolsa_armas_itens = ('\nBolsa : id - peso máximo'
    + '\n - Armas : nome - dano - peso - tipo'
    + '\n - Itens : nome - peso - valor - quantidade')

    cabeçalho_caminho_mágico_magias = ('\nCaminho Mágico : nome - magia tipo'
    + '\n - Magias :  nome - nível dificuldade - dano - utiliza componente')

    cabeçalho_ser_magico = ('\nSer Mágico : nome - habilidade_mágica - '
                            'monstro:[tipo_fera - fraqueza - origem] | raça inteligente:[tendência - habilidade_unica - habitat]')

    cabeçalho_personagem = ('\nPersonagem : nome - nivel - classe - pontos_vida - pontos_forca - bolsa - caminho_magico - ser_magico')

    while not sair_loop:
        print()
        operação = ler_str('Opções [C: Cadastrar / I: Imprimir / S: Selecionar / T: imprimir Todos / <ENTER>: Parar]', retornar=True)
        if operação == None: break
        elif operação in ('C','I'):
            opção_conteúdo = ler_str('SM: Ser Mágico / C: Caminho Mágico / B: Bolsa / P: Personagem / <ENTER>: retornar]',retornar=True)
            if opção_conteúdo == None: pass
            elif opção_conteúdo == 'SM':
                if operação == 'C': loop_leitura_seres_mágicos()
                imprimir_objetos(cabeçalho_ser_magico, get_seres_magicos().values())
            elif opção_conteúdo == 'C':
                if operação == 'C': loop_leitura_caminhos_mágicos()
                imprimir_objetos(cabeçalho_caminho_mágico_magias, get_caminhos().values())
            elif opção_conteúdo == 'B':
                if operação == 'C': loop_leitura_bolsas()
                imprimir_objetos(cabeçalho_bolsa_armas_itens, get_bolsas().values())
            elif opção_conteúdo == 'P':
                if operação == 'C': loop_leitura_personagens()
                imprimir_objetos(cabeçalho_personagem, get_personagens())
        elif operação == 'S': loop_seleção_personagens()
        elif operação == 'T':
            imprimir_objetos(cabeçalho_ser_magico, get_seres_magicos().values())
            imprimir_caminho_mágico_magias(cabeçalho_caminho_mágico_magias)
            imprimir_cabeçalho_bolsa_armas_itens(cabeçalho_bolsa_armas_itens)
            imprimir_objetos(cabeçalho_personagem, get_personagens())

def imprimir_cabeçalho_bolsa_armas_itens(cabeçalho_bolsa_armas_itens):
    print(cabeçalho_bolsa_armas_itens)
    for índice, bolsa in enumerate(get_bolsas().values()):
        imprimir_objeto(índice=índice, objeto_str=str(bolsa))
        imprimir_objetos_internos(bolsa.armas.values())
        imprimir_objetos_internos(bolsa.itens.values())

def imprimir_caminho_mágico_magias(cabeçalho_caminho_mágico_magias):
    print(cabeçalho_caminho_mágico_magias)
    for índice, caminho in enumerate(get_caminhos().values()):
        imprimir_objeto(índice=índice, objeto_str=str(caminho))
        imprimir_objetos_internos(caminho.magias.values())

def selecionar_personagens():
    filtros = '\nFiltros -- '

    nivel_max = ler_int_positivo('LV máximo de Personagem:', filtro=True)
    if nivel_max is not None: filtros += 'LV máximo de Personagem: ' + str(nivel_max )
    peso_max_bolsa = ler_int_positivo('peso máximo da Bolsa:', filtro=True)
    if peso_max_bolsa is not None: filtros += ' | peso máximo da Bolsa: ' + str(peso_max_bolsa)
    magia_tipo_caminhoMágico = ler_magia_tipo_caminho()
    if magia_tipo_caminhoMágico is not None: filtros += '| caminhoMágico do tipo: ' + magia_tipo_caminhoMágico
    nivel_max_dificuldade_magia = ler_int_positivo('LV máximo mágia: ', filtro=True)
    if nivel_max_dificuldade_magia is not None: filtros += '| LV máximo mágia: ' + str(nivel_max_dificuldade_magia)
    dano_max_arma = ler_int_positivo('Max damage Armas: ', filtro=True)
    if dano_max_arma is not None: filtros += '| Max damage Armas: ' + str(dano_max_arma)
    peso_max_itens = ler_int_positivo('Valor máximo dos itens: ', filtro=True)
    if peso_max_itens is not None: filtros += '\n| Valor máximo dos itens: ' + str(peso_max_itens)
    habilidade_max_ser_magico = ler_int_positivo('Habilidade máxima do ser mágico:', filtro=True)
    if habilidade_max_ser_magico is not None: filtros += ' | Habilidade máxima do ser mágico: ' + str(habilidade_max_ser_magico)
    fraqueza_monstro = ler_fraqueza_monstro()
    if fraqueza_monstro is not None: filtros += ('| Fraqueza monstro: ' + fraqueza_monstro)
    tendencia_raca_inteligente = ler_tendência_raça_inteligente()
    if tendencia_raca_inteligente is not None: filtros += ('| Tendencia raça: ' + tendencia_raca_inteligente)

    personagens_selecionados = filtrar_personagens(nivel_max , peso_max_bolsa ,magia_tipo_caminhoMágico, nivel_max_dificuldade_magia,dano_max_arma, peso_max_itens, habilidade_max_ser_magico , fraqueza_monstro ,tendencia_raca_inteligente)
    return filtros,personagens_selecionados



def loop_seleção_personagens():
    sair_loop = False
    print('--- Seleção de Personagens ---')
    while not sair_loop:
        filtros, personagens_selecionados = selecionar_personagens()
        if filtros is not None:
            cabeçalho = ('Personagem: nome - nivel - classe - pontos_vida - pontos_forca - bolsa - caminho_magico'
                         + '\n -- nível máximo de Personagem - peso máximo da Bolsa - CaminhoMágico do tipo - Nivel máximo das mágias - Dano máximo das Armas '
                         + '\n -  Valor máximo dos itens - Habilidade máxima do ser mágico - Monstro:[fraqueza] | RaçaInteligente:[tendência]')
            imprimir_objetos_associação_filtros(cabeçalho, personagens_selecionados, filtros)
        sair_loop = ler_sair_loop('seleção de personagens')

def loop_leitura_personagens():
    sair_loop = False
    print('--- Leitura de Dados do Personagem ---')
    while not sair_loop:
        personagem = ler_personagem()
        if personagem is not None: inserir_personagem(personagem)
        else: print(' - ERRO : na leitura do personagem')
        sair_loop = ler_sair_loop('cadastro do personagem')

def loop_leitura_seres_mágicos():
    sair_loop = False
    print('--- Leitura de Dados dos Seres Mágicos ---')
    while not sair_loop:
        ser = ler_ser_magico()
        if ser is not None: inserir_ser_magico(ser)
        else: print(' - ERRO : na leitura de ser mágico')
        sair_loop = ler_sair_loop('cadastro de ser mágico')
def loop_leitura_caminhos_mágicos():
    sair_loop = False
    print('--- Leitura de Dados de Caminhos Mágicos ---')
    while not sair_loop:
        caminho = ler_caminho()
        if caminho is not None:
            inserir_caminho(caminho)
            loop_leitura_magias_caminho(caminho)
        else: print(' - ERRO : na leitura do caminho mágico')
        sair_loop = ler_sair_loop('cadastro de Caminho mágico')

def loop_leitura_magias_caminho(caminho):
    sair_loop = False
    print('--- Leitura de Dados das Magias do Caminho mágico : ' + caminho.nome + ' ---')
    while not sair_loop:
        magia = ler_magia()
        if magia is not None:
            caminho.inserir_magias(magia)
        else: print(' - ERRO : na leitura da magia')
        sair_loop = ler_sair_loop('cadastro de magias do caminho')

def loop_leitura_bolsas():
    sair_loop = False
    print('--- Leitura de Dados da Bolsa ---')
    while not sair_loop:
        bolsa = ler_bolsa()
        if bolsa is not None:
            inserir_bolsa(bolsa)
            loop_leitura_armas_bolsa(bolsa)
            loop_leitura_itens_bolsa(bolsa)
        else: print(' - ERRO : na leitura da bolsa')
        sair_loop = ler_sair_loop('cadastro da bolsa')

def loop_leitura_armas_bolsa(bolsa):
    sair_loop = False
    print('--- Leitura de Dados das Armas da bolsa : ' + bolsa.id + ' ---')
    while not sair_loop:
        arma = ler_arma()
        if arma is not None: bolsa.inserir_arma(arma)
        else: print(' - ERRO : na leitura da arma')
        sair_loop = ler_sair_loop('cadastro de arma da bolsa')

def loop_leitura_itens_bolsa(bolsa):
    sair_loop = False
    print('--- Leitura de Dados dos Itens da bolsa : ' + bolsa.id + ' ---')
    while not sair_loop:
        item = ler_item()
        if item is not None:  bolsa.inserir_itens(item)
        else: print(' - ERRO : na leitura do item')
        sair_loop = ler_sair_loop('cadastro de itens da bolsa')


def ler_personagem():
    nome_personagem = ler_str('nome do personagem')
    if nome_personagem == None: return None
    nivel_personagem = ler_int_positivo('nivel do personagem')
    if nivel_personagem == None: return None
    classe_personagem = ler_classe_personagem()
    if classe_personagem == None: return None
    pontos_vida_personagem = ler_int_positivo('pontos de vida do personagem')
    if pontos_vida_personagem is None: return None
    pontos_forca_personagem = ler_int_positivo('pontos de força do personagem')
    if pontos_forca_personagem is None: return None
    id_bolsa = ler_str('id da bolsa')
    if id_bolsa is None: return None
    nome_caminho_magico = ler_str('nome do caminho mágico')
    if nome_caminho_magico == None: return None
    nome_ser_magico = ler_str('nome do ser mágico')
    if nome_ser_magico == None: return None

    return criar_personagem(nome_personagem, nivel_personagem, classe_personagem, pontos_vida_personagem,pontos_forca_personagem, id_bolsa,nome_caminho_magico, nome_ser_magico)

def ler_ser_magico():
    nome = ler_str('nome do ser mágico')
    if nome == None: return None
    habilidade_mágica = ler_int_positivo('habilidade mágica do ser mágico')
    if habilidade_mágica == None: return None


    tipo_ser_magico = ler_str('Tipo do ser mágico [M=Monstro / R=Raça Inteligente]')
    if tipo_ser_magico == 'M':
        tipo_fera = ler_str('nome do tipo da fera')
        if tipo_fera == None: return None
        fraqueza = ler_fraqueza_monstro()
        if fraqueza == None: return None
        origem = ler_str('origem da fera')
        if origem == None: return None
        return Monstro(nome, habilidade_mágica, tipo_fera, fraqueza, origem)

    if tipo_ser_magico == 'R':
        tendência = ler_tendência_raça_inteligente()
        if tendência == None: return None
        habilidade_unica = ler_str('habilidade única da raça inteligente')
        if habilidade_unica == None: return None
        habitat = ler_str('habitat da raça inteligente')
        if habitat == None: return None
        return RaçaInteligente(nome, habilidade_mágica, tendência, habilidade_unica, habitat)

def ler_bolsa():
    id = ler_str('id da bolsa')
    if id == None: return None
    peso_max = ler_int_positivo('peso máximo da bolsa')
    if peso_max == None: return None
    return Bolsa(id, peso_max)

def ler_arma():
    nome = ler_str('nome da arma')
    if nome == None: return None
    dano = ler_int_positivo('dano da arma')
    if dano == None: return None
    peso = ler_int_positivo('peso da arma')
    if peso == None: return None
    tipo = ler_tipo_arma()
    if tipo == None: return None
    return Arma(nome, dano, peso, tipo)

def ler_item():
    nome = ler_str('nome do item')
    if nome == None: return None
    peso = ler_int_positivo('peso do item')
    if peso == None: return None
    valor = ler_int_positivo('valor do item')
    if valor == None: return None
    quantidade = ler_int_positivo('quantidade do item')
    if quantidade == None: return None
    return Item(nome, peso, valor, quantidade)
def ler_caminho():
    nome = ler_str('nome do caminho')
    if nome == None: return None
    magia_tipo = ler_magia_tipo_caminho()
    if magia_tipo == None: return  None
    return CaminhoMagico(nome,magia_tipo)

def ler_magia():
    nome = ler_str('nome da magia')
    if nome == None: return None
    nível_dificuldade = ler_int_positivo('dificuldade da magia')
    if nível_dificuldade == None: return None
    dano = ler_str('dano da magia')
    if dano == None: return None
    utiliza_componente = ler_bool('magia utiliza componente')
    if utiliza_componente == None: return None
    return Magia(nome, nível_dificuldade, dano, utiliza_componente)


def ler_sair_loop(loop):
    try:
        sair = input('-- sair do loop de ' + loop + ' [S]: ')
        if sair == 'S': return True
    except IOError: pass
    return False

def ler_str(dado, filtro=False, retornar=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and (filtro or retornar): return None
        if len(string) > 0: return string
    except IOError: pass
    print('Erro na leitura do dado: ' + dado)
    return None

def ler_int_positivo(dado, filtro=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and filtro: return None
        int_positivo = int(string)
        if int_positivo >= 0: return int_positivo
    except ValueError: pass
    print('Erro na leitura/conversão do inteiro positivo: ' + dado)
    return None

def ler_float_positivo(dado, filtro=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and filtro: return None
        float_positivo = float(input('- ' + dado + ' : '))
        if float_positivo > 0.0: return float_positivo
    except ValueError: pass
    print('Erro na leitura/conversão do flutuante positivo: ' + dado)
    return None

def ler_bool(dado, filtro=False):
    try:
        string = input('- ' + dado + ' [S/N]: ')
        if len(string) == 0 and filtro: return None
        if string == 'S': return True
        elif string == 'N': return False
    except ValueError: pass
    print('Erro na leitura do booleano: ' + dado)
    return None


def ler_tipo_arma(filtro=False):
    try:
        string = input('- tipo da arma [E=espada / A=arco / M=machado / AG=adaga / C=cajado]: ')
        if len(string) == 0 and filtro: return None
        if string == 'E': return 'Espada'
        if string == 'A': return 'Arco'
        if string == 'M': return 'Machado'
        if string == 'AG': return 'Adaga'
        if string == 'C': return 'Cajado'
    except IOError: pass
    print('Erro na leitura do tipo da arma')
    return None

def ler_magia_tipo_caminho(filtro=False):
    try:
        string = input('- tipo da magia do caminho [AG=água / T=terra / F=fogo / AR=ar / E=estranha]: ')
        if len(string) == 0 and filtro: return None
        if string == 'AG': return 'água'
        if string == 'T': return 'terra'
        if string == 'F': return 'fogo'
        if string == 'AR': return 'ar'
        if string == 'E': return 'estranha'

    except IOError:
        pass
        print('Erro na leitura do tipo da magia do caminho')
        return None

def ler_classe_personagem(filtro=False):
    try:
        string = input('- classe do personagem [I=insano / M=mago / F=feiticeiro / IV=inventor / G=guerreiro]: ')
        if len(string) == 0 and filtro: return None
        if string == 'I': return 'Insano'
        if string == 'M': return 'Mago'
        if string == 'F': return 'Feiticeiro'
        if string == 'IV': return 'Inventor'
        if string == 'G': return 'Guerreiro'
    except IOError:
        pass
        print('Erro na leitura da classe do personagem')
        return None

def ler_fraqueza_monstro(filtro=False):
    try:
        string = input('- fraqueza do monstro [RE=Ruídos estridentes / MG=Magias de gelo / C=Corte / AR=Ar / E=Eletricidade]: ')
        if len(string) == 0 and filtro: return None
        if string == 'RE': return 'Ruídos estridentes'
        if string == 'MG': return 'Magias de gelo'
        if string == 'C': return 'Corte'
        if string == 'AR': return 'Ar'
        if string == 'E': return 'Eletricidade'
    except IOError:
        pass
        print('Erro na leitura da fraqueza do monstro')
        return None

def ler_tendência_raça_inteligente(filtro=False):
    try:
        string = input('- tendência da raça inteligente [B=Boa / C=Caótico / N=Neutra]: ')
        if len(string) == 0 and filtro: return None
        if string == 'B': return 'Boa'
        if string == 'C': return 'Caótico'
        if string == 'N': return 'Neutra'
    except IOError:
        pass
        print('Erro na leitura da tendência da raça inteligente')
        return None