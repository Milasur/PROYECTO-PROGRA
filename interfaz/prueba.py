import tkinter as tk


def al_presionar():
    etiqueta.config(
        text="Bienvenido a la sección de generación de contraseñas")


ventana = tk.Tk()
ventana.title("Gestor de Contraseñas")
ventana.geometry("600x400")
etiqueta = tk.Label(ventana, text="Sección Generar una contraseña")
etiqueta.pack(pady=10)
boton = tk.Button(ventana, text="Presióname", command=al_presionar)
boton.pack(pady=10)

ventana.mainloop()
