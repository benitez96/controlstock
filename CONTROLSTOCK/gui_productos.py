from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
from productos import Producto
class CargaProductos:

    db_name = 'controlstock'
    



    def __init__(self, window):
        self.wind = window
        self.wind.title('CARGA DE PRODUCTOS')
        self.wind.geometry('840x500')

        #Contenedor Registro
        frame = LabelFrame(self.wind, text='REGISTRAR NUEVO PRODUCTO')
        frame.grid(row=0, column=0, columnspan=3, pady=20, )
        #Nombre Producto
        Label(frame, text='NOMBRE: ').grid(row=1, column=0)
        self.nombre = Entry(frame)
        self.nombre.focus()
        self.nombre.grid(row=1, column=1)
        Label(frame, text='LINK: ').grid(row=2, column=0)
        self.link = Entry(frame)
        self.link.grid(row=2, column=1)
        Label(frame, text='CANTIDAD: ').grid(row=3, column=0)
        self.cantidad = Entry(frame)
        self.cantidad.grid(row=3, column=1)
        #Boton Agregar Producto
        ttk.Button(frame, text='GUARDAR PRODUCTO', command=lambda:self.aniadir_producto()).grid(row=4, columnspan=2, sticky=W+E)
        
        #Mensaje Cargar



        #Tabla Productos
        self.tree = ttk.Treeview(self.wind,height=10)
        self.tree['columns']=('#1','#2', '#3')
        self.tree.grid(row=4, column=0, columnspan=3, padx=20)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='En stock', anchor=CENTER)
        self.tree.heading('#2', text='Precio ML', anchor=CENTER)
        self.tree.heading('#3', text='Precio Sugerido', anchor=CENTER)
        #Productos registrados
        self.get_productos()

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

    def get_productos(self):
        #Limpiar Tabla
        records = self.tree.get_children()
        for elem in records:
            self.tree.delete(elem)
        #Consulta datos
        query = 'SELECT * FROM PRODUCTOS'
        db_rows = self.run_query(query)
        #Relleno Tabla
        for id, nombre, cantidad, link, precio, precio_venta in db_rows:
            self.tree.insert('', 0, text=nombre, values=(cantidad, precio, precio_venta))

    def validar(self):
        return (len(self.nombre) != 0) and (len(self.link) != 0)

    def aniadir_producto(self):
        if self.validar:
            producto = Producto(self.nombre.get(), self.link.get())
            # query = 'SELECT * FROM PRODUCTOS'
            # db_rows = self.run_query(query)
            # for id, nombre, cantidad, link, precio, precio_venta in db_rows:
            #     if link == producto.link:
            #         query = 'UPDATE'


            query = 'INSERT INTO PRODUCTOS VALUES(NULL, ?, ?, ?, ?, ?)'
            
            parameters = (producto.nombre, self.cantidad.get(), producto.link, producto.precio, producto.precio_venta)
            self.run_query(query, parameters)
            
        else:
            print('Se requiere nombre y link')
        self.get_productos()


if __name__=='__main__':

    window = Tk()
    aplicacion = CargaProductos(window)
    window.mainloop()
