import random as rd
import collections

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]


def robar_3(mazo):

    mano = rd.sample(mazo, k=3)
    
    return mano

def c_envido(mazo):
    naipes = robar_3(mazo)
    caras_r = [(p,r) for p, r in collections.Counter(c for v,c in naipes).items() if r>1]
    
    if len(caras_r) == 0:
        return max(naipes)[0]
    elif caras_r[0][1] == 2:
        sumatoria = 20
        for v, p in naipes:
            if p == caras_r[0][0]:
                if v<10:
                    sumatoria += v
        return sumatoria
    else:
        sumatoria = 20
        v_naipes = [v for v,p in naipes if v<10]
        v_naipes.sort(reverse=True)

        if len(v_naipes)>1:
            sumatoria += sum(v_naipes[:2])
        elif len(v_naipes) == 1:
            sumatoria += sum(v_naipes)
        else:
            pass
        return sumatoria
        
    
def envido_31(mazo):
    return c_envido(mazo)==31

def envido_32(mazo):
    return c_envido(mazo)==32
    
def envido_33(mazo):
    return c_envido(mazo)==33


print('*'*50)
N=10000
E = sum([envido_31(naipes) for i in range(N)])
prob = E/N
print(f'Jugue {N} manos, de las cuales {E} saqué envido 31.')
print(f'Podemos estimar que la probabilidad de sacar "31" es {round(prob*100, 2)}.')
print('*'*50)

E = sum([envido_32(naipes) for i in range(N)])
prob = E/N
print(f'Jugue {N} manos, de las cuales {E} saqué envido 32.')
print(f'Podemos estimar que la probabilidad de sacar "32" es {round(prob*100, 2)}.')
print('*'*50)

E = sum([envido_33(naipes) for i in range(N)])
prob = E/N
print(f'Jugue {N} manos, de las cuales {E} saqué envido 33.')
print(f'Podemos estimar que la probabilidad de sacar "33" es {round(prob*100, 2)}.')
print('*'*50)
 



