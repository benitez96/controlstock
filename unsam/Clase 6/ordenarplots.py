import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot2grid((2,1),(0,0)) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot2grid((2,3),(1,1))
plt.plot([0,1], [1,1])
plt.xticks([]), plt.yticks([])

plt.subplot2grid((2, 3),(1,0)) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot2grid((2, 3), (1,2)) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()