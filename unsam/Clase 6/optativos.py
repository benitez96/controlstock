#%% 6.11: Grafico de barras.
import matplotlib.pyplot as plt
import numpy as np
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)


plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
plt.yticks([])
plt.xticks([])

for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
for x, y in zip(X, Y2):
    plt.text(x + 0.4, -(y + 0.20), '%.2f' % y, ha='center', va='bottom',)

plt.ylim(-1.25, +1.25)

#%% 6.12 Coordenadas Polares.

import matplotlib.pyplot as plt
import numpy as np


plt.axes([0, 0, 1, 1], polar=True )


N = 20
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)




for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)

    
    
    
#%% Ejercicio 6.13: Setear el color de un scatter plot
    
import matplotlib.pyplot as plt
import numpy as np


n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xticks([])
plt.yticks([])
plt.scatter(X, Y, c=np.arctan2(Y, X), alpha=0.4)

    
    
    
    
    
    



