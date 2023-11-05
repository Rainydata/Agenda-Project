#pip install mysql-connector-python
import mysql.connector

class Conexion:

    def ConexionBD():
        try:
            conexion = mysql.connector.connect(user='root', password='alejandrobd411', host='127.0.0.1', database='agenda_contactos', port='3306')
            print("Conexión exitosa")
            return conexion
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
            return conexion

    ConexionBD()