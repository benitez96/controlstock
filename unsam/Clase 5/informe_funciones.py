
from fileparse import parse_csv

def leer_camion(nombre_archivo):
    '''Recibe un archivo .csv con pedidos de un camion y devuelve un diccionario
    con el nombre, cajones, y precio del producto por cajonz'''
    camion = parse_csv(nombre_archivo, types=[str, int, float])
    return camion

def leer_precios(nombre_archivo):
    '''recibe un archivo .csv de precios de productos y devuelve un diccionario
    con los productos y sus precios.'''
    precios = parse_csv(nombre_archivo, types=[str, float], has_headers=False)
    precios = dict(precios)
    return precios

def hacer_informe(camion, pvp):
    '''Este funcion recibe un dict camion y uno de precios de venta publico
    y devuelve un informe con el nombre, cantidad de cajones, precio de compra
    y la ganancia obtenida por cajon.'''
    tabla=list()

    for i in camion:
        tabla.append((i['nombre'], i['cajones'], pvp[i['nombre']], pvp[i['nombre']]-i['precio']))
    
    return tabla


def imprimir_informe(informe):
    'Este funcion recibe un informe y devuelve una impresion formateada.'
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in informe:
        print('%10s %10s %10.2f %10.2f' % row)
        
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    '''Recibe un archivo camion y uno precios y devuelve un informe impreso.'''

    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios( nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)
    
    
    