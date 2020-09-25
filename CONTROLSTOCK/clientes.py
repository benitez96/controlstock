from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
from forms import Form

class CargaCliente():
    db_name = 'controlstock'

    def __init__(self, window):
        self.window = window
        self.window.title('ADMINISTRACION CLIENTES')
        self.window.geometry('840x500')
        frame = Frame(self.window).grid(row=0, column=0, columnspan=12, pady=20, padx=20)
        Button(frame, text='AÑADIR\nCLIENTE', height=3, command=lambda:self.client_form() ).grid(row=0, column=1, pady=30, sticky=W+E)     
        Button(frame, text='VER\nESTADO',  height=3 ).grid(row=0, column=2, pady=30, sticky=W+E)
        Button(frame, text='EDITAR\nCLIENTE',  height=3, command=lambda:self.edit_client()).grid(row=0, column=3, pady=30, sticky=W+E)
        Button(frame, text='BUSCAR',  height=3 ).grid(row=0, column=4, pady=30, sticky=W+E)
        self.mensaje = Label(self.window, text = '', fg='red')
        self.mensaje.grid(row=17, column=0, columnspan=12)


        #Tree Clientes
        self.tree = ttk.Treeview(self.window, height=15)
        self.tree['columns']=('#1','#2', '#3')
        self.tree.grid(row=5, column=0, columnspan=12, padx=20)
        self.tree.heading('#0', text='NOMBRE', anchor=CENTER)
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

    def edit_client(self):
        name = self.tree.item(self.tree.selection())['text']
        if len(name) == 0:
            self.mensaje['fg'] = 'red'
            self.mensaje['text'] = 'Debes Seleccionar un Cliente.'
            return
        l_name, name = name.split(maxsplit=1)
        dni = self.tree.item(self.tree.selection())['values'][0]
        adress = self.tree.item(self.tree.selection())['values'][1]
        tel = self.tree.item(self.tree.selection())['values'][2]
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'EDITAR CLIENTE'
        

        #Old name -------------------------------------------------
        Label(self.edit_wind, text= 'Apellido Anterior: ').grid(row=0, column=0)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=l_name), state='readonly').grid(row=0, column=1)
        #New name
        Label(self.edit_wind, text= 'Nuevo Apellido: ').grid(row=1, column=0)
        n_lname = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=l_name))
        n_lname.grid(row=1, column=1)
        #Old name -------------------------------------------------
        Label(self.edit_wind, text= 'Nombre Anterior: ').grid(row=2, column=0)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=name), state='readonly').grid(row=2, column=1)
        #New name
        Label(self.edit_wind, text= 'Nuevo Nombre: ').grid(row=3, column=0)
        n_name = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=name))
        n_name.grid(row=3, column=1)
        #Old precio ------------------------------------------------
        Label(self.edit_wind, text= 'DNI Anterior: ').grid(row=4, column=0)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=dni), state='readonly').grid(row=4, column=1)
        #New DNI
        Label(self.edit_wind, text= 'Nuevo DNI: ').grid(row=5, column=0)
        n_dni = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=dni))
        n_dni.grid(row=5, column=1)
        #Old Adress ------------------------------------------------
        Label(self.edit_wind, text= 'Domicilio Anterior: ').grid(row=6, column=0)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=adress), state='readonly').grid(row=6, column=1)
        #New Adress 
        Label(self.edit_wind, text= 'Nuevo Domicilio: ').grid(row=7, column=0)
        n_adress = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=adress))
        n_adress.grid(row=7, column=1)
        #Old Tel---------------------------------------------------
        Label(self.edit_wind, text= 'Telefono Anterior: ').grid(row=8, column=0)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=tel), state='readonly').grid(row=8, column=1)
        #New Tel
        Label(self.edit_wind, text= 'Nuevo Telefono: ').grid(row=9, column=0)
        n_tel = Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=tel))
        n_tel.grid(row=9, column=1)
        
        Label(self.edit_wind, text=' ').grid(row=10, column=0)

        Button(self.edit_wind, text='ACTUALIZAR', command=lambda:self.editar_registro(n_name.get(), n_lname.get(), n_dni.get(), dni, n_adress.get(), n_tel.get())).grid(row=11, column=1, sticky=W)

    def editar_registro(self, n_name, n_lname, n_dni, dni, n_adress, n_tel):
        query= 'UPDATE CLIENTES SET nombre = ?, apellido = ?, dni = ?, direccion = ?, tel = ? WHERE dni = ?'
        parameters=(n_name.upper(), n_lname.upper(), n_dni, n_adress.upper(), n_tel, dni)
        self.run_query(query, parameters)
        self.edit_wind.destroy()
        self.mensaje['fg'] = 'green'
        self.mensaje['text'] = f'El registro {n_name} {n_lname}, ha sido actualizado.'
        self.get_clientes()

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
    