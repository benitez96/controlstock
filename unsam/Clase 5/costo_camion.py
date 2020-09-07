import informe_funciones as informe
def costo_camion(archivo):
    camion = informe.leer_camion(archivo)
    costo = 0
    for cajon in camion:
        costo += cajon['precio']*cajon['cajones']
    return costo
