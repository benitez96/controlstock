class Canguro:
    
    def __init__(self, nombre, contenido_marsupio=[]):
        self.contenido_marsupio = contenido_marsupio
        self.nombre = nombre
        
    
    
    def meter_en_marsupio(self, obj):
        self.contenido_marsupio.append(obj)
        
        
    def __str__(self):
        return f'El canguro {self.nombre}, contiene {self.contenido_marsupio}'
    
    def __repr__(self):
        return f'Canguro {self.nombre}'
    
    

# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido[:]  #Aqui estaba el bug, ambas instancias
                                                #Apuntaban a la misma dir de mem para contenido.
                                                
    
    def __repr__(self):
        return f"'{self.nombre}'"

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        self.t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            self.t.append(s)
        return '\n'.join(self.t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.