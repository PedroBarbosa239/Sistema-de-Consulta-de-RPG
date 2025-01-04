from util.persistência_arquivo import carregar_arquivo,salvar_arquivo
from entidades.personagem import get_personagens, set_personagens
from entidades.caminho_mágico import get_caminhos, set_caminhos
from entidades.bolsa import get_bolsas, set_bolsas
from entidades.ser_mágico import get_seres_magicos, set_seres_magicos
from interfaces.interface_textual import loop_opções_execução
nome_arquivo = 'personagens_campanha'


def salvar_aplicação():
    personagens_camapanha = []
    personagens_camapanha.append(get_bolsas())
    personagens_camapanha.append(get_caminhos())
    personagens_camapanha.append(get_seres_magicos())
    personagens_camapanha.append(get_personagens())
    salvar_arquivo(nome_arquivo, objetos=personagens_camapanha)

def recuperar_aplicação():
    personagens_camapanha = carregar_arquivo(nome_arquivo)
    if personagens_camapanha is not None:
        set_bolsas(personagens_camapanha[0])
        set_caminhos(personagens_camapanha[1])
        set_seres_magicos(personagens_camapanha[2])
        set_personagens (personagens_camapanha[3])


if __name__ == '__main__':
    recuperar_aplicação()
    loop_opções_execução()
    salvar_aplicação()
