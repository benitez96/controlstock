import datetime as dt

#%% Ejercicio 7.2: Cuánto falta
def dias_primavera():
    
    hoy = dt.date.today()
    
    if hoy < dt.date(hoy.year, 9, 21) :
        primavera = dt.date(hoy.year, 9, 21)
    elif hoy < dt.date(hoy.year, 12, 21):
        return 'Estamos en primavera!'
        
    else:
        primavera = dt.date(hoy.year+1, 9, 21)
    
    
    tiempo_primavera = primavera - hoy
    
    return f'Faltan {tiempo_primavera.days} dias para que comience la primavera\
 nuevamente.'

#%% Ejercicio 7.3: Fecha de reincorporación 
def fin_licencia():
     
     inicio = dt.date(2020, 9, 26)
     dias_licencia = dt.timedelta(days=200)
     fin = inicio + dias_licencia
     
     return f'La licencia termina el {fin.strftime("%d - %m - %Y")}'
 
    
#%% Ejercicio 7.4: Días hábiles
import datetime as dt

feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']

def dias_habiles(inicio, fin, feriados=[]):
    
    l_feriados = list(map(lambda f : dt.datetime.strptime(f, '%d/%m/%Y'), feriados))
    d_inicio = dt.datetime.strptime(inicio, '%d/%m/%Y')
    d_fin = dt.datetime.strptime(fin, '%d/%m/%Y')
    d_fin += dt.timedelta(days=1) # Se debe incluir el ultimo dia
    dias_hab = []
    while d_inicio < d_fin:

        if d_inicio in l_feriados:
            d_inicio += dt.timedelta(days=1)
            continue
        if d_inicio.weekday()==6 or d_inicio.weekday()==5:
            d_inicio += dt.timedelta(days=1)
            continue
        dias_hab.append(d_inicio.strftime('%d-%m-%Y'))
        d_inicio += dt.timedelta(days=1)
        
    return dias_hab
 
    

print(dias_habiles('28/09/2020', '05/10/2020'))

#print(dias_habiles('28/09/2020', '31/12/2020', feriados))










