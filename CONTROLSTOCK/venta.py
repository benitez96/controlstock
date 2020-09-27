from tkinter import *
from searchtree import SearchWindow
from tkinter import ttk
import sqlite3

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
        #Ingreso productos
        self.ingresar_prod = Entry(self.window, width=50, font=('Verdana', 14) )
        self.ingresar_prod.place(x=90, y=417)
        self.ingresar_prod.focus()
        self.buscar = Button(self.window, text='Buscar\nProducto', command=lambda:self.buscar_prod())
        self.buscar.place(x=700,y=410)
        self.window.bind('<Return>', self.buscar_prod)



        #Tabla Productos
    def buscar_prod(self, event=None):
        self.wind = Toplevel()
        self.tree = ttk.Treeview(self.wind,height=10)
        self.tree['columns']=('#1','#2', '#3')
        self.tree.pack(side=LEFT)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='En stock', anchor=CENTER)
        self.tree.heading('#2', text='Precio ML', anchor=CENTER)
        self.tree.heading('#3', text='Precio Sugerido', anchor=CENTER)
        scrollbary = Scrollbar(self.wind, orient=VERTICAL)
        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        self.wind.bind("<Escape>", lambda *ignore: self.wind.destroy())
        #Productos registrados
        self.wind.bind()
        self.get_productos()
        

    def selection(self, event):
        selected = self.tree.item(self.tree.selection())
        
        self.selected = f'{id} - {l_name} {name}'        
        self.window.destroy()
        self.client['text'] = self.selected
        return self.selected

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_productos(self):
        #Limpiar Tabla
        self.wind.focus()
        records = self.tree.get_children()
        for elem in records:
            self.tree.delete(elem)
        #Consulta datos
        parameters=(f'%{self.ingresar_prod.get()}%',f'%{self.ingresar_prod.get()}%')
        query = 'SELECT * FROM PRODUCTOS WHERE nombre LIKE ? OR categoria LIKE ?'
        db_rows = self.run_query(query, parameters)
        #Relleno Tabla
        for id, nombre, cantidad, categoria, link, precio, precio_venta in db_rows:
            self.tree.insert('', id, text=nombre, values=(cantidad, precio, precio_venta))
        child_id = self.tree.get_children()[0]
        self.tree.selection_set(child_id) 
        self.tree.focus(child_id)
        
        


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
    