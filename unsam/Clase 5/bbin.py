def busqueda_binaria(lista, x, verbose = False):
    '''Busqueda binaria
    Precondicion: la lista esta ordenada
    Devuelve -1 si x no esta en lista;
    Devuelve p tal que lista[p] == x, si x esta en lista
    '''
    if verbose:
        print('[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:       
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

#%%
def donde_insertar(lista, x):
    
    pos = None # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    descartado = None
    while izq <= der:
        medio = (izq + der) // 2
        
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            return pos
            
        if lista[medio] > x:
            descartado = 'der'
            der = medio - 1 # descarto mitad derecha
            
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            descartado = 'izq'
    
    if descartado == 'izq':
        pos = medio + 1    
    else:
        pos = medio
              
    return pos    
    
#%%
def insertar(lista,e):
    """ recibe una lista ordenada l y un elemento y e. Si el elemento se 
    encuentra en la lista solamente devuelve su posición; si no se encuentra 
    en la lista, lo inserta en la posición correcta para mantener el orden."""
    
    pos = None # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    descartado = None
    while izq <= der:
        medio = (izq + der) // 2
        
        if lista[medio] == e:
            pos = medio     # elemento encontrado!
            return pos
            
        if lista[medio] > e:
            descartado = 'der'
            der = medio - 1 # descarto mitad derecha
            
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            descartado = 'izq' 
    
    if descartado == 'izq':
        pos = medio + 1
        lista.insert(pos, e)
    else:
        pos = medio
        lista.insert(pos, e)
        
    return pos
    