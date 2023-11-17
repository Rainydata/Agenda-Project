from Conexion import *
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
class Contacto:

   def __init__(self):
      self.connection = CConexion.ConexionBD()
      self.cursor = self.connection.cursor()

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
          
   
   def buscarContacto(self, nombre, telefono, apellido):
    try:
        query = "SELECT nombre, apellido, telefono, correo, direccion, relacion FROM Contacto WHERE nombre LIKE %s OR telefono LIKE %s OR apellido LIKE %s"
        self.cursor.execute(query, ('%' + nombre + '%', '%' + telefono + '%', '%' + apellido + '%'))
        return self.cursor.fetchall()
    except Exception as e:
        print(f"Error al buscar contacto: {e}")
        return None

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
   
   #funcion que valida si hay un contacto con el mismo telefono
   def validar_telefono(telefono):
     try:
        conexion = CConexion.ConexionBD()
        cursor = conexion.cursor()
        sql = "SELECT * FROM Contacto WHERE telefono=%s"
        valores = (telefono,)
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()
        conexion.close()
        return resultado
     except mysql.connector.Error as error:
        print("Error al mostrar contacto: {} ".format(error))  

          
        
            