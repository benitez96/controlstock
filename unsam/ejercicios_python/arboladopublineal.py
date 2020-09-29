import numpy as np
import pandas as pd
import seaborn as sns


#%% Ejercicio 7.7: Lectura y selección
df_lineal = pd.read_csv('Data/arbolado-publico-lineal-2017-2018.csv')

cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']

df_lineal = df_lineal[cols_sel]

print(df_lineal['nombre_cientifico'].value_counts().head(10)) #10 especies mas repetidas

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

#como seleccionar especies
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]


#%% Ejercicio 7.8: Boxplots

df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')

df_lineal_seleccion.boxplot('altura_arbol', by='nombre_cientifico')

sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')

