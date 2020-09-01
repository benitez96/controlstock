# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:52:26 2020

@author: DANIEL BENITEZ
"""
import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y


def puntos_d_circulo(puntos):    
    puntos_dentro = []
    for x, y in puntos:
        if (x**2 + y**2) < 1:
            puntos_dentro.append((x, y))
    return puntos_dentro
        

def estimar_pi(n_puntos):
    puntos = [generar_punto() for _ in range(n_puntos)]
    M = len(puntos_d_circulo(puntos))
    pi = M*4/n_puntos
    
    return pi
    
print(f'pi es aproximadamente: {estimar_pi(100000)}')