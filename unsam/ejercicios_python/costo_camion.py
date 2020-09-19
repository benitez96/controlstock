import informe
def costo_camion(archivo):
    camion = informe.leer_camion(archivo)
    costo = 0
    for cajon in camion:
        costo += cajon['precio']*cajon['cajones']
    return costo

def main(archivos):
    if len(archivos)!=2:
        raise SystemExit('Debe pasar un solo archivo camion.')
    else:
        costo = costo_camion(archivos[1])
        print(f'Costo total: {costo}')
        
if __name__ == '__main__':
    import sys
    main(sys.argv)