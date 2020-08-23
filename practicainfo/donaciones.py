class Producto:

    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def __repr__(self):
        return f'Producto: {self.nombre}.\t-> Cant.: {self.cantidad}'
    

class Perecedero(Producto):
    def __init__(self, nombre, cantidad, dias):
        super().__init__(nombre, cantidad)
        self.dias = dias



class noPerecedero(Producto):
    def __init__(self, nombre, cantidad, tipo):
        super().__init__(nombre, cantidad)
        self.tipo = tipo
  

class Entidad():
    def __init__(self, nombre):
        self.nombre = nombre

class Calculadora:
    
    l_entidades=[]
    l_productos=[]
       
    def entidades(self, entidad):
        Calculadora.l_entidades.append(entidad)
    
    def productos(self, productos):
        Calculadora.l_productos.append(productos)

    def calcular(self):
        alerta = None
        repartir = list()
        for p in Calculadora.l_productos:
            producto, cantidad = p.nombre, (p.cantidad//len(Calculadora.l_entidades))
            p.cantidad -= (cantidad*len(Calculadora.l_entidades))
            if isinstance(p, Perecedero):
                if p.dias<10:
                    alerta = 'Entrega Urgente'
                if p.dias>=10:
                    alerta = 'Entregar en el plazo de una semana'
                    repartir.append((producto, cantidad, alerta))
            else:
                alerta = 'Entregar dentro del mes'
                repartir.append((producto, cantidad, alerta))
        return repartir 

