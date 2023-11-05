from Conexion import *

class Contactos:

    def ingresarContacto(nombre, apellido, telefono, correo, relacion):

        try:
            conexion = Conexion.ConexionBD()
            cursor = conexion.cursor()
            sql = "INSERT INTO contactos (nombrePersona, apellidoPersona, telefonoPersona, correoPersona, relacionPersona) VALUES (%s, %s, %s, %s, %s)"
            valores = (nombre, apellido, telefono, correo, relacion)
            cursor.execute(sql, valores)
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
            