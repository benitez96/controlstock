import webbrowser
import bs4, requests
import re
from tkinter import *


class Producto:

    def __init__(self, nombre, link):
        self.nombre = nombre.upper()
        self.link = link

    
        

    

    def verificar_link(self):
        return isinstance(self.getMercadoLibrePrice(self.link), float)
        
    def reingresar_link(self, comando):
        self.comando = comando
        
        self.ventana = Toplevel()
        self.ventana.title('Reingresar')
        self.ventana.geometry('300x200')
        Label(self.ventana, text=f'PRODUCTO: {self.nombre}!').pack()
        self.mensaje = Label(self.ventana, text='Link ingresado INCORRECTO.', fg='red')
        self.mensaje.pack()
        Label(self.ventana, text='Reingresar Link').pack()
        n_link = Entry(self.ventana)
        n_link.pack()
        print(n_link.get())
        Button(self.ventana, text='Verificar', command=lambda:self.update_link(n_link.get(), self.comando)).pack()
        Button(self.ventana, text='Ingresar nuevo link', command=self.comando, bg='blue').pack()

        if self.verificar_link():
            self.mensaje['text']= 'Link ingresado CORRECTO.'
            self.mensaje['fg'] = 'green'
            n_link['textvariable'] = StringVar(value=self.link)

        
        
            

    def getMercadoLibrePrice(self, productUrl):
        try:
            res = requests.get(productUrl)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, 'html.parser')
            elems = soup.select('span.price-tag-fraction:nth-child(3)')
            price = elems[0].text.strip()
            precio = re.sub(r'[\.-]','', price)
            return float(precio)
        except Exception as e:
            return e

    @property
    def precio(self):
        precio = self.getMercadoLibrePrice(self.link)
        return precio
  
    @property
    def precio_venta(self):
        precio_venta = self.precio / 0.8    # ganancia 20%
        return precio_venta
    

    def update_link(self, n_link, comando):
        self.link = n_link
        self.ventana.destroy()
        self.reingresar_link(self.comando)
        print(self.link)

