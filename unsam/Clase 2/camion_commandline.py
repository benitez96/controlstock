import csv, sys

def costo_camion(nombre_archivo):
    try:
        f = open(nombre_archivo)
        rows = csv.reader(f)
        next(rows)
        total = 0
        for row in rows:
            try:
                total += int(row[1]) * float(row[2])
            except:
                continue
        f.close()
        return f'Costo total: {total}'
    except:
        return 'El archivo cargado no cumple los requisitos del programa.'
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'
costo = costo_camion(nombre_archivo)
print(costo)
