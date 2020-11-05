import sqlite3
import pandas as pd
import seaborn as sns
#import tkinter
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

with sqlite3.connect('controlstock') as db:

    df_ventas = pd.read_sql_query('SELECT * FROM VENTAS', db)
    df_productos = pd.read_sql_query('SELECT * FROM PRODUCTOS', db)
    
sns.catplot(data=df_ventas, x='fecha_venta', y='precio_venta', kind='bar')


# def create_plot():
#     #sns.set(style="white")

    
#     # Set up the matplotlib figure
#     f, ax = plt.subplots(figsize=(5, 5))
    
#     sns.displot(data=df_ventas, x='fecha_venta', y='precio_venta')
#     return f





# root = tkinter.Tk()

# fig = create_plot()
# canvas = FigureCanvasTkAgg(fig, master=root)    #
# canvas.draw()
# canvas.get_tk_widget().pack()

# root.mainloop()