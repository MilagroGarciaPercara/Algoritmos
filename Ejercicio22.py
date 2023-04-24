def usar_la_fuerza(lista, buscado):
    if len(lista) == 0:
        return -1
    elif lista[-1] == buscado:
        return len(lista)-1
    else:
        return usar_la_fuerza(lista[0:-1], buscado)


lista = ['antidoto', 'sable de luz', 'traje termico', 'herramientas']

if 'sable de luz' in lista:
    print('Ha sido encontrado el sable de luz, después de sacar',
          usar_la_fuerza(lista, 'sable de luz'), 'objetos')
else:
    print('El sable de luz no fue encontrado')
