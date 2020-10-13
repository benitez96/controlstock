import pprint

class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        


    def __add__(self, b):
      return Punto(self.x + b.x, self.y + b.y)
  

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
    
class Rectangulo():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # Esquinas
        self.esquina = {
            'inf_der' : Punto(max(p1.x, p2.x), min(p1.y, p2.y)),
            'sup_der' : Punto(max(p1.x, p2.x), max(p1.y, p2.y)),
            'inf_izq' : Punto(min(p1.x, p2.x), min(p1.y, p2.y)),
            'sup_izq' : Punto(min(p1.x, p2.x), max(p1.y, p2.y)),
            }
        
    def base(self):
        return abs(self.p1.x - self.p2.x)
    
    def altura(self):
        return abs(self.p1.y - self.p2.y)
    
    def area(self):
        return self.base() * self.altura()
    
    def posicion_relativa(self):
        for k, esquina in self.esquina.items():

            if esquina.__repr__() == self.p1.__repr__():
                bandera_p1 = k
            if esquina.__repr__() == self.p2.__repr__():
                bandera_p2 = k
        
        return bandera_p1, bandera_p2
                
                
    def rotar(self):
        b1, b2 = self.posicion_relativa()
        
        self.esquina['sup_der'] += Punto(self.altura(),  -self.altura())
        self.esquina['inf_izq'] += Punto(self.base(), self.base())
        self.esquina['sup_izq'] += Punto(self.base()+self.altura(), -self.altura()+self.base())
        
        self.p1 = self.esquina[b1]
        self.p2 = self.esquina[b2]
        
        return self.p1, self.p2
        
        
    def desplazar(self, desplazamiento):
        
        self.p1 += desplazamiento
        self.p2 += desplazamiento
        return self.p1, self.p2
        
        
        
    def __str__(self):
        return f'Rectangulo -> base:{self.base()} , altura: {self.altura()}'
    
    def __repr__(self):
        return f'Rectangulo({self.p1.__repr__()}, {self.p2.__repr__()})'
    
r1 = Rectangulo(Punto(1, 2), Punto(3, 9))
print('P1 -> ', r1.p1)
print('P2 -> ', r1.p2)
pprint.pprint(r1.esquina)
r1.rotar()
print('{:*^40}'.format('Rotacion'))
pprint.pprint(r1.esquina)
print('P1 -> ', r1.p1)
print('P2 -> ', r1.p2)
