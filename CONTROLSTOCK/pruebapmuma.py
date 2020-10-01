#Este es un comentarios
"""Este es un comentario
multilinea

"""

'''
TIPOS DE DATOS:
    - STRINGS
    - INTEGERS
    - FLOAT
    - TUPLES
    - LISTS - ESTRUCTURAS
    - BOOLEANS
    - DICTIONARY - ESTRUCTURAS
    - SETS - ESTRUCTURAS

'''
a = 'Esto es un string'
b = 5 #Esto es un entero
c = 5.0 #Esto es un flotante
d = ('hola', 5, 7.0)
e = ['hola', 5, 7.0]

f = 2-2 > 3 #returns False

# Diccionarios ---> {k1:v1, k2:v2, ..., kn:vn}
 
g = {
    'nombre':'muma',
    5:('hola', 15),
    'dni':294829323,    

}

h = {
    'hola',
    5,
    7,
    'hola',
    5,
    '15',

}
lista = [1,1,1,1,2,2,2,5,5,3,6,4,4,4]
valores_no_repetidos = set(lista)

lista = ['hola', 'como', 'estas']
palabras_lista = {}

# range(inicio, fin, pasos) --> range(1, 20, 2)--> 1,3,5,7,...


cadena = 'Hola, como como estas me llamo daniel'
letras = {}
for palabra in cadena.split(' '):
    letras.setdefault(palabra, 0)
    letras[palabra] += 1
    

