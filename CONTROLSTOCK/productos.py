import webbrowser
import bs4, requests
import re
from tkinter import *


class Producto:

    def __init__(self, nombre, link):
        self.nombre = nombre.upper()
        self.link = link
        self.verificar_link(self.link)
    

    def verificar_link(self, link):
        self.verificacion = False
        if isinstance(self.getMercadoLibrePrice(link), float):
            self.verificacion = True
            return 
        else:
            self.ventana = Toplevel()
            self.ventana.title('Reingresar')
            self.ventana.geometry('300x200')
            Label(self.ventana, text='Link ingresado INCORRECTO.', fg='red').pack()
            Label(self.ventana, text='Reingresar Link').pack()
            n_link = Entry(self.ventana)
            n_link.pack()
            print(n_link.get())
            Button(self.ventana, text='Actualizar', command=lambda:self.update_link(n_link.get())).pack()


    


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
            print(e)

    @property
    def precio(self):
        precio = self.getMercadoLibrePrice(self.link)
        return precio
  
    @property
    def precio_venta(self):
        precio_venta = self.precio / 0.8 # ganancia 20%
        return precio_venta
    

    def update_link(self, n_link):
        self.link = n_link
        if self.verificacion:
            self.ventana.destroy()
        


