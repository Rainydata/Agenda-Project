import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


ventana = Tk()

ventana.title("Agenda de contactos")
ventana.geometry("720x400")

groupBox = LabelFrame(ventana, text="Contactos", padx=190, pady=5)
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
selectRelacion = tk.StringVar()
combo = ttk.Combobox(groupBox, values = ["Familiar", "Trabajo", "Amigos"], textvariable = selectRelacion, width=27)
combo.set("Selecciona una opción")
combo.grid(row = 5, column = 1)

Button(groupBox, text ="Agregar", width=10, font=("Arial", 12)).grid(row=6, column=1, pady=25)

ventana.mainloop()