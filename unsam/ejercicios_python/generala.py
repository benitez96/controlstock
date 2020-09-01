import random
from statistics import mode

def tirar():
    return [random.randint(1,6) for i in range(6)]

def es_generala(tirada):
    bandera = True
    for i in range(len(tirada)-1):
        if tirada[i]!=tirada[i+1]:
            bandera=False
            
    return bandera


def tirar_tres():
    tirada = tirar()
    n = 1
    while n<3:
        for i in range(len(tirada)):
            if tirada[i] != mode(tirada):
                tirada[i] = random.randint(1,6)
                n += 1 
            if n==3:
                break
    
    return tirada

a = tirar_tres()
    

N = 1000
G = sum([es_generala(tirar_tres()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')