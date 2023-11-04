import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox


listaContactos = Tk()

def centrar_ventana(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)

    window.geometry(f"{width}x{height}+{position_right}+{position_top}")

centrar_ventana(listaContactos, 1220, 300)

listaContactos.title("Lista de contactos")

groupBox = LabelFrame(listaContactos, text="Tus contactos:")
groupBox.pack(padx=5, pady=5)

tablaContactos = ttk.Treeview(groupBox, columns=("Nombre", "Apellido", "Número", "Correo", "Dirección", "Relación"), show="headings", height=10,)

tablaContactos.column("# 1", anchor=CENTER)
tablaContactos.heading("# 1", text="Nombre")
tablaContactos.column("# 2", anchor=CENTER)
tablaContactos.heading("# 2", text="Apellido")
tablaContactos.column("# 3", anchor=CENTER)
tablaContactos.heading("# 3", text="Número")
tablaContactos.column("# 4", anchor=CENTER)
tablaContactos.heading("# 4", text="Correo")
tablaContactos.column("# 5", anchor=CENTER)
tablaContactos.heading("# 5", text="Dirección")
tablaContactos.column("# 6", anchor=CENTER)
tablaContactos.heading("# 6", text="Relación")

tablaContactos.pack()


def btnAgregarContactos():

    ventanaAgregarContactos = Toplevel()
    ventanaAgregarContactos.title("Agregar nuevo contacto")
    centrar_ventana(ventanaAgregarContactos, 720, 300)

    groupBox = LabelFrame(ventanaAgregarContactos, text="Agregar nuevo contacto", padx=190)
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
    Button(groupBox, text = "Tus contactos", font=("Arial", 12)).grid(row=6, column=0, pady=25)

btnAgregarContacto = Button(groupBox, text = "Agregar nuevo contacto", width=20, font=("Arial", 10), command=btnAgregarContactos).pack(pady=5)

    


listaContactos.mainloop()