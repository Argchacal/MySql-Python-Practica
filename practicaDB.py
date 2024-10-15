import mysql.connector
from json import *


"""
Inicializa y conecta al hostDb usando el usuario y contraseña almacenado en el 
archivo setting.json"""

try:
    with open("./datos.json",'r') as archivo:
        datosConeccion = load(archivo)
    
    miDB = mysql.connector.connect(host= datosConeccion["host"],user =datosConeccion["user"],password =datosConeccion["password"] )
except mysql.Error as error:
    print(f"Error al conectar a la base de datos: {error}")

miCursor = miDB.cursor()
# #cramos la base de dato
# miCursor.execute("CREATE DATABASE IF NOT EXISTS practica")
#usamos la DB creada
miCursor.execute("USE practica")
#creamos la tabla
# miCursor.execute('CREATE TABLE IF NOT EXISTS clientes(nombre VARCHAR(255), direccion VARCHAR(255))')
# #mostramos la tabla
# miCursor.execute("SHOW TABLES")
for x in miCursor:
    print(x)

#insertamos datos a la tabla

# consulta = "INSERT INTO clientes(nombre, direccion) VALUE (%s,%s)"
#valor = ("marcelo","pasco 203")
#miCursor.execute(consulta, valor)
#No olvidar del commit para aplicar los cambios
#miDB.commit()

#rowcount nos indica la cantida de filas agregadas a la tabla
#print(miCursor.rowcount, "FIlas agregadas")

# valor = [('Juan Pérez', 'Calle 1, Ciudad A'),
#     ('María González', 'Avenida 2, Ciudad B'),
#     ('Carlos Ramírez', 'Calle 3, Ciudad C'),
#     ('Ana López', 'Avenida 4, Ciudad D'),
#     ('Luis Fernández', 'Calle 5, Ciudad E'),
#     ('Marta Sánchez', 'Avenida 6, Ciudad F'),
#     ('José Gómez', 'Calle 7, Ciudad G'),
#     ('Lucía Ruiz', 'Avenida 8, Ciudad H'),
#     ('Raúl Díaz', 'Calle 9, Ciudad I'),
#     ('Sofía Torres', 'Avenida 10, Ciudad J'),
#     ('Andrés Morales', 'Calle 11, Ciudad K'),
#     ('Laura Ortiz', 'Avenida 12, Ciudad L'),
#     ('Pedro Castro', 'Calle 13, Ciudad M')
# ]
#con executemany ejecuto multiples consultas
#miCursor.executemany(consulta, valor)
#rowcount nos indica la cantida de filas agregadas a la tabla
#print(miCursor.rowcount, "FIlas agregadas")
#-----------------------------------------------------
#No olvidar del commit para aplicar los cambios
#-----------------------------------------------------
#miDB.commit()
#agrego un id 
# miCursor.execute("ALTER TABLE clientes ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# #-----------------------------------------------------
# #No olvidar del commit para aplicar los cambios
# #-----------------------------------------------------
# miDB.commit()

# -----------------------------------------------------
# realizo consulta
# -----------------------------------------------------
# consulta = "SELECT * FROM clientes"

# miCursor.execute(consulta)
# #fetchall() trae todo los datos guardados en mi cursor y lo guarda en la variable
# consulta =  miCursor.fetchall()
# for i in consulta:
#     print (i)

# -----------------------------------------------------
# realizo delete
# -----------------------------------------------------
# #Eliminamos a ('Marta Sánchez', 'Avenida 6, Ciudad F')
# consulta = "DELETE FROM clientes WHERE direccion LIKE 'Avenida 6, Ciudad F'"
# miCursor.execute(consulta)
# #-----------------------------------------------------
# #No olvidar del commit para aplicar los cambios
# #-----------------------------------------------------
# miDB.commit()

# -----------------------------------------------------
# realizo delete
# -----------------------------------------------------
#update a 'Juan Pérez', 'Calle 1, Ciudad A', '1'
consulta = "UPDATE  clientes SET direccion ='Avenida 1, Ciudad AAA' WHERE nombre ='Juan Pérez'"
miCursor.execute(consulta)
#-----------------------------------------------------
#No olvidar del commit para aplicar los cambios
#-----------------------------------------------------
miDB.commit()
print(miCursor.rowcount, "FIlas modificadas")
#cerramos cursor
miCursor.close()
