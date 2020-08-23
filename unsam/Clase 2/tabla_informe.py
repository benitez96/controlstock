import csv

def leer_camion(nombre_archivo):
    camion = list()
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            lote = {'nombre':row[0], 'cant.':int(row[1]), 'precio': float(row[2])}
            camion.append(lote)
    return camion

def leer_precios(nombre_archivo):
    precios={}
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = float(row[1])
            except:
                continue
    return precios

def hacer_informe(camion, pvp):
    tabla=list()
    for i in camion:
        tabla.append((i['nombre'], i['cant.'], pvp[i['nombre']], pvp[i['nombre']]-i['precio']))
    return tabla


camion = leer_camion(r'C:\\Users\\DANIEL BENITEZ\\Desktop\\unsam\\ejercicios_python\\Data\\camion.csv')
precios = leer_precios(r'C:\\Users\\DANIEL BENITEZ\\Desktop\\unsam\\ejercicios_python\\Data\\precios.csv')
informe = hacer_informe(camion, precios)
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')

print('---------- ---------- ---------- ----------')
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {"$"+str(precio):>10s} {cambio:>10.2f}')
