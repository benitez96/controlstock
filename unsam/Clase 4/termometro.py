import random


n=100 #poblacion

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
        
    
    
    
registros = [round(random.normalvariate(37.5,0.2), 2) for _ in range(n)]

print(f'el maximo registrado es: {max(registros)}')

print(f'el minimo registrado es: {min(registros)}')

print(f'el promedio registrado es: {sum(registros)/n:.2f}')

print(f'la mediana es: {calcular_cuartil(registros,2)}')
