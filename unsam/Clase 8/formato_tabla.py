
class FormatoTabla:
    
    
    
    def encabezado(self, headers):
        
        
        raise NotImplementedError()
        
    def fila(self, rowdata):
        
        
        
        raise NotImplementedError()
        
    
    
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
        
    
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
        
class FormatoTablaHTML(FormatoTabla):    
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def fila(self, data_fila):
         
        print('<tr>', end='')
        for d in data_fila:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
        
    
def crear_formateador(nombre):
    if nombre == 'txt':
        formateador = FormatoTablaTXT()
    elif nombre == 'csv':
        formateador = FormatoTablaCSV()
    elif nombre == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {nombre}')
    
    return formateador
    
    
def imprimir_tabla(camion, columnas, formateador):

    # Seteo encabezados
    formateador.encabezado(columnas)
    # Seteo filas
    for lote in camion:
        rowdata = [f'{getattr(lote, name)}' for name in columnas]
        formateador.fila(rowdata)
        
    
    
    
    