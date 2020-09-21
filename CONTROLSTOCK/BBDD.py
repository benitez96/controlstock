import sqlite3

con = sqlite3.connect('controlstock')

cur = con.cursor()
#TABLA PRODUCTOS
cur.execute("""CREATE TABLE IF NOT EXISTS Productos (
  idProductos INTEGER PRIMARY KEY NOT NULL,
  nombre VARCHAR(45) NULL,
  link_ml VARCHAR(200) NULL,
  precio_ml FLOAT NULL)
  """
  )
#TABLA CLIENTES
cur.execute("""

CREATE TABLE IF NOT EXISTS Clientes (
  idClientes INTEGER PRIMARY KEY NOT NULL,
  nombre VARCHAR(45) NULL,
  apellido VARCHAR(45) NULL,
  dni INTEGER NULL,
  direccion VARCHAR(45) NULL,
  tel INTEGER NULL)

""")

#TABLA VENTAS

cur.execute( """
  CREATE TABLE IF NOT EXISTS Ventas (
  id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
  idCliente INTEGER NOT NULL,
  idProducto INTEGER NOT NULL,
  fecha_venta DATE NULL,
  precio_venta FLOAT NULL,
  cuotas_totales INTEGER NULL,
  cuotas_pagadas INTEGER NULL)
""" )

#cur.commit()


con.close()