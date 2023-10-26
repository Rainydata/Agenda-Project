
from Persona import Persona


class Usuario (Persona):
    
    #Contructor aplicando herencia

    def __init__(self, nombreUsuario:str, contraseña:str, nombre:str, apellido:str, correo:str, telefono:int):
        
        super().__init__(nombre, apellido, correo, telefono)
        self.nombreUsuario = nombreUsuario
        self.contraseña = contraseña
       

#Metodos Get

def get_nombreUsuario(self):
    return self.nombreUsuario

def get_contraseña(self):
    return self.contraseña

def get_correo(self):
    return self.correo

def get_telefono(self):
    return self.telefono

#Metodos Set

def set_nombreUsuario(self,nombreUsuario):
    self.nombreUsuario = nombreUsuario

def set_contraseña(self,contraseña):
    self.contraseña = contraseña 

def set_correo(self, correo):
    self.correo = correo

def set_telefono(self, telefono):
    self.telefono = telefono