from tkinter import *
from tkinter import messagebox, ttk
import sqlite3

class CargaCliente():
    
    def __init__(self, window):
        self.window = window
        self.window.title('ADMINISTRACION CLIENTES')
        self.window.geometry('840x500')
        




if __name__ == '__main__':

    window = Tk()
    aplicacion = CargaCliente(window)
    window.mainloop()