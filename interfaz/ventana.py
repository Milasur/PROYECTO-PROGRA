import tkinter as tk
from logica.generador import (
    generar_contraseña_alfanumerica,
    generar_contraseña_robusta,
    generar_contraseña_desde_frase,
    generar_contraseña_desde_frase_aleatoria,
    generar_contraseña_passphrase,
)
from logica.evaluador import evaluar_fortaleza_contraseña

ventana = tk.Tk()
ventana.title("Gestor de Contraseñas")
ventana.geometry("600x400")
ventana.mainloop()


def al_presionar():
    etiqueta.config(text="¡Botón presionado!")


ventana = tk.Tk()
etiqueta = tk.Label(ventana, text="Hola mundo")
etiqueta.pack(pady=10)
boton = tk.Button(ventana, text="Presióname", command=al_presionar)
boton.pack(pady=10)
ventana.mainloop()
