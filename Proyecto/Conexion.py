import mysql.connector

class CConexion:

    def ConexionBD():
        try:
            conexion = mysql.connector.connect(
                user='root', password='alejandrobd411', 
                host='127.0.0.1',database='agenda_contactos', 
                port='3306')
        
            print("Conexion exitosa")
            return conexion
            
        
        except mysql.connector.Error as error:
            print("Error al conectar la base de datos {}".format(error))