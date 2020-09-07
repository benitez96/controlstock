import matplotlib.pyplot as plt
import numpy as np

temperaturas = np.load('Data/termometro.npy')

plt.hist(temperaturas, bins=25)