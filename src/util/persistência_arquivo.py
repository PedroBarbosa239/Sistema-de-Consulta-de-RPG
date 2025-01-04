import pickle

def salvar_arquivo(nome_arquivo, objetos):
    arquivo = open('../../dados/' + nome_arquivo + '.bin', 'wb')
    pickle.dump(objetos, arquivo)
    arquivo.close()

def carregar_arquivo(nome_arquivo):
    try:
        arquivo = open('../../dados/' + nome_arquivo + '.bin', 'rb')
        objetos = pickle.load(arquivo)
    except IOError: objetos = None
    return objetos