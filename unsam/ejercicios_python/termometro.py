import random
import numpy as np




def calcular_cuartil(registros, cuartil):
    c = cuartil
    posicion = int(c*n/4)
    cuartil = None
    registros.sort()
    if n%2 == 0:
        cuartil = round((registros[posicion]+registros[posicion+1])/2, 2)
    else:
        cuartil = registros[posicion]
        
    return cuartil
        
    
n=999 #poblacion    
    
registros = np.array([round(random.normalvariate(37.5,0.2), 2) for _ in range(n)])

np.save('Data/termometro', registros)

print(f'el maximo registrado es: {np.max(registros)}')

print(f'el minimo registrado es: {np.min(registros)}')

print(f'el promedio registrado es: {np.mean(registros):.2f}')

print(f'la mediana es: {calcular_cuartil(registros,2)}')
