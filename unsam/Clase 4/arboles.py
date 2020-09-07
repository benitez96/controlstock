import csv
from collections import Counter
#%%
def leer_parque(nombre_archivo, parque):
    'devuelve una lista de arboles en un parque'
    arboles = list()
    with open(nombre_archivo, encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            lote = dict(zip(headers, row))
            if lote['espacio_ve'] == parque.upper():
                lote['altura_tot'] = float(lote['altura_tot'])
                arboles.append(lote)
    return arboles
#%%
def especies(lista_arboles):
    'esta funcion devuelve las especies presentes en un parque'
    especies = []
    for registro in lista_arboles:
        especies.append(registro['nombre_com'])
    especies = set(especies)
    return especies
#%%
def contar_ejemplares(lista_arboles):
    count = Counter()
    for registro in lista_arboles:
        count.setdefault(registro['nombre_com'], 0)
        count[registro['nombre_com']] += 1
    return count
#%%
def obtener_alturas(lista_arboles, especie):
    alturas = []
    for registro in lista_arboles:
        if registro['nombre_com'] == especie:
            alturas.append(registro['altura_tot'])
    return alturas
    #return f'Maximo -> {max(alturas)}, Promedio -> {round((sum(alturas)/len(alturas)), 2)}'
#%%
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for registro in lista_arboles:
        if registro['nombre_com'] == especie:
            inclinaciones.append(float(registro['inclinacio']))
    return inclinaciones
#%%
def especimen_mas_inclinado(lista_arboles):
    l_especies = especies(lista_arboles)
    l_inclinaciones = []
    for e in l_especies:
        inc_esp = obtener_inclinaciones(lista_arboles, e)
        inc_esp = max(inc_esp)
        l_inclinaciones.append((inc_esp, e))
    inc_max = max(l_inclinaciones)
    
    return inc_max
#%%
def especie_promedio_mas_inclinada(lista_arboles):
    l_especies = especies(lista_arboles)
    l_inclinaciones = []
    for e in l_especies:
        inc_esp = obtener_inclinaciones(lista_arboles, e)
        inc_esp = sum(inc_esp)/len(inc_esp)
        l_inclinaciones.append((inc_esp, e))
    inc_prom = max(l_inclinaciones)
    
    return inc_prom

#%%
def leer_arboles(nombre_archivo):
    with open (nombre_archivo, encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        arboleda = [{enc: valor for enc, valor in zip(headers, row)} for row
                    in rows]
    return arboleda


arboleda = leer_arboles('Data/arbolado.csv')
H=[float(arbol['altura_tot']) for arbol in arboleda]
H_jac = [float(arbol['altura_tot']) for arbol in arboleda if 
         arbol['nombre_com'] == 'Jacarandá']
HyD_jac = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in 
           arboleda if arbol['nombre_com'] == 'Jacarandá']


#%%
def medidas_de_especies(especies, arboleda):
    '''Esta funcion recibe una lista de arboles y una de especies. Devuelve un
    diccionario con su nombre(clave) y altura y diametro(valores)'''
    diccionario = {especie:[(float(arbol['altura_tot']), float(arbol['diametro']))
                for arbol in arboleda if arbol['nombre_com'] == especie] for
                especie in especies}
                                        
    return diccionario
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
dicc = medidas_de_especies(especies, arboleda)


#%% plotear altura jacaranda
import os
import matplotlib.pyplot as plt
nombre_archivo = os.path.join('Data', 'arbolado.csv')
arboleda = leer_arboles(nombre_archivo)
altos = [float(arbol['altura_tot']) for arbol in arboleda if 
         arbol['nombre_com'] == 'Jacarandá']
plt.hist(altos,bins=20)

#%%  scatterplot jacaranda h y d
import numpy as np
h = np.array([float(arbol['altura_tot']) for arbol in arboleda if 
         arbol['nombre_com'] == 'Jacarandá'])
d = np.array([float(arbol['diametro']) for arbol in arboleda if 
         arbol['nombre_com'] == 'Jacarandá'])

plt.scatter(d, h, c='red', alpha=0.5)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")

#%%

import os
import matplotlib.pyplot as plt
import numpy as np

nombre_archivo = os.path.join('Data', 'arbolado.csv')
arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)
colores = ['blue', 'green','red']
for i,z in enumerate(medidas):
    for h, d in medidas[z]:
        plt.scatter(x=d, y=h, alpha=0.4, c=colores[i])
        plt.xlabel("diametro (cm)")
        plt.ylabel("alto (m)")
        #plt.xlim(0,40) 
        #plt.ylim(0,80) 
        plt.title(list(medidas.keys())[i])
