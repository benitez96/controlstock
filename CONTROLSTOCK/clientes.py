from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
from forms import Form
#Button, Label, Toplevel, Tk, Canvas, Frame

class CargaCliente():
    db_name = 'controlstock'

    def __init__(self, window):
        self.window = window
        self.window.title('ADMINISTRACION CLIENTES')
        self.window.geometry('840x500')
        frame = Frame(self.window).grid(row=0, column=0, columnspan=12, pady=20, padx=20)
        Button(frame, text='AÑADIR\nCLIENTE', height=3, command=lambda:self.client_form() ).grid(row=0, column=1, pady=30, sticky=W+E)     
        Button(frame, text='VER\nESTADO',  height=3 ).grid(row=0, column=2, pady=30, sticky=W+E)
        Button(frame, text='EDITAR\nCLIENTE',  height=3 ).grid(row=0, column=3, pady=30, sticky=W+E)
        Button(frame, text='BUSCAR',  height=3 ).grid(row=0, column=4, pady=30, sticky=W+E)
        


        #Tree Clientes
        self.tree = ttk.Treeview(self.window, height=15)
        self.tree['columns']=('#1','#2', '#3')
        self.tree.grid(row=5, column=0, columnspan=12, padx=20)
        self.tree.heading('#0', text='Nombre', anchor=CENTER)
        self.tree.heading('#1', text='DNI', anchor=CENTER)
        self.tree.heading('#2', text='DOMICILIO', anchor=CENTER)
        self.tree.heading('#3', text='TELEFONO', anchor=CENTER)
        
        self.get_clientes()


    def get_clientes(self):
        #Limpiar Tabla
        records = self.tree.get_children()
        for elem in records:
            self.tree.delete(elem)
        #Consulta datos
        query = 'SELECT * FROM CLIENTES'
        db_rows = self.run_query(query)
        #Relleno Tabla
        for id_clientes, nombre, apellido, dni, direccion, tel in db_rows:
            self.tree.insert('', id_clientes, text=f'{apellido} {nombre}', values=(dni, direccion, tel))


    def client_form(self):
        window = Toplevel()
        Label(window, text ='INGRESE LOS DATOS DEL CLIENTE').grid(row=0, column=0, columnspan=2)
        Label(window, text =' ').grid(row=1, column=0, columnspan=2)
        self.client = Form(window, 'REGISTRO DE CLIENTES', ['APELLIDO','NOMBRE','DNI','DOMICILIO','TELEFONO'],start_row=2)
        ttk.Button(window, text='AÑADIR', command=lambda:self.aniadir_cliente()).grid(row=7, column=1)
    
    def validar(self):
        validation = (
        len(self.client.entry['APELLIDO'].get())!=0 and
        len(self.client.entry['NOMBRE'].get())!=0 and
        len(self.client.entry['DNI'].get())!=0 and
        len(self.client.entry['DOMICILIO'].get())!=0 and
        len(self.client.entry['TELEFONO'].get())!=0
        )
        return validation

    def aniadir_cliente(self):
        if self.validar():

            query = 'INSERT INTO CLIENTES VALUES(NULL, ?, ?, ?, ?,? )'
            parameters = (
                self.client.entry['NOMBRE'].get().upper(),
                self.client.entry['APELLIDO'].get().upper(),
                self.client.entry['DNI'].get(),
                self.client.entry['DOMICILIO'].get().upper(),
                self.client.entry['TELEFONO'].get(),
            )          
            self.run_query(query, parameters)

        self.get_clientes()
        
    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result

if __name__ == '__main__':

    window = Tk()
    aplicacion = CargaCliente(window)
    window.mainloop()
    