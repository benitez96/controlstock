import numpy as np
import matplotlib.pyplot as plt



def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

def caminata_alejada(caminatas):
    
    dist_max = max(np.amax(abs(caminatas), axis=1))
        
    index = np.where(dist_max == np.amax(abs(caminatas), axis=1))[0][0]
    
    return index
    
"""    otra posibilidad pero sin numpy
    index = 0
    max_dist = 0
    for i, c in enumerate(caminatas):
        for value in c:
            if abs(value) > max_dist:
                max_dist = abs(value)
                index = i
    
    return index
"""


def caminata_cercana(caminatas):
    dist_min = min(np.amax(abs(caminatas), axis=1))
        
    index = np.where(dist_min == np.amax(abs(caminatas), axis=1))[0][0]
    
    return index
N = 100000

caminatas = np.array([randomwalk(N) for _ in range(12)])

colores = ('red',
           'blue',
           'brown',
           'green',
           'pink',
           'yellow',
           'orange',
           'peru',
           'crimson',
           'coral',
           'grey',
           'gold'
           )


plt.figure(figsize=(8, 6), dpi=90)

plt.subplot(2,1,1)
plt.title('12 Caminatas al azar')

for i, c in enumerate(colores):
    plt.plot(caminatas[i], linewidth=1, color=c, )

plt.ylim(-1000, 1000)
plt.yticks((-500, 0, 500))
plt.xticks([])

plt.subplot(2,2,3)   
plt.title('La caminata que mas se aleja')


plt.ylim(-1000, 1000)
plt.yticks((-500, 0, 500))
plt.xticks([])
plt.plot(caminatas[caminata_alejada(caminatas)], linewidth=1)

plt.subplot(2,2,4)
plt.title('La caminata que menos se aleja')

plt.plot(caminatas[caminata_cercana(caminatas)], linewidth=1)
plt.ylim(-1000, 1000)
plt.yticks((-500, 0, 500))
plt.xticks([])

plt.show()