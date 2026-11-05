import tkinter as tk
import backend.logica as back
from tkinter import messagebox




def validar():
    
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    
    mensaje = back.validar_edad(nombre,edad)
    
    if mensaje == True:
        messagebox.showinfo("Validador", "Usted es mayor de edad")
    else:
        messagebox.showwarning("Validador", "Usted es menor de edad")
    


ventana = tk.Tk()
ventana.geometry("400x800")
ventana.config(bg="black")


#widgets

#etiqueta de edad

etiqueta_nombre = tk.Label(ventana, text="Ingrese su nombre: ", bg="black", fg="white", font="Arial,14")
etiqueta_nombre.pack(pady=20)

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady= 20)

etiqueta_edad = tk.Label(ventana, text="Ingrese su edad: ", bg="black", fg="white", font="Arial, 14")
etiqueta_edad.pack(pady=20)

entrada_edad = tk.Entry(ventana)
entrada_edad.pack(pady = 20)

boton = tk.Button(ventana, text="Presiona", font="Arial", command=validar)
boton.pack(pady=20)


ventana.mainloop()