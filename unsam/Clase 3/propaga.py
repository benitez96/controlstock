def propagar(lista):
    for i in range(len(lista)-1):
        if lista[i] == 1:
            if lista[i-1] == 0:
                lista[i-1] = 1
                propagar(lista)
            elif lista[i+1] == 0:
                lista[i+1] = 1
                propagar(lista)
    return lista
