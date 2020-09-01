#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era SEMANTICO, la funcion no pasaba solamente por la
#primer letra.
#    Lo corregí quitando el 'else' puesto que el 'return' hacia que la 
#funcion termine sin poder recorrer la palabra completa.
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))


#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de SINTAXIS y estaba ubicado en el 'return "Falso"'.
# En los ':' faltantes luego de la definicion de la funcion, el loop while y
# el if. Ademas en 'expesion[i] habia un solo '=' lo cual indica asignacion y
# NO comparacion.
def tiene_a2(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))


#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de TIPO y sucedio al pasar como argumento 1984
#puesto que los objetos int no tienen una funcion len().
#   Lo solucione transformando los argumentos pasados a str.
def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))

#%%
#Ejercicio 3.4: Alcances
#Comentario: El error era SEMANTICO puesto que la funcion suma() no retorna nada.
#   Lo solucione agregando 'return c'.
    
def suma(a,b):
    c = a + b
    return c
    
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5: Pisando memoria
#Comentario: El error era SEMANTICO puesto que se fueron almacenando variables
# y todas ellas apuntaban a la misma direccion de memoria.
#   Lo solucione realizando copias superficiales de cada registro durante el
# append. cambie 'camion.append(registro)' --> 'camion.append(dict(registro))'
    
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(dict(registro))
    return camion

camion = leer_camion('Data/camion.csv')
pprint(camion)
