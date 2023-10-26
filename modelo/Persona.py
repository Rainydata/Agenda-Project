class Persona (object):
    
    #contrucor
    def __init__(self, nombre:str, apellido: str, correo:str, telefono: int):
        
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo  
        self.telefono = telefono

    #Metodos Get         

    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_correo(self):
        return self.correo
    
    def get_telefono(self):
        return self.telefono
    
    #Metodos Set

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):    
        self.apellido = apellido

    def set_correo(self, correo):
        self.correo = correo 

    def set_telefono(self, telefono):
        self.telefono = telefono       