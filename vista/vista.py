
#Vista de la aplicación.

import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox



class Persona (object):
    
    
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





ventana = Tk()

ventana.title("Agenda de contactos")
ventana.geometry("1000x400")

groupBox = LabelFrame(ventana, text="Contactos", padx=300, pady=5)
groupBox.grid(row=0, column=0, padx=10, pady=10)

labelNombre = Label(groupBox, text="Nombre: ", width=13, font=("Arial", 12)).grid(row=0, column=0)
txtBoxNombre = Entry(groupBox, width=30).grid(row=0, column=1)

labelApellido = Label(groupBox, text="Apellido: ", width=13, font=("Arial", 12)).grid(row=1, column=0)
txtBoxApellido = Entry(groupBox, width=30).grid(row=1, column=1)

labelNumero = Label(groupBox, text="Número: ", width=13, font=("Arial", 12)).grid(row=2, column=0)
txtBoxNumero = Entry(groupBox, width=30).grid(row=2, column=1)

labelCorreo = Label(groupBox, text="Correo: ", width=13, font=("Arial", 12)).grid(row=3, column=0)
txtBoxCorreo = Entry(groupBox, width=30).grid(row=3, column=1)

labelDireccion = Label(groupBox, text="Dirección: ", width=13, font=("Arial", 12)).grid(row=4, column=0)
txtBoxDireccion = Entry(groupBox, width=30).grid(row=4, column=1)

labelRelacion = Label(groupBox, text="Relación: ", width=13, font=("Arial", 12)).grid(row=5, column=0)
selectRelacion = tk.StringVar(groupBox)
combo = ttk.Combobox(groupBox)



ventana.mainloop()