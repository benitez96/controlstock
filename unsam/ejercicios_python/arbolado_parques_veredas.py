import numpy as np
import pandas as pd
import seaborn as sns
import os

parques = os.path.join('Data', 'arbolado.csv')
veredas = os.path.join('Data', 'arbolado-publico-lineal-2017-2018.csv')

df_parques = pd.read_csv(parques)
df_veredas = pd.read_csv(veredas)

df_tipas_parques = df_parques[df_parques['nombre_cie']=='Tipuana Tipu'].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico']=='Tipuana tipu'].copy()


df_tipas_veredas = df_tipas_veredas.rename(columns={'nombre_cientifico':'nombre_cie',
                                                    'diametro_altura_pecho':'diametro',
                                                    'altura_arbol':'altura_tot'})




