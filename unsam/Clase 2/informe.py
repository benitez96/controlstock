import csv
def leer_camion(nombre_archivo):
    camion = list()
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            lote = {'nombre':row[0], 'cajones':int(row[1]), 'precio': float(row[2])}
            camion.append(lote)
    return camion
#%%
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
#%%
def hacer_informe(camion, pvp):
    p_camion = leer_camion(camion)
    p_venta = leer_precios(pvp)
    balance = 0
    total_camion = 0
    total_vendido = 0
    for i in p_camion:
        total_camion += i['precio']*i['cajones']
        if i['nombre'] in p_venta:
            balance += (float(p_venta[i['nombre']])-float(i['precio']))*int(i['cajones'])
            total_vendido += float(p_venta[i['nombre']])*int(i['cajones'])
    return f'Costo camion -> {total_camion}\nTotal vendido -> {total_vendido}\nBalance -> {balance}'
