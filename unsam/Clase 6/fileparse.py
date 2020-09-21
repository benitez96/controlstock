import csv

def parse_csv(nombre_archivo, select=None, types=None, has_headers=True, silence_errors=False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    if not has_headers and select:
        raise RuntimeError('Para seleccionar, necesito encabezados.')
    #with open(nombre_archivo, encoding='UTF-8') as f:
    filas = csv.reader(nombre_archivo)

    # Lee los encabezados del archivo
    if has_headers:
        encabezados = next(filas)

    # Si se indicó un selector de columnas,
    #    buscar los índices de las columnas especificadas.
    # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

    registros = [] #lista, cada registra se almacena como diccionario al final
    for i, fila in enumerate(filas, 1):
        if not fila:    # Saltear filas vacías
            continue
        # Filtrar la fila si se especificaron columnas
        if has_headers:
            if indices:
                fila = [fila[index] for index in indices]
        if types:   #Se asignan tipos a los datos.
            try:    
                fila = [func(val) for func, val in zip(types, fila) ]
            except Exception as e:
                if not silence_errors:
                    print(f'Fila {i}: No pude convertir {fila}')
                    print(f'Fila {i}-> MOTIVO: {e}')
                
        if has_headers:
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
        else:
            registro = tuple(fila)
        registros.append(registro)

    return registros

