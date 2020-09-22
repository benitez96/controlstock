import webbrowser
import bs4, requests
import re


class Producto:

    def __init__(self, nombre, link):
        self.nombre = nombre.upper()
        self.link = link
    
    def getMercadoLibrePrice(self, productUrl):
        res = requests.get(productUrl)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        elems = soup.select('span.price-tag-fraction:nth-child(3)')
        price = elems[0].text.strip()
        return price

    @property
    def precio(self):
        precio = self.getMercadoLibrePrice(self.link)
        precio = re.sub(r'[\.-]','', precio)
        return float(precio)
  
    @property
    def precio_venta(self):
        precio_venta = self.precio / 0.8 # ganancia 20%
        return precio_venta
    

    def update_link(self, n_link):
        self.link = n_link
        return self.link

