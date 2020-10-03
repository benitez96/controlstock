from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
import datetime as dt
import random as rd



class Estado():
    
    
    def __init__(self, window, cliente):
        self.cliente = cliente
        self.db_name = 'controlstock'
        self.window = window
        self.window.title('GESTION DE PAGOS')


        #=============FRAMES=======================
        self.titleframe = Frame(self.window)
        self.titleframe.pack(side=TOP)
        Label(self.titleframe, text='GESTION DE PAGOS CLIENTES\n', font=('Verdana', 15)).pack()
        self.butframe = Frame(self.window)
        self.butframe.pack(side=TOP)
        self.dispframe = Frame(self.window)
        self.dispframe.pack(side=BOTTOM)

        #=============BUTTONS=======================

        Button(self.butframe, text='Ingresar\nPago', bg='#25cc6b', command=self.pago).pack(side=LEFT, padx=10, pady=10)
        Button(self.butframe, text='Modificar\nDeuda', bg='#2589cc', command=self.nueva_cuota).pack(side=LEFT, padx=10, pady=10)
        Button(self.butframe, text='Cancelar\nDeuda', bg='#cc2546', command=self.eliminar_cuota).pack(side=LEFT, padx=10, pady=10)

        #==============TREEVIEW===================

        self.deudas = ttk.Treeview(self.dispframe)
        

        scrollbary = Scrollbar(self.dispframe, orient=VERTICAL)
        scrollbary.config(command=self.deudas.yview)
        scrollbary.pack(side=RIGHT, fill=Y)


        self.deudas['columns'] = ['F VENTA', 'PRODUCTO', 'CANTIDAD','TOTAL','MONTO CUOTA','CUOTAS PAGAS','TOTAL CUOTAS']
        self.deudas.heading('#0', text='N°')
        self.deudas.heading('F VENTA', text='F VENTA')
        self.deudas.heading('PRODUCTO', text='PRODUCTO')
        self.deudas.heading('CANTIDAD', text='CANTIDAD')
        self.deudas.heading('TOTAL', text='TOTAL')
        self.deudas.heading('MONTO CUOTA', text='MONTO CUOTA')
        self.deudas.heading('CUOTAS PAGAS', text='CUOTAS PAGAS')
        self.deudas.heading('TOTAL CUOTAS', text='TOTAL CUOTAS')        
        self.deudas.column('#0', width=40, anchor=CENTER)
        self.deudas.column('F VENTA', width=100, anchor=CENTER)
        self.deudas.column('PRODUCTO', width=200, anchor=CENTER)
        self.deudas.column('CANTIDAD', width=80, anchor=CENTER)
        self.deudas.column('TOTAL', width=80, anchor=CENTER)
        self.deudas.column('MONTO CUOTA', width=120, anchor=CENTER)
        self.deudas.column('CUOTAS PAGAS', width=120, anchor=CENTER)
        self.deudas.column('TOTAL CUOTAS', width=120, anchor=CENTER)

        self.deudas.pack(pady=10, padx=20)



        self.get_deudas()





    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result


    def get_deudas(self):
        #Limpiar Tabla
        records = self.deudas.get_children()
        for elem in records:
            self.deudas.delete(elem)
        query = '''SELECT VENTAS.id_venta,
        VENTAS.fecha_venta,
        PRODUCTOS.nombre, 
        VENTAS.cant,
        VENTAS.precio_venta,
        VENTAS.cuotas_totales,
        VENTAS.cuotas_pagadas
        FROM VENTAS
        INNER JOIN PRODUCTOS ON VENTAS.id_producto = PRODUCTOS.id_productos
        WHERE VENTAS.id_cliente = ?
        ORDER BY VENTAS.fecha_venta DESC
        
        '''
        db_rows = self.run_query(query, parameters=(self.cliente, ))

        for id_venta, fecha, nombre, cant, precio, ct, cp in db_rows:
            impagas = ct-cp
            monto_c = f'{precio/ct:,.2f}'
            precio = f'{precio:,.2f}'
            fecha = dt.datetime.strptime(fecha, '%Y-%m-%d')
            fecha = dt.datetime.strftime(fecha, '%d-%m-%Y')

            if impagas != 0:
                self.deudas.insert('', id_venta, text=id_venta, values=[fecha, nombre, cant, precio,monto_c, cp, ct], tags='T')
                self.deudas.tag_configure('T', font=('Arial', 10))

    def pago(self):
        selected = self.deudas.item(self.deudas.selection())
        monto_c = selected['values'][4]

        ing_pago = Toplevel(bg = '#25ccab')
        ing_pago.title = 'Confirmar pago'
        ing_pago.geometry('250x200')
        Label(ing_pago, text='MONTO CUOTA', font=('Arial Black', 11)).pack(pady=10)
        Entry(ing_pago,readonlybackground='#638a82', textvariable=StringVar(value=monto_c), state='readonly', font=('Arial',10)).pack()
        Button(ing_pago, text='Confirmar\nPago', command=self.persistir_pago).pack(pady=40)


    def persistir_pago(self):
        selected = self.deudas.item(self.deudas.selection())['values']
        fecha, nombre, cant, precio, monto_c, impagas, ct = selected
        query = 'INSERT INTO PAGOS VALUES(NULL, ?, ?, ?)'
        id_venta = self.deudas.item(self.deudas.selection())['text']
        parameters=(fecha, id_venta, monto_c)
        self.run_query(query, parameters)
        
        #==========DESCUENTO CUOTA =============
        query = 'UPDATE VENTAS SET cuotas_pagadas = cuotas_pagadas + 1 WHERE id_venta = ?'
        parameters = (id_venta, )
        self.run_query(query, parameters)

        messagebox.showinfo('Pago Confirmado', 'Operacion Exitosa!')
        self.get_deudas()

    def nueva_cuota(self):
        values = self.deudas.item(self.deudas.selection())['values']
        ventana = Toplevel()
        ventana.geometry('250x290')
        Label(ventana, text='Monto cuota actual',font=('Arial', 11)).pack(pady=10)
        Entry(ventana, textvariable=StringVar(value=values[4]),font=('Arial', 11) ,state='readonly', readonlybackground='grey').pack(pady=10)
        Label(ventana, text='Nuevo monto cuota',font=('Arial', 11)).pack(pady=10)
        n_monto = Entry(ventana,font=('Arial', 11))
        n_monto.pack()
        n_monto.focus()
        Button(ventana, text='MODIFICAR\nCUOTA', command=lambda:self.modificar_cuota(n_monto)).pack(pady=40)

    def modificar_cuota(self, n_monto):

        if len(n_monto.get())<1:
            messagebox.showinfo('Error!', 'Necesita Ingresar un nuevo monto.')
            return


        values = self.deudas.item(self.deudas.selection())['values']
        total = float(n_monto.get()) * values[6]
        id_venta = self.deudas.item(self.deudas.selection())['text']
        query= 'UPDATE VENTAS SET precio_venta = ? WHERE id_venta = ?'
        parameters = (total, id_venta)
        self.run_query(query, parameters)

        messagebox.showinfo('Cuota modificada', 'Operacion Exitosa!')
        self.get_deudas()
    
    def eliminar_cuota(self):
        ventana = Toplevel()
        ventana.geometry('250x260')
        factor = rd.randint(1000,9999)
        Label(ventana, text=f'Para confirmar ingrese:\n\n{factor}', font=('Arial', 12), justify=CENTER).pack()
        d_factor = Entry(ventana, font=('Arial', 12), width=8)
        d_factor.pack(pady=40)
        d_factor.focus()
        Button(ventana, text='CONFIRMAR', font=('Arial', 13), command=lambda:self.verificar_factor(ventana, factor, d_factor)).pack()


    def verificar_factor(self, ventana, factor, d_factor):
        d_factor = d_factor.get()
        try:
            d_factor = int(d_factor)

        except ValueError:
            return 'Debe Ingresar un Entero'


        if factor != d_factor:
            messagebox.showinfo('Error', 'El doble factor no coincide.')
            ventana.destroy()
            return
        else:
            id_venta = self.deudas.item(self.deudas.selection())['text']
            query = f'DELETE FROM VENTAS WHERE id_venta = {id_venta}'
            self.run_query(query)
            messagebox.showinfo('Operacion exitosa!', 'Registro Borrado correctamente.')
            self.get_deudas()
            ventana.destroy()





    
if __name__=='__main__':
    window = Tk()
    aplicacion = Estado(window, 1)
    window.mainloop()