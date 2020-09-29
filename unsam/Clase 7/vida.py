import datetime


def segundos_vividos(fecha):
    '''Esta funcion recibe un string con una fecha y devuelve el 
    tiempo transcurrido hasta el momento en segundos.
    pre: El string debe ser de la forma "dd/mm/yyyy"
    pos: Se devuelve un objeto timedelta en seg'''
    
    f_inicio = datetime.datetime.strptime(fecha, '%d/%m/%Y')
    f_actual = datetime.datetime.now()
    tiempo_transcurrido = f_actual - f_inicio
    
    return tiempo_transcurrido.total_seconds()