#! python3
import fileparse

def leer_camion(nombre_archivo):
    '''Recibe un archivo .csv con pedidos de un camion y devuelve un diccionario
    con el nombre, cajones, y precio del producto por cajonz'''
    with open(nombre_archivo, 'rt') as file:
        camion = fileparse.parse_csv(file, types=[str, int, float] )
    return camion

def leer_precios(nombre_archivo):
    '''recibe un archivo .csv de precios de productos y devuelve un diccionario
    con los productos y sus precios.'''
    with open(nombre_archivo, 'rt', encoding='UTF-8') as file:
        precios = fileparse.parse_csv(file, types=[str, float], has_headers=False)
        precios = dict(precios)
    
    return precios

def hacer_informe(camion, pvp):
    '''Este funcion recibe un dict camion y uno de precios de venta publico
    y devuelve un informe con el nombre, cantidad de cajones, precio de compra
    y la ganancia obtenida por cajon.'''
    tabla=list()

    for i in camion:
        tabla.append((i['nombre'], i['cajones'], pvp[i['nombre']],
                      round((pvp[i['nombre']]-i['precio']), 2)))
    
    return tabla


def imprimir_informe(informe):
    'Este funcion recibe un informe y devuelve una impresion formateada.'
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for nombre, cajon, precio, cambio in informe:
        print(f'{nombre:10s} {cajon:10d} {"$"+str(precio):>10s} {"$"+str(cambio):>10s}')
        
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    '''Recibe un archivo camion y uno precios y devuelve un informe impreso.'''

    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios( nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

def main(archivos):
    if len(archivos)!=3:
        raise SystemExit('Los parametros deben ser archivo_camion, archivo_precios')
    else:
        informe_camion(archivos[1], archivos[2])
    
if __name__ == '__main__':
    import sys
    main(sys.argv)
    
    