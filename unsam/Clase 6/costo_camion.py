from fileparse import parse_csv
def costo_camion(archivo):
    with open(archivo, 'rt') as file:
        camion = parse_csv(file, types=[str, int, float] )
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