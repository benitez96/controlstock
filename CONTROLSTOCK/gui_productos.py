from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
from productos import Producto
import pyperclip
class CargaProductos:

    db_name = 'controlstock'
    



    def __init__(self, window):
        self.wind = window
        self.wind.title('CARGA DE PRODUCTOS')
        self.wind.geometry('840x500')

        #Contenedor Registro
        frame = LabelFrame(self.wind, text='REGISTRAR NUEVO PRODUCTO')
        frame.grid(row=0, column=0, columnspan=4, pady=20, )
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
        self.cantidad.insert(END, 1)
        #Boton Agregar Producto
        ttk.Button(frame, text='GUARDAR PRODUCTO', command=lambda:self.aniadir_producto()).grid(row=4, columnspan=3, sticky=W+E)
        ttk.Button(frame, text='LIMPIAR FORMULARIO', command=lambda:self.clean_form()).grid(row=3, column=2)
        ttk.Button(frame, text='INSERTAR LINK', command=lambda:self.paste_link()).grid(row=2, column=2, sticky = E+W)
        #Mensaje Cargar
        self.mensaje = Label(frame, text='', fg='red')
        self.mensaje.grid(row=5, column=0, columnspan=4, sticky= W + E)


        #Tabla Productos
        self.tree = ttk.Treeview(self.wind,height=10)
        self.tree['columns']=('#1','#2', '#3')
        self.tree.grid(row=4, column=0, columnspan=4, padx=20)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='En stock', anchor=CENTER)
        self.tree.heading('#2', text='Precio ML', anchor=CENTER)
        self.tree.heading('#3', text='Precio Sugerido', anchor=CENTER)
        #Productos registrados
        self.get_productos()

        #Botones
        Button(text='ACTUALIZAR').grid(row= 6, column=0, sticky = E+W+N+S)
        Button(text='ACTUALIZAR\nTODOS', justify=CENTER).grid(row=6, column=1, sticky = E+W)
        Button(text='EDITAR', command=lambda:self.editar_producto()).grid(row=6, column=2, sticky = E+W+N+S)
        Button(text='BORRAR', command=lambda:self.eliminar_producto()).grid(row=6, column=3, sticky = E+W+N+S)


    
    
    #Funciones Botones
    def clean_form(self):
        self.nombre.delete(0, END)
        self.link.delete(0, END)

    def paste_link(self):
        self.link.insert(END, pyperclip.paste())

    def eliminar_producto(self):
        nombre = self.tree.item(self.tree.selection())['text']
        if len(nombre) == 0:
            self.mensaje['text'] = 'Debes Seleccionar un producto.'
            return
        query = 'DELETE FROM PRODUCTOS WHERE nombre = ?'
        self.run_query(query, (nombre, ))
        self.mensaje['text'] = f'SE ELIMINO "{nombre}" DE LA BASE DE DATOS'
        self.get_productos()


    def editar_producto(self):
        nombre = self.tree.item(self.tree.selection())['text']
        if len(nombre) == 0:
            self.mensaje['text'] = 'Debes Seleccionar un producto.'
            return
        precio = self.tree.item(self.tree.selection())['values'][1]
        precio_v = self.tree.item(self.tree.selection())['values'][2]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'EDITAR PRODUCTO'
        
        #Old name
        Label(self.edit_wind, text= 'Nombre Anterior: ').grid(row=0, column=0)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=nombre), state='readonly').grid(row=0, column=1)
        #New name
        Label(self.edit_wind, text= 'Nuevo Nombre: ').grid(row=1, column=0)
        n_nombre = Entry(self.edit_wind)
        n_nombre.grid(row=1, column=1)
        #Old precio
        Label(self.edit_wind, text= 'Precio Anterior: ').grid(row=2, column=0)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=precio), state='readonly').grid(row=2, column=1)
        #New precio
        Label(self.edit_wind, text= 'Nuevo precio: ').grid(row=3, column=0)
        n_precio = Entry(self.edit_wind)
        n_precio.grid(row=3, column=1)
        #Old precio_venta
        Label(self.edit_wind, text= 'Precio Venta Anterior: ').grid(row=4, column=0)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=precio_v), state='readonly').grid(row=4, column=1)
        #New precio_venta
        Label(self.edit_wind, text= 'Nuevo Precio Venta: ').grid(row=5, column=0)
        n_pv = Entry(self.edit_wind)
        n_pv.grid(row=5, column=1)
        
        Button(self.edit_wind, text='ACTUALIZAR', command=lambda:self.editar_registro(n_nombre.get(), nombre, n_precio.get(), precio, n_pv.get(), precio_v)).grid(row=6, column=1, sticky=W)

    def editar_registro(self, n_nombre, nombre, n_precio, precio, n_pv, precio_v):
        query= 'UPDATE PRODUCTOS SET nombre = ?, precio_ml = ?, precio_venta = ? WHERE nombre = ? AND precio_ml = ? AND precio_venta = ?'
        parameters=(n_nombre, n_precio, n_pv, nombre, precio, precio_v)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.mensaje['text'] = f'El registro {nombre}, ha sido actualizado.'
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
            self.tree.insert('', id, text=nombre, values=(cantidad, precio, precio_venta))

    def validar(self):
        return (len(self.nombre.get()) != 0) and (len(self.link.get()) != 0) and (len(self.cantidad.get()) !=0)

    def aniadir_producto(self):
        
        if self.validar():
            try:
                producto = Producto(self.nombre.get(), self.link.get())
            
                query = 'SELECT * FROM PRODUCTOS'
                #Si ya se encuentra registrado el producto se actualiza la cantidad
                db_rows = self.run_query(query)
                for id, nombre, cantidad, link, precio, precio_venta in db_rows:
                    if link == producto.link:
                        query = 'UPDATE PRODUCTOS SET CANTIDAD = ? WHERE link_ml = ?;'
                        parameters=(cantidad+int(self.cantidad.get()), producto.link)
                        self.run_query(query, parameters)
                        self.get_productos()
                        self.mensaje['text'] = 'Producto ya existente. Se actualizo el stock.'
                        return
                #De lo contrario de inserta un nuevo producto
                query = 'INSERT INTO PRODUCTOS VALUES(NULL, ?, ?, ?, ?, ?)'
                parameters = (producto.nombre, self.cantidad.get(), producto.link, producto.precio, producto.precio_venta)
                self.run_query(query, parameters)
                self.mensaje['text'] = 'Producto añadido satifactoriamente.'
            except Exception as e:
                self.mensaje['text'] = 'Link ingresado es invalido'
                return e
        else:
            self.mensaje['text'] = 'Se requiere nombre y link'

        self.get_productos()


if __name__=='__main__':

    window = Tk()
    aplicacion = CargaProductos(window)
    window.mainloop()
