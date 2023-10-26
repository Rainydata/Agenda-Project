from Persona import Persona

class Contacto (Persona):

    #Contructor
    def __init__(self, nota:str, relacion:str, direccion:str, nombre:str, apellido:str, correo:str, telefono:int):

        super().__init__(nombre, apellido, correo, telefono)
        self.relacion = relacion
        self.direccion = direccion
        self.nota = nota


    #metodo Get

    def get_nota(self):
        return self.nota
    
    def get_relacion(self):
        return self.relacion
    
    def get_direccion(self):
        return self.direccion
    
    #Metodo Set

    def set_nota(self, nota):
        self.nota = nota

    def set_relacion(self, relacion):
        self.relacion = relacion

    def set_direccion(self, direccion):
        self.direccion = direccion        