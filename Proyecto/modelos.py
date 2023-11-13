class Persona:
    
    def __init__(self, nombre, apellido) :
        
        self.nombre = nombre
        self.apellido = apellido

class Contacto(Persona):

    def __init__(self, nombre, apellido,telefono, correo, direccion, relacion):
        super().__init__(nombre, apellido)
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.relacion = relacion
        
   