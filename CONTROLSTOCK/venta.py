from tkinter import *
from searchtree import SearchWindow
from tkinter import ttk, messagebox
import sqlite3
from forms import Form
import datetime
import re

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
        Button(self.window, text='Editar\nArticulo', command=self.editar_art).place(x=600, y=29)
        Button(self.window, text='Completar\nVenta', command=self.concretar_venta).place(x=670, y=29)
        self.productos = ttk.Treeview(self.window)
        self.productos.place(x=90, y=100)
        self.productos['columns'] = ['ID', 'PRODUCTO', 'CANTIDAD','PRECIO REPO', 'PRECIO U', 'PRECIO TOTAL']
        self.productos.heading('ID', text='ID', anchor=CENTER)
        self.productos.heading('PRODUCTO', text='PRODUCTO', anchor=CENTER)
        self.productos.heading('CANTIDAD', text='CANTIDAD', anchor=CENTER)
        self.productos.heading('PRECIO REPO', text='PRECIO REPO', anchor=CENTER, )
        self.productos.heading('PRECIO U', text='PRECIO UNITARIO', anchor=CENTER)
        self.productos.heading('PRECIO TOTAL', text='PRECIO TOTAL', anchor=CENTER)
        self.productos.column('#0', minwidth=0, width=0)
        self.productos.column('ID', minwidth=0, width=50)
        self.productos.column('PRODUCTO', minwidth=0, width=200)
        self.productos.column('CANTIDAD', minwidth=0, width=80)
        self.productos.column('PRECIO REPO', minwidth=0, width=100, )
        self.productos.column('PRECIO U', minwidth=0, width=120)
        self.productos.column('PRECIO TOTAL', minwidth=0, width=100)
        #self.productos.tag_configure('PRECIO REPO', foreground='red')
        #===============TOTALES===============
        Label(self.window, text= 'TOTAL VENTA', font=('arial', 15)).place(x=475, y=330)
        self.total_venta = Label(self.window, text='0.00', font=('arial', 15))
        self.total_venta.place(x=650, y=330)
        Label(self.window, text= 'N° Cuotas: ', font=('arial', 8)).place(x=475, y=365)
        self.cuotas = Entry(self.window, textvariable=IntVar(value=1), width=5)
        self.cuotas.place(x=570, y=365)
        Label(self.window, text= 'Recargo: ', font=('arial', 8)).place(x=475, y=390)
        self.recargo = Entry(self.window, textvariable=IntVar(value=0), width=5)
        self.recargo.place(x=570, y=390)
        Label(self.window, text= 'Precio Cuota: ', font=('arial', 8)).place(x=475, y=415)
        
        self.precio_c = Entry(self.window, textvariable=StringVar(value='0.00'), state='readonly', width=12)
        self.precio_c.place(x=570, y=415)
        Button(self.window, text='A', command=self.p_cuota).place(x=655, y=412)

    
        #Ingreso productos
        self.ingresar_prod = Entry(self.window, width=50, font=('Verdana', 14) )
        self.ingresar_prod.place(x=90, y=447)
        self.ingresar_prod.focus()
        self.buscar = Button(self.window, text='Buscar\nProducto', command=lambda:self.buscar_prod())
        self.buscar.place(x=700,y=440)
        self.window.bind('<Return>', self.buscar_prod)



        #Tabla Productos
    def buscar_prod(self, event=None):
        self.wind = Toplevel()
        self.tree = ttk.Treeview(self.wind,height=10)
        self.tree['columns']=('#1','#2', '#3', '#4')
        self.tree.pack(side=LEFT)
        self.tree.heading('#0', text='ID', anchor=CENTER)
        self.tree.heading('#1', text='Nombre', anchor=CENTER)
        self.tree.heading('#2', text='En stock', anchor=CENTER)
        self.tree.heading('#3', text='Precio ML', anchor=CENTER)
        self.tree.heading('#4', text='Precio Sugerido', anchor=CENTER)
        scrollbary = Scrollbar(self.wind, orient=VERTICAL)
        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        self.wind.bind("<Escape>", lambda *ignore: self.wind.destroy())
        #Productos registrados
        self.wind.bind("<Return>", self.product_selection)
        self.wind.bind("<Double-1>", self.product_selection)
        self.get_productos()
        
    def p_cuota(self):
        total = self.calcular_total()
        cuota = (total + total * int(self.recargo.get())/100)/int(self.cuotas.get())
        self.precio_c['textvariable'] = StringVar(value=f'{cuota:,.2f}')
        self.total_venta['text'] = f'{(total + total * int(self.recargo.get())/100):,.2f}'


    def product_selection(self, event):
        selected = self.tree.item(self.tree.selection())
        parameters = (selected['text'],)
        query = 'SELECT * FROM PRODUCTOS WHERE id_productos = ?'
        db_product = self.run_query(query, parameters)
        for id, nombre, cantidad, categoria, link, precio, precio_venta in db_product:
            self.productos.insert('', id, text=id, values=(id, nombre, 1, precio, precio_venta, precio_venta))
        self.ingresar_prod['textvariable'] = StringVar(value='')
        self.calcular_total()
        self.wind.destroy()
        
        

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
            self.tree.insert('', id, text=id, values=(nombre, cantidad, precio, precio_venta))
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

        self.total_venta['text'] = f'{total:,.2f}'
        return total
        

    def editar_art(self):

        try:
            cant = self.productos.item(self.productos.selection())['values'][2]
            precio_v = self.productos.item(self.productos.selection())['values'][4]
            self.edit_wind = Toplevel()
            self.edit_wind.title = 'EDITAR PRODUCTO'

            #Old precio
            Label(self.edit_wind, text= 'Precio Anterior: ').grid(row=0, column=0)
            Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=precio_v), state='readonly').grid(row=0, column=1)
            #New precio
            Label(self.edit_wind, text= 'Nuevo precio: ').grid(row=1, column=0)
            n_precio = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=precio_v))
            n_precio.grid(row=1, column=1)
            #Cantidad
            Label(self.edit_wind, text= 'Cantidad: ').grid(row=2, column=0)
            n_cant = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=cant))
            n_cant.grid(row=2, column=1)
            Label(self.edit_wind, text='').grid(row=3, column=0)
            Button(self.edit_wind, text='ACTUALIZAR', command=lambda:self.cambio_preciov(n_cant.get(), n_precio.get())).grid(row=4, column=1, sticky=W)
               
        
        except Exception as e:
            return e

    def cambio_preciov(self, n_cant, n_precio):
        n_cant = int(n_cant)
        n_precio = float(n_precio)
        item = self.productos.selection()
        self.productos.set(item, 'CANTIDAD', n_cant)
        self.productos.set(item, 'PRECIO U', n_precio)
        self.productos.set(item, 'PRECIO TOTAL', n_cant*n_precio)

        self.calcular_total()
        self.edit_wind.destroy()


    def concretar_venta(self):

        if len(self.client['text'])<2:
            messagebox.showinfo('Error de Venta', 'No has seleccionado ningun cliente.')
            return 
        
        if len(self.productos.get_children()) == 0:
            messagebox.showinfo('Error de Venta', 'No hay productos en el carrito.')
            return



        query = 'INSERT INTO VENTAS VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)'
        id_productos = [self.productos.item(child)['values'][0] for child in self.productos.get_children()]
        totales = [self.productos.item(child)['values'][4] for child in self.productos.get_children()]
        cantidades = [self.productos.item(child)['values'][2] for child in self.productos.get_children()]
        id_regex= re.compile(r'\d*')
        id = re.search(id_regex, self.client['text'])
        id = int(id.group())
        
        for id_producto, cant, total in zip(id_productos, cantidades, totales):
            total = float(total)
            total += total*int(self.recargo.get())/100
            parameters = (id, id_producto, datetime.date.today(), total, int(self.cuotas.get()) , 1, cant)
            self.run_query(query, parameters)
            #========== DESCONTAR DE LA TABLA PRODUCTOS===============#
            d_query = 'UPDATE PRODUCTOS SET cantidad = cantidad - ? WHERE id_productos = ?'
            parameters = (cant, id_producto)
            self.run_query(d_query, parameters)

        messagebox.showinfo('Venta Exitosa!', 'La venta se ha registrado correctamente.')
        records = self.productos.get_children()
        for elem in records:
            self.productos.delete(elem)
        self.calcular_total()

        
        




if __name__ == '__main__':

    window = Tk()
    aplicacion = Venta(window)
    window.mainloop()
    