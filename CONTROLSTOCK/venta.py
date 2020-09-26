from tkinter import *
from searchtree import SearchWindow
from tkinter import ttk
class Venta:
    def __init__(self, window):
        self.db_name = 'controlstock'

        self.window = window
        self.window.title('GESTION DE VENTAS')
        self.window.geometry('840x500')
        self.window.config(bg='#7bb7b6')
        Label(self.window, text='CLIENTE:').place(x=40, y=30)
        self.client = Label(self.window, bg='#669291', font=('arial', 12))
        self.client.place(x=120,y=30)
        Button(self.window, text='Buscar', command=lambda:self.search_client()).place(x=370, y=29)
        self.productos = ttk.Treeview(self.window)
        self.productos.place(x=90, y=100)
        self.productos['columns'] = ['ID', 'PRODUCTO', 'CANTIDAD','PRECIO REPO', 'PRECIO U', 'PRECIO TOTAL']
        self.productos.heading('ID', text='ID', anchor=CENTER)
        self.productos.heading('PRODUCTO', text='PRODUCTO', anchor=CENTER)
        self.productos.heading('CANTIDAD', text='CANTIDAD', anchor=CENTER)
        self.productos.heading('PRECIO REPO', text='PRECIO REPO', anchor=CENTER, )
        self.productos.heading('PRECIO U', text='PRECIO UNITARIO', anchor=CENTER)
        self.productos.heading('PRECIO TOTAL', text='PRECIO TOTAL', anchor=CENTER)
        self.productos.column('#0', stretch=NO, minwidth=0, width=0)
        self.productos.column('ID', stretch=NO, minwidth=0, width=50)
        self.productos.column('PRODUCTO', stretch=NO, minwidth=0, width=200)
        self.productos.column('CANTIDAD', stretch=NO, minwidth=0, width=80)
        self.productos.column('PRECIO REPO', stretch=NO, minwidth=0, width=100, )
        self.productos.column('PRECIO U', stretch=NO, minwidth=0, width=120)
        self.productos.column('PRECIO TOTAL', stretch=NO, minwidth=0, width=100)
        self.productos.tag_configure('PRECIO REPO', foreground='red')
        Label(self.window, text= 'TOTAL VENTA', font=('arial', 15)).place(x=475, y=340)
        self.total_venta = Label(self.window, text='', font=('arial', 15))
        self.total_venta.place(x=650, y=340)

        self.ingresar_prod = Entry()
        self.ingresar_prod.place(x=40, y=430)
        
        


    def search_client(self):
        window = Toplevel()
        self.s_app = SearchWindow(window, self.db_name, self.client)

    def calcular_total(self):
        total = 0
        for item in self.productos.get_children():
            total += float(self.productos.item(item)['values'][5])

        self.total_venta['text'] = total
        






if __name__ == '__main__':

    window = Tk()
    aplicacion = Venta(window)
    window.mainloop()
    