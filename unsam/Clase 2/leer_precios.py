import csv, pprint
def leer_precios(nombre_archivo):
    precios=dict()
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                precios[row[0]] = row[1]
            except IndexError:
                continue
        precios = list(zip(precios.values(), precios.keys()))
    return precios
