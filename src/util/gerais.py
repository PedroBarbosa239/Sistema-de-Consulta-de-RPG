def imprimir_objetos(cabeçalho, objetos, filtros=None):
    if filtros is not None: print(filtros)
    print(cabeçalho)
    for índice, objeto in enumerate(objetos):
        imprimir_objeto(índice, str(objeto))

def imprimir_objeto(índice, objeto_str):
    formato = '{} {} {}'
    ordem = índice + 1
    separador = '-'
    string_formatado = formato.format(f'{ordem:2d}', separador, objeto_str)
    print(string_formatado)


def imprimir_objetos_associação_filtros(cabeçalho, objetos, filtros=None):
    if filtros is not None: print(filtros)
    print(cabeçalho)
    for índice, objeto in enumerate(objetos):
     imprimir_objeto(índice, objeto.str_filtro())

def imprimir_objetos_internos(objetos):
    for objeto in objetos: print(' - ' + str(objeto))