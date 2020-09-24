from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
from PIL import ImageTk, Image

class CargaCliente():
    
    def __init__(self, window):
        self.window = window
        self.window.title('ADMINISTRACION CLIENTES')
        self.window.geometry('840x500')
        frame = Frame(self.window).grid(row=0, column=0, columnspan=12, pady=20)
        Button(frame, text='AÑADIR CLIENTE', height=5 ).grid(row=0, column=0, pady=30)     
        Button(frame, text='VER ESTADO',  height=5 ).grid(row=0, column=1, pady=30)
        Button(frame, text='EDITAR CLIENTE',  height=5 ).grid(row=0, column=2, pady=30)
        Button(frame, text='BUSCAR',  height=5 ).grid(row=0, column=3, pady=30)



        #Tree Clientes
        self.tree = ttk.Treeview(self.window, height=15)
        self.tree['columns']=('#1','#2', '#3')
        self.tree.grid(row=4+1, column=0, columnspan=12, padx=20)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='DNI', anchor=CENTER)
        self.tree.heading('#2', text='DOMICILIO', anchor=CENTER)
        self.tree.heading('#3', text='TELEFONO', anchor=CENTER)




if __name__ == '__main__':

    window = Tk()
    aplicacion = CargaCliente(window)
    window.mainloop()