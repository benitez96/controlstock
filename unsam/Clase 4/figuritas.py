import random as rd
import numpy as np
import matplotlib.pyplot as plt


#%% CREAR ALBUM

def crear_album(figus_total):
        album = np.zeros(figus_total, dtype=int)
        return album
    
#%% ALBUM INCOMPLETO

def album_incompleto(A):
    return 0 in A

#%% COMPRAR FIGURITAS

def comprar_figu(figus_total):
    figurita = rd.randint(0,figus_total-1)
    return figurita

#%%

def cuantas_figus(figus_total):
    A = crear_album(figus_total)
    compras = 0
    while album_incompleto(A):
        f = comprar_figu(figus_total)
        A[f] += 1
        compras += 1
    return compras

#%%COMPRAR PAQUETE

def comprar_paquete(figus_total, figus_paquete):
    paquete = np.array([comprar_figu(figus_total) for _ in range(figus_paquete)])
    return paquete


#%%CUANTOS PAQUETES

def cuantos_paquetes(figus_total, figus_paquete):
    A = crear_album(figus_total)
    compras = 0
    while album_incompleto(A):
        paquete = comprar_paquete (figus_total, figus_paquete)
        for fig in paquete:
            A[fig] += 1
        compras += 1
    return compras
        
    


#%%pruebas 1

n_repeticiones = 100

l = np.array([cuantas_figus(6) for _ in range(n_repeticiones)])

print(f'Promedio: {np.mean(l):.2f}')

n_repeticiones=100

l = np.array([cuantas_figus(670) for _ in range(n_repeticiones)])
print('*'*40)
print(f'Promedio: {np.mean(l):.2f} cartas')
print('*'*40)

#%%pruebas 2
n_repeticiones = 100
figus_total = 670
figus_paquete = 5

l = np.array([cuantos_paquetes(figus_total, figus_paquete)
                               for _ in range(n_repeticiones)])

menos_850 = (l<=850).sum()

print(f'Menos de 850: {menos_850/n_repeticiones*100:.2f}')
print(f'Promedio: {np.mean(l):.2f} paquetes')

#%%

plt.hist(l, bins=15)

#%% PROBABILDAD 90%

percentil_90 = np.percentile(l, 90)

print(f'Se deben comprar al menos {percentil_90:.0f} paquetes para tener un\
       90% de chance de completar el album.')






