#%% FUNCION REALIZADA CON UN CICLO
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    sumatoria = 0
    if hasta >= desde:
        for n in range(desde, hasta+1):
            sumatoria += n #invariante
    
    return sumatoria

#%% FUNCION REALIZADA CON DIFERENCIA DE NUMEROS TRIANGULARES

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    t_desde = (desde * (desde - 1))/2 #numero triangular desde 
    # (-)para que incluya desde en el intervalo
    t_hasta = (hasta * (hasta + 1))/2 #numero triangular hasta
    sumatoria = t_hasta - t_desde
    return sumatoria

