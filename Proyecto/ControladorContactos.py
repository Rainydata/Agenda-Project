from Conexion import *

class Contacto:

    def ingresarContacto(Contacto):

        try:
            conexion = CConexion.ConexionBD()
            cursor = conexion.cursor()
            sql = "INSERT INTO Contacto (nombre, apellido, telefono, correo, direccion, relacion) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (Contacto.nombre, Contacto.apellido, Contacto.telefono, Contacto.correo, Contacto.direccion, Contacto.relacion)
            cursor.execute(sql, valores)
            conexion.commit()
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))

    def editarContacto(ID,Contacto): 

         try:
            conexion = CConexion.ConexionBD()
            cursor = conexion.cursor()
            sql = "UPDATE Contacto SET nombre=%s, apellido=%s,telefono=%s,correo=%s, direccion=%s, relacion=%s WHERE telefono=%s"
            valores = (Contacto.nombre, Contacto.apellido,Contacto.telefono, Contacto.correo,Contacto.direccion,Contacto.relacion, ID)
            cursor.execute(sql,valores)
            conexion.commit()
         except mysql.connector.Error as error:   
            print("Error al conectar la base de datos: {}".format(error))
    
    def borrarContacto(telefono):
       try:
          conexion = CConexion.ConexionBD()
          cursor = conexion.cursor()
          sql = "DELETE FROM Contacto where telefono = %s"
          #se utiliza "coma" al final ya que el .execute espera una lista o tupla, no un entero
          valores = (telefono,)  
          cursor.execute(sql, valores)
          conexion.commit()
       except mysql.connector.Error as error:
          print("Error al eliminar el contacto: {}".format(error))
          
    def buscarContacto(nombre, telefono):
     try:
        conexion = CConexion.ConexionBD()
        cursor = conexion.cursor()
        sql = "SELECT * FROM contactos WHERE nombrePersona=%s OR telefonoPersona=%s"
        valores = (nombre, telefono)
        cursor.execute(sql, valores)
        resultados = cursor.fetchall()
        for resultado in resultados:
            print(resultado)  
     except mysql.connector.Error as error:
        print("Error al conectar a la base de datos: {}".format(error))

    def cargar_contactos():
     try:
        conexion = CConexion.ConexionBD()
        cursor = conexion.cursor()
        sql = "SELECT nombre, apellido, telefono, correo, direccion, relacion FROM Contacto"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conexion.close()
        return resultado
     except mysql.connector.Error as error:
        print("Error al mostrar contacto: {} ".format(error))

          
        
            