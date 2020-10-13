from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def reparar(df):
    '''La siguiente función completa datos faltantes y corrige pequeños
    problemas en los índices.'''
    df = df.interpolate()
    df = df.resample('H').mean()
    df = df.fillna(method = 'ffill')
    return df


def calcular_fft(y, freq_sampleo = 24.0):
    '''y debe ser un vector con números reales
    representando datos de una serie temporal.
    freq_sampleo está seteado para considerar 24 datos por unidad.
    Devuelve dos vectores, uno de frecuencias 
    y otro con la transformada propiamente.
    La transformada contiene los valores complejos
    que se corresponden con respectivas frecuencias.'''
    N = len(y)
    freq = np.fft.fftfreq(N, d = 1/freq_sampleo)[:N//2]
    tran = (np.fft.fft(y)/N)[:N//2]
    return freq, tran


df_zar = pd.read_csv('Data/OBS_Zarate_2013A.csv', index_col=['Time'], parse_dates= True)
df_zar = reparar(df_zar)


df_ba = pd.read_csv('Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates= True)
df_ba = df_ba['H_BA']













