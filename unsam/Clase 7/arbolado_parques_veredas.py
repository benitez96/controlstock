import numpy as np
import pandas as pd
import seaborn as sns
import os
def comparar_arboles(especie_v, especie_p=especie_v):
    
    '''Esta funcion recibe el nombre cientifico de un arbol a comparar.
    En caso que haya diferencias en los nombres de cada archivo, se pasan
    ambos nombres.'''
    
    parques = os.path.join('Data', 'arbolado.csv')
    veredas = os.path.join('Data', 'arbolado-publico-lineal-2017-2018.csv')
    
    df_parques = pd.read_csv(parques)
    df_veredas = pd.read_csv(veredas)
    
    df_tipas_parques = df_parques[df_parques['nombre_cie']==especie_p][['diametro','altura_tot']].copy()
    df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico']==especie_v][['diametro_altura_pecho','altura_arbol']].copy()
    
    
    df_tipas_veredas = df_tipas_veredas.rename(columns={'diametro_altura_pecho':'diametro',
                                                        'altura_arbol':'altura_tot'})
    
    df_tipas_veredas['ambiente'] = 'vereda'
    df_tipas_parques['ambiente'] = 'parque'
    
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    
    df_tipas.boxplot('diametro',by = 'ambiente')
    
    df_tipas.boxplot('altura_tot',by = 'ambiente')


