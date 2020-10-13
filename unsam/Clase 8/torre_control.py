class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
class TorreDeControl:
    def __init__(self):
        self.despegues = Cola()
        self.arribos = Cola()
        
    def nuevo_arribo(self, avion):
        self.arribos.encolar(avion)
        
    def nuevo_despegue(self, avion):
        self.despegues.encolar(avion)
    
    def ver_estado(self):
        arribos = f'Vuelos esperando para aterrizar: {", ".join(self.arribos.items)}'
        despegues = f'Vuelos esperando para despegar: {", ".join(self.despegues.items)}'
        return '{}.\n{}.'.format(arribos, despegues)
    
    def asignar_pista(self):
        if self.arribos.esta_vacia() and self.despegues.esta_vacia():
            return 'No hay vuelos en espera.'
        
        if not self.arribos.esta_vacia():
            avion = self.arribos.desencolar()
            return f'El vuelo {avion}, aterrizo con exito.'
        else:
            avion = self.despegues.desencolar()
            return f'El vuelo {avion}, despego con exito.'
        
        
        
        
     