import csv
def costo_camion(archivo):
    f = open(archivo)
    rows = csv.reader(f)
    headers = next(rows)
    costo_total = 0
    for i, row in enumerate(rows, start=1):
        record = dict(zip(headers, row))
        try:
            n_cajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += n_cajones*precio
        except ValueError:
            print(f'Fila {i}: no pude interpretar: {row}')
    f.close()
    return f'Costo costo_total: {costo_total}'
