def busqueda_binaria(lista, x, verbose = False):
    '''Busqueda binaria
    Precondicion: la lista esta ordenada
    Devuelve -1 si x no esta en lista;
    Devuelve p tal que lista[p] == x, si x esta en lista
    '''
    if verbose:
        print('[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    contador = 0
    while izq <= der:
        contador += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, contador

#%%BUSQUEDA SECUENCIAL
def busqueda_secuencial_(lista,e):
    '''Si e está en la lista devuelve el índice de su primer aparición, 
    de lo contrario devuelve -1.
    '''
    comps = 0 #inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 #sumo la comparación que estoy por hacer
        if z == e:
            pos = i
            break
    return pos, comps
#%% GENERAR LISTA 
import random

def generar_lista(n,m):
    l = random.sample(range(m),k=n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0,m-1)

#%%EXPERIMENTO BUSQUEDA LINEAL

def experimento_secuencial_promedio(lista,m,k):
    comps_tot = 0
    for _ in range(k):
        e = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,e)[1]

    comps_prom = comps_tot / k
    return comps_prom

#%%EXPERIMENTO BUSQUEDA BINARIA

def experimento_binario_promedio(lista,m,k):   
    comps_tot = 0
    for _ in range(k):
        e = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,e)[1]

    comps_prom = comps_tot / k
    return comps_prom

#%% PLOT BUSQUEDA SECUENCIAL
import matplotlib.pyplot as plt
import numpy as np

m = 10000
k = 1000

largos = np.arange(256)+1 #estos son los largos de listas que voy a usar
comps_promedio = np.zeros(256) #aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n,m) # genero lista de largo n
    comps_promedio[i] = experimento_secuencial_promedio(lista,m,k)

#ahora grafico largos de listas contra operaciones promedio de búsqueda.
# =============================================================================
# plt.plot(largos,comps_promedio,label='Búsqueda Secuencial')
# plt.xlabel("Largo de la lista")
# plt.ylabel("Cantidad de comparaiciones")
# plt.title("Complejidad de la Búsqueda")
# plt.legend()
# =============================================================================

#%%PLOT BUSQUEDA BINARIA

m = 10000
k = 1000

largos = np.arange(256)+1 #estos son los largos de listas que voy a usar
comps_promedio_b = np.zeros(256) #aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

for i, n in enumerate(largos):
    lista = generar_lista(n,m) # genero lista de largo n
    comps_promedio_b[i] = experimento_binario_promedio(lista,m,k)

#ahora grafico largos de listas contra operaciones promedio de búsqueda.
# =============================================================================
# plt.plot(largos,comps_promedio,label='Búsqueda Secuencial')
# plt.xlabel("Largo de la lista")
# plt.ylabel("Cantidad de comparaiciones")
# plt.title("Complejidad de la Búsqueda")
# plt.legend()
# =============================================================================

#%%PLOT BUSQUEDA LINEAL VS BINARIA
plt.plot(largos,comps_promedio_b,label='Busqueda Binaria')
plt.plot(largos,comps_promedio,label='Búsqueda Secuencial')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaiciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
