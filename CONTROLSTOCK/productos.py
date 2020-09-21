import webbrowser

class Producto:

    def __init__(self, nombre, link):
        self.nombre = nombre
        self.link = link
    
    
    @property
    def precio(self):
        return precio

    @precio.setter
    def precio(self):
        self.precio = self.link

    
    
    @property
    def precio_venta(self):
        precio_venta = self.precio / 0.8 # ganancia 20%
        return precio_venta
    
    
    
    
    @setter get_link
    def set_link(self, link):
        self.link = link
        return self.link

    def update_link(self, n_link):
        self.link = n_link
        return self.link