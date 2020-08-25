# ALGORITMOS DE BUSQUEDAS DE LISTAS
#%%

def buscar_u_elemento(lista, elemento):
    '''Busca la posicion de un elemento en una lista, devuelve
    su ultimo indice'''
    pos = -1
    for i in range(len(lista)-1, -1, -1):
        if elemento == lista[i]:
            pos = i
            return pos
    return pos

#%%

def buscar_n_elemento(lista, elemento):
    'Cuenta cuantas veces se repite un elemento en una lista'
    contador = 0
    for e in lista:
        if e == elemento:
            contador +=1
    return contador

#%%

def maximo(lista):
    'Recibe una lista y devuelve el valor maximo'
    m = lista[0]
    for e in lista:
        if e>m:
            m = e
    return m
#
#%%

def minimo(lista):
    'Recibe una lista y devulve el valor minimo'
    m = lista[0]
    for e in lista:
        if e<m:
            m = e
    return m


