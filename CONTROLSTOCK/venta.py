from tkinter import *

class Venta:
    def __init__(self, window):

        self.window = window
        self.window.title('GESTION DE VENTAS')
        self.window.geometry('840x500')
        self.window.config(bg='#7bb7b6')
        Label(self.window, text='CLIENTE:').place(x=40, y=30)
        self.client = Label(self.window, bg='#669291')
        self.client.place(x=120,y=30)
        Button(self.window, text='Buscar').place(x=250, y=27)
        







if __name__ == '__main__':

    window = Tk()
    aplicacion = Venta(window)
    window.mainloop()
    