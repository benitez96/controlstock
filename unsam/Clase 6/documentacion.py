def valor_absoluto(n):
    'Recibe Reales y devuelve el valor absoluto del mismo'    
    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    'Recibe una lista de enteros y devuelve la sumatoria de sus elementos pares'
    
    res = 0 
    for e in l:
        if e % 2 ==0:
            res += e #invariante
        else:
            res += 0 #invariante

    return res

def veces(a, b):
    'Recibe un numero (a) y devuelve la suma del mismo (b) veces.'
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res) -> invariante!
        res += a    #invariante
        nb -= 1     #invariante
    return res

def collatz(n):
    'Recibe un NATURAL y devuelve cuantos ciclos se necesitan para llegar a 1'
    
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2        #invariante
        else:
            n = 3 * n + 1   #invariante
        res += 1            #invariante

    return res