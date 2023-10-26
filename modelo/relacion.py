from Persona import Persona

class Familia(Persona):
    def __init__(self, nombre:str , apellido:str, correo:str, telefono:int, parentesco:str):
        super().__init__(nombre, apellido, correo, telefono)
        self.parentesco = parentesco

    def get_parentesco(self):
        return self.parentesco
    
    def set_parentesco(self, parentesco):
        self.parentesco = parentesco

    