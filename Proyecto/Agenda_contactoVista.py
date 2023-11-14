import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import ControladorContactos as co
from tkinter import messagebox
import modelos as mo

listaContactos = Tk()


#Funcion que carga los datos de la BD a la tablaContactos

def cargarDatos():
    datos = co.Contacto.cargar_contactos()
    for fila in datos:
        tablaContactos.insert("", "end", values=fila)
        

#Funcion que limpia los datos de la tabla tablaContactos
def limpiarTabla():
    for item in tablaContactos.get_children():
        tablaContactos.delete(item)        

#Función que centra la ventana
def centrar_ventana(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    position_top = int(screen_height / 2 - height / 2)
    position_right = int(screen_width / 2 - width / 2)

    window.geometry(f"{width}x{height}+{position_right}+{position_top}")  

#Funcion recursiva para cerrar la ventana  ventanaAgregarContactos
def cerrar_ventana_actual(ventanaAgregarContactos):
    ventanaAgregarContactos.destroy()    

def cerrar_ventana(ventanaAgregarContactos):
    cerrar_ventana_actual(ventanaAgregarContactos)
    cerrar_ventana(ventanaAgregarContactos)          

##Ventana Principal -----------------------------------------------------------------------------------------------

centrar_ventana(listaContactos, 1220, 310)

listaContactos.title("Lista de contactos")
listaContactos.configure(background="#144966")

groupBox = LabelFrame(listaContactos,fg="white", text="Tus contactos:")
groupBox.grid(row=0, column=0)
groupBox.config(background="#144966")

style = ttk.Style()
style.configure("Treeview",background="#7AAFCC")
tablaContactos = ttk.Treeview(groupBox, style="Treeview", columns=("Nombre", "Apellido", "Número", "Correo", "Dirección", "Relación"), show="headings", height=10,)


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
tablaContactos.grid(row=0, column=0, padx=10, pady=10)  
cargarDatos()        

##-----------------------------------------------------------------------------------------------------
   
#Funcion que crea una nueva ventana (TopLevel) con un formulario para el registro de nuevos contactos

def btnAgregarContactos():
    

    ventanaAgregarContactos = Toplevel()
    ventanaAgregarContactos.title("Agregar nuevo contacto")
    centrar_ventana(ventanaAgregarContactos, 720, 300)
    

    groupBox = LabelFrame(ventanaAgregarContactos, text="Agregar nuevo contacto", padx=190)
    groupBox.grid(row=0, column=0, padx=10, pady=10)
    
    labelNombre = Label(groupBox, text="Nombre: ", width=13, font=("Arial", 12)).grid(row=0, column=0)
    txtBoxNombre = Entry(groupBox, width=30)
    txtBoxNombre.grid(row=0, column=1)

    labelApellido = Label(groupBox, text="Apellido: ", width=13, font=("Arial", 12)).grid(row=1, column=0)
    txtBoxApellido = Entry(groupBox, width=30)
    txtBoxApellido.grid(row=1, column=1)

    labelNumero = Label(groupBox, text="Número: ", width=13, font=("Arial", 12)).grid(row=2, column=0)
    txtBoxNumero = Entry(groupBox, width=30)
    txtBoxNumero.grid(row=2, column=1)

    labelCorreo = Label(groupBox, text="Correo: ", width=13, font=("Arial", 12)).grid(row=3, column=0)
    txtBoxCorreo = Entry(groupBox, width=30)
    txtBoxCorreo.grid(row=3, column=1)

    labelDireccion = Label(groupBox, text="Dirección: ", width=13, font=("Arial", 12)).grid(row=4, column=0)
    txtBoxDireccion = Entry(groupBox, width=30)
    txtBoxDireccion.grid(row=4, column=1)

    labelRelacion = Label(groupBox, text="Relación: ", width=13, font=("Arial", 12))
    labelRelacion.grid(row=5, column=0)
    selectRelacion = tk.StringVar()
    combo = ttk.Combobox(groupBox, values = ["Familiar", "Trabajo", "Amigos"], textvariable = selectRelacion, width=27)
    combo.set("Selecciona una opción")
    combo.grid(row = 5, column = 1)
    
    ##Funcion que captura los datos y utiliza la funcion ingresar datos del controlador

    def GuardarContacto():
   
     try:
         nombre = txtBoxNombre.get()
         apellido = txtBoxApellido.get()
         numero = txtBoxNumero.get()
         correo = txtBoxCorreo.get()
         direccion = txtBoxDireccion.get()
         relacion =  combo.get()
         nuevoContacto = mo.Contacto(nombre, apellido, numero, correo, direccion, relacion)
         
         if txtBoxNombre.get() == "" or txtBoxNumero.get() == "" :
             messagebox.showinfo(title="Error", message="Ingrese el nombre y numero como campos obligatorios")
         else:
            co.Contacto.ingresarContacto(nuevoContacto)
            messagebox.showinfo(title="Correcto", message="Se registro el contacto correctamente")
            limpiarTabla()
            cargarDatos()

            txtBoxNombre.delete(0,END)
            txtBoxApellido.delete(0,END) 
            txtBoxNumero.delete(0,END) 
            txtBoxCorreo.delete(0,END) 
            txtBoxDireccion.delete(0,END)
            

     except ValueError as error:
        print("Error al registrar nuevo contacto {}".format(error))       

    Button(groupBox, text ="Agregar", width=10, command= GuardarContacto,font=("Arial", 12)).grid(row=6, column=1, pady=25)
    Button(groupBox, text = "Tus contactos", font=("Arial", 12),command=lambda: cerrar_ventana(ventanaAgregarContactos)).grid(row=6, column=0, pady=25)

##-------------------------------------------------------------------------------------------------------------------

def btnEditarContactos():
    try:
        # Se obtiene el contacto seleccionado
        Contacto = tablaContactos.focus()
        #Guarda el nombre del contacto
        ContactoNombre = tablaContactos.item(Contacto)['values'][0]
    
        ventanaEditarContactos = Toplevel() 
        centrar_ventana(ventanaEditarContactos, 720, 300)
        ventanaEditarContactos.title("Editar contacto")

        groupBox = LabelFrame(ventanaEditarContactos, text="Editar el contacto con el nombre: "+ ContactoNombre, padx=190)
        groupBox.grid(row=0, column=0, padx=10, pady=10)

        labelNombre = Label(groupBox, text="Nombre: ", width=13, font=("Arial", 12)).grid(row=0, column=0)
        txtBoxNombre = Entry(groupBox, width=30)
        txtBoxNombre.grid(row=0, column=1)

        labelApellido = Label(groupBox, text="Apellido: ", width=13, font=("Arial", 12)).grid(row=1, column=0)
        txtBoxApellido = Entry(groupBox, width=30)
        txtBoxApellido.grid(row=1, column=1)

        labelNumero = Label(groupBox, text="Número: ", width=13, font=("Arial", 12)).grid(row=2, column=0)
        txtBoxNumero = Entry(groupBox, width=30)
        txtBoxNumero.grid(row=2, column=1)

        labelCorreo = Label(groupBox, text="Correo: ", width=13, font=("Arial", 12)).grid(row=3, column=0)
        txtBoxCorreo = Entry(groupBox, width=30)
        txtBoxCorreo.grid(row=3, column=1)

        labelDireccion = Label(groupBox, text="Dirección: ", width=13, font=("Arial", 12)).grid(row=4, column=0)
        txtBoxDireccion = Entry(groupBox, width=30)
        txtBoxDireccion.grid(row=4, column=1)

        labelRelacion = Label(groupBox, text="Relación: ", width=13, font=("Arial", 12))
        labelRelacion.grid(row=5, column=0)
        selectRelacion = tk.StringVar()
        combo = ttk.Combobox(groupBox, values = ["Familiar", "Trabajo", "Amigos"], textvariable = selectRelacion, width=27)
        combo.set("Selecciona una opción")
        combo.grid(row = 5, column = 1)
       
        def editarContacto():
            try:
                ContactoID = tablaContactos.item(Contacto)['values'][2]
                nombre = txtBoxNombre.get()
                apellido = txtBoxApellido.get()
                numero = txtBoxNumero.get()
                correo = txtBoxCorreo.get()
                direccion = txtBoxDireccion.get()
                relacion = combo.get()
                nuevoContacto = mo.Contacto(nombre, apellido, numero, correo, direccion, relacion)
                co.Contacto.editarContacto(ContactoID,nuevoContacto)
                messagebox.showinfo(title="Correcto", message="Se ha editado correctamente el contacto")
                limpiarTabla()
                cargarDatos()

            except ValueError as error:
                print("Error al editar el contacto{}".format(error))   

        Button(groupBox, text ="Editar", width=10, font=("Arial", 12),command=editarContacto).grid(row=6, column=1, pady=25)
        Button(groupBox, text = "Tus contactos", font=("Arial", 12),command=lambda: cerrar_ventana(ventanaEditarContactos)).grid(row=6, column=0, pady=25)

    except IndexError as error:
        messagebox.showinfo(title="Error", message="Por favor seleccione un contacto")

##---------------------------------------------------------------------------------------------------------------------------------------------------
#Funcion que gestiona el boton eliminarContacto
def btnEliminarContacto():
    #Se obtiene el Contacto seleccionado
    ContactoEliminar = tablaContactos.focus()
    nombreContacto = tablaContactos.item(ContactoEliminar)['values'][0]
    telefonoContacto = tablaContactos.item(ContactoEliminar)['values'][2]
    mensaje = messagebox.askokcancel(title="Eliminar", message="¿Esta seguro de eliminar el contacto? "+ nombreContacto)
    if mensaje == True:
     co.Contacto.borrarContacto(telefonoContacto)
     limpiarTabla()
     cargarDatos()

##------------------------------------------------------------------------------------------------------------------------
#Creacion de botones CRUD de los contactos
groupBox = LabelFrame(listaContactos)
groupBox.grid(row=1, column=0)
groupBox.config(background="#144966")
btnAgregarContacto = Button(groupBox, text = "Agregar nuevo contacto", width=20,font=("Arial", 10), command=btnAgregarContactos).grid(row=0, column=0, pady=5, padx=5)
btnEditarContacto = Button(groupBox, text = "Editar contacto", width=20, font=("Arial", 10), command=btnEditarContactos).grid(row=0, column=1, pady=5, padx=5)
btnEliminarContactos = Button(groupBox, text = "Eliminar contacto", width=20, font=("Arial", 10),command=btnEliminarContacto).grid(row=0, column=2, pady=5, padx=5)

##------------------------------------------------------------------------------------------------------------------------


listaContactos.mainloop()