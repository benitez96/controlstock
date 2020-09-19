def propagar(lista):
    for i in range(len(lista)):
        if lista[i] == 1:
            try:
                if lista[i-1] == 0:
                    lista[i-1] = 1
                    propagar(lista)
                elif lista[i+1] == 0:
                    lista[i+1] = 1
                    propagar(lista)
            except IndexError:
                continue
    return lista
