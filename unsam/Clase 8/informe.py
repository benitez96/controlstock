# informe.py
from lote import Lote
import fileparse
from formato_tabla import crear_formateador, imprimir_tabla
#import lote
#%%
def leer_camion(nom_archivo):
    '''
    Lee un archivo de lotes en un camión 
    y lo devuelve como lista de objetos Lote con atributos
    nombre, cajones, precio.
    '''
    with open('Data/camion.csv') as lineas:
        camion_dicts = fileparse.parse_csv(lineas, select=['nombre', 'cajones', 'precio'], types=[str, int, float])
    
    
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion


def leer_precios(nom_archivo):
    '''
    Lee un archivo CSV con data de precios 
    y lo devuelve como un diccionario
    con claves nombres y con sus precios como valores
    '''
    with open(nom_archivo) as lines:
        return dict(fileparse.parse_csv(lines, types = [str,float], has_headers = False))
#%%
def hacer_informe(camion, precios):
    '''
    Crea una lista de tuplas (nombre, cajones, precio, cambio) 
    dada una lista de lotes en un camión y un diccionario de precios nuevos.
    '''
    filas = []
    for c in camion:
        precio_orig = c.precio
        cambio = precios[c.nombre] - precio_orig
        reg = (c.nombre, c.cajones, precio_orig, cambio)
        filas.append(reg)
    return filas
#%%
def imprimir_informe(data_informe, formateador):
    '''
    Imprime adecuadamente una tabla de una lista de tuplas
    (nombre, cajones, precio, cambio).
    '''
    formateador.encabezado(['Nombre', 'Cajones', 'Precio', 'Cambio'])

    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)
#%%
def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)
    
#%%
def main(args):
    if len(args) != 3 and len(args) != 4:
        raise SystemExit('Uso: %s archivo_camion archivo_precios' % args[0])
    if len(args)==3:
        informe_camion(args[1], args[2])
    else:
        informe_camion(args[1], args[2], args[3])
#%%
if __name__ == '__main__':
    import sys
    main(sys.argv)
