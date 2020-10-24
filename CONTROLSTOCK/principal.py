from tkinter import *
import clientes
import gui_productos
import venta

def ir_ventas():
    topl = Toplevel()
    venta.Venta(topl)
    #topl.mainloop()

def ir_clientes():
    topl = Tk()
    clientes.CargaCliente(topl)
    topl.mainloop()

def ir_stock():
    topl = Tk()
    gui_productos.CargaProductos(topl)
    topl.mainloop()
    
ventana = Tk()
ventana.config(bg='#728fce')
ventana.geometry('800x400')
ventana.title('GESTION CASA ELECTRODOMESTICOS')
Button(ventana, text='REALIZAR\nVENTA', font=('Verdana', 15), command=ir_ventas).place(x= 230, y=250)
Button(ventana, text='GESTION\nCLIENTES', font=('Verdana', 15), command=ir_clientes).place(x=360, y=250)
Button(ventana, text='CONTROL\nSTOCK', font=('Verdana', 15), command=ir_stock).place(x=490, y=250)
logo = PhotoImage(file='electro.gif')
Label(ventana, image=logo).place(x=60, y=100)




ventana.mainloop()