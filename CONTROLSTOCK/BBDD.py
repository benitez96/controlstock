import sqlite3

con = sqlite3.connect('controlstock')

cur = con.cursor()
#TABLA PRODUCTOS
cur.execute("""CREATE TABLE IF NOT EXISTS PRODUCTOS (
  id_productos INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombre VARCHAR(45) NULL,
  cantidad INTEGER NULL,
  link_ml VARCHAR(300) NULL,
  precio_ml FLOAT NULL)
  """
  )
#TABLA CLIENTES
cur.execute("""

CREATE TABLE IF NOT EXISTS CLIENTES (
  id_clientes INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombre VARCHAR(45) NULL,
  apellido VARCHAR(45) NULL,
  dni INTEGER NULL,
  direccion VARCHAR(45) NULL,
  tel INTEGER NULL)

""")

#TABLA VENTAS

cur.execute( """
  CREATE TABLE IF NOT EXISTS VENTAS (
  id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
  id_cliente INTEGER NOT NULL,
  id_producto INTEGER NOT NULL,
  fecha_venta DATE NULL,
  precio_venta FLOAT NULL,
  cuotas_totales INTEGER NULL,
  cuotas_pagadas INTEGER NULL)
""" )

#cur.commit()


con.close()