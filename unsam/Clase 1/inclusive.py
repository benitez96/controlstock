frase = 'Los hermanos sean unidos porque ésa es la ley primera'
'Todos, tu también'
'¿cómo transmitir a los otros el infinito Aleph?'
'todos somos programadores'
palabras = frase.split()

for palabra in palabras:
    if palabra[-2] == 'o' :
        r_pal = list(palabra) #convertimos en lista cada string(de inmutable a mutable)
        r_pal[-2] = 'e' #cambiamos 'o' por 'e'
        palabras[palabras.index(palabra)] = ''.join(r_pal) #sustituimos en la lista original
    elif palabra[-1] == 'o' : #lo mismo pero para el caso que la 'o' esté en la última letra
        r_pal = list(palabra)
        r_pal[-1] = 'e'
        palabras[palabras.index(palabra)] = ''.join(r_pal)
frase_t = ' '.join(palabras)   
print(frase_t)

# ----- Otra posible solucion utlizando expresiones regulares ----- #
import re
frase_t = re.sub(r'o(s)?\b', r'e\1', frase)#(s)-> grupo 1

print(frase_t)