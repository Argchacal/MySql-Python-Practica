import mysql.connector
from json import *


"""
Inicializa y conecta al hostDb usando el usuario y contraseña almacenado en el 
archivo setting.json"""

try:
    with open("./dato.json",'r') as archivo:
        datosConeccion = load(archivo)
    
    miDB = mysql.connector.connect(host= datosConeccion["host"],user =datosConeccion["user"],password =datosConeccion["password"] )
except mysql.Error as error:
    print(f"Error al conectar a la base de datos: {error}")

miCursor = miDB.cursor()
miCursor.execute("CREATE DATABASE IF NOT EXISTS practica")
miCursor.execute("USE practica")
miCursor.execute('CREATE TABLE IF NOT EXISTS clientes(nombre VARCHAR(255), direccion VARCHAR(255))')
miCursor.close()