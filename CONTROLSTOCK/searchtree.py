from tkinter import *
from tkinter import ttk
import sqlite3

class SearchWindow():
    def __init__(self, tk_obj, db_name, client):
        self.client = client
        self.window = tk_obj
        self.window.title("BUSCAR CLIENTES")
        width = 700
        height = 430
        self.window.geometry("%dx%d" % (width, height))
        self.db_name = db_name



#=====================================FRAME================================================
        self.Top = Frame(self.window, width=500, bd=1, relief=SOLID)
        self.Top.pack(side=TOP)
        self.TopFrame = Frame(self.window, width=500)
        self.TopFrame.pack(side=TOP)
        self.TopForm= Frame(self.TopFrame, width=300)
        self.TopForm.pack(side=LEFT, pady=10)
        self.TopMargin = Frame(self.TopFrame, width=260)
        self.TopMargin.pack(side=LEFT)
        self.MidFrame = Frame(self.window, width=500)
        self.MidFrame.pack(side=TOP)


#=====================================VARIABLES============================================
        self.SEARCH = StringVar()
        self.selected = StringVar()

#=====================================LABEL WIDGET=========================================
        lbl_title = Label(self.Top, width=500, font=('arial', 18), text="BUSCAR CLIENTES")
        lbl_title.pack(side=TOP, fill=X)
    
#=====================================ENTRY WIDGET=========================================
        self.search = Entry(self.TopForm, textvariable=self.SEARCH)
        self.search.pack(side=LEFT)
            
#=====================================BUTTON WIDGET========================================
        btn_search = Button(self.TopForm, text="Search", bg="#006dcc", command=lambda:self.Search())
        btn_search.pack(side=LEFT)
        btn_reset = Button(self.TopForm, text="Reset", command=lambda:self.Reset())
        btn_reset.pack(side=LEFT)

#=====================================Table WIDGET=========================================
        scrollbarx = Scrollbar(self.MidFrame, orient=HORIZONTAL)
        scrollbary = Scrollbar(self.MidFrame, orient=VERTICAL)
        self.tree = ttk.Treeview(self.MidFrame, columns=("ID", "NOMBRE", "APELLIDO", 'DNI','DOMICILIO', 'TELEFONO'), selectmode="extended", height=400, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('ID', text="ID",anchor=W)
        self.tree.heading('APELLIDO', text="APELLIDO",anchor=W)
        self.tree.heading('NOMBRE', text="NOMBRE",anchor=W)
        self.tree.heading('DNI', text="DNI",anchor=W)
        self.tree.heading('DOMICILIO', text="DOMICILIO",anchor=W)
        self.tree.heading('TELEFONO', text="TELEFONO",anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=0)
        self.tree.column('#2', stretch=NO, minwidth=0, width=120)
        self.tree.column('#3', stretch=NO, minwidth=0, width=120)
        self.tree.column('#4', stretch=NO, minwidth=0, width=120)
        self.tree.column('#5', stretch=NO, minwidth=0, width=220)
        self.tree.column('#6', stretch=NO, minwidth=0, width=80)
        self.tree.pack()
        self.Database()
        self.window.bind("<Escape>", lambda *ignore: self.window.destroy())
        self.tree.bind("<Double-1>", self.selection)



    def selection(self, event):
        
        l_name = self.tree.item(self.tree.selection())['values'][2]
        id = self.tree.item(self.tree.selection())['values'][0]
        name = self.tree.item(self.tree.selection())['values'][1]
        self.selected = f'{id} - {l_name} {name}'        
        self.window.destroy()
        self.client['text'] = self.selected
        return self.selected

#=====================================METHODS==============================================


    def Database(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CLIENTES ORDER BY apellido")
        fetch = cursor.fetchall()
        for data in fetch:
            self.tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

    def Search(self):
        if self.SEARCH.get() != "":
            #Limpiar Tabla
            records = self.tree.get_children()
            for elem in records:
                self.tree.delete(elem)
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM CLIENTES WHERE nombre LIKE ? OR apellido LIKE ?", ('%'+str(self.SEARCH.get())+'%', '%'+str(self.SEARCH.get())+'%'))
            fetch = cursor.fetchall()
            for data in fetch:
                self.tree.insert('', 'end', values=(data))
            cursor.close()
            conn.close()
    def Reset(self):
        #Limpiar Tabla
        records = self.tree.get_children()
        for elem in records:
            self.tree.delete(elem)
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CLIENTES ORDER BY APELLIDO ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            self.tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        self.search.delete(0, END)
        



#=====================================INITIALIZATION=======================================
if __name__ == '__main__':
    window = Tk()
    aplicacion = SearchWindow(window, 'controlstock')
    window.mainloop()