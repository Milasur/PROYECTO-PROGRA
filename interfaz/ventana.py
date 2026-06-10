import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import tkinter as tk
from tkinter import messagebox

# IMPORTACIÓN DIRECTA DE TUS MÓDULOS DE LÓGICA
from logica import generador
from logica import evaluador
from logica import ataques

# -------------------------------------------------------------------------
# DESPLIEGUE DE VENTANAS INDEPENDIENTES (GUI NATIVA CON GRID)
# -------------------------------------------------------------------------

def abrir_f1():
    v = tk.Toplevel(ventana)
    v.title("Función 1: Numérica Simple")
    v.geometry("400x200")
    v.columnconfigure(1, weight=1)
    
    tk.Label(v, text="Longitud deseada:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_long = tk.Entry(v)
    entry_long.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Resultado:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_res = tk.Entry(v, font=("Courier", 11, "bold"))
    entry_res.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    
    def ejecutar():
        try:
            longitud = int(entry_long.get())
            res = generador.generar_contraseña_numerica(longitud)
            entry_res.delete(0, tk.END)
            entry_res.insert(0, res)
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=v)
        
    tk.Button(v, text="Generar", bg="#E0E0E0", command=ejecutar).grid(row=1, column=0, columnspan=2, pady=10)

def abrir_f2():
    v = tk.Toplevel(ventana)
    v.title("Función 2: Alfabética Simple")
    v.geometry("400x200")
    v.columnconfigure(1, weight=1)
    
    tk.Label(v, text="Longitud deseada:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_long = tk.Entry(v)
    entry_long.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Resultado:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_res = tk.Entry(v, font=("Courier", 11, "bold"))
    entry_res.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    
    def ejecutar():
        try:
            longitud = int(entry_long.get())
            res = generador.generar_contraseña_letras(longitud)
            entry_res.delete(0, tk.END)
            entry_res.insert(0, res)
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=v)
        
    tk.Button(v, text="Generar", bg="#E0E0E0", command=ejecutar).grid(row=1, column=0, columnspan=2, pady=10)

def abrir_f3():
    v = tk.Toplevel(ventana)
    v.title("Función 3: Alfanumérica")
    v.geometry("400x200")
    v.columnconfigure(1, weight=1)
    
    tk.Label(v, text="Longitud deseada:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_long = tk.Entry(v)
    entry_long.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Resultado:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_res = tk.Entry(v, font=("Courier", 11, "bold"))
    entry_res.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    
    def ejecutar():
        try:
            longitud = int(entry_long.get())
            res = generador.generar_contraseña_alfanumerica(longitud)
            entry_res.delete(0, tk.END)
            entry_res.insert(0, res)
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=v)
        
    tk.Button(v, text="Generar", bg="#E0E0E0", command=ejecutar).grid(row=1, column=0, columnspan=2, pady=10)

def abrir_f4():
    v = tk.Toplevel(ventana)
    v.title("Función 4: Contraseña Robusta")
    v.geometry("400x200")
    v.columnconfigure(1, weight=1)
    
    tk.Label(v, text="Longitud deseada:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_long = tk.Entry(v)
    entry_long.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Resultado:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_res = tk.Entry(v, font=("Courier", 11, "bold"))
    entry_res.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    
    def ejecutar():
        try:
            longitud = int(entry_long.get())
            res = generador.generar_contraseña_robusta(longitud)
            entry_res.delete(0, tk.END)
            entry_res.insert(0, res)
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=v)
        
    tk.Button(v, text="Generar", bg="#E0E0E0", command=ejecutar).grid(row=1, column=0, columnspan=2, pady=10)

def abrir_f5():
    v = tk.Toplevel(ventana)
    v.title("Función 5: Basada en Frase")
    v.geometry("450x250")
    v.columnconfigure(1, weight=1)
    
    tk.Label(v, text="Frase base (mín 5 palabras):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_frase = tk.Entry(v)
    entry_frase.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Símbolo final:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_simbolo = tk.Entry(v)
    entry_simbolo.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Resultado:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_res = tk.Entry(v, font=("Courier", 11, "bold"))
    entry_res.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
    
    def ejecutar():
        try:
            frase = entry_frase.get()
            simbolo = entry_simbolo.get()
            res = generador.generar_contraseña_desde_frase(frase, simbolo)
            entry_res.delete(0, tk.END)
            entry_res.insert(0, res)
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=v)
            
    tk.Button(v, text="Generar", bg="#E0E0E0", command=ejecutar).grid(row=2, column=0, columnspan=2, pady=10)

def abrir_f6():
    v = tk.Toplevel(ventana)
    v.title("Función 6: Frase Aleatoria")
    v.geometry("450x250")
    v.columnconfigure(1, weight=1)
    
    tk.Label(v, text="Frase base (mín 5 palabras):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_frase = tk.Entry(v)
    entry_frase.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Símbolo final:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_simbolo = tk.Entry(v)
    entry_simbolo.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Resultado:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_res = tk.Entry(v, font=("Courier", 11, "bold"))
    entry_res.grid(row=3, column=1, padx=10, pady=10, sticky="ew")
    
    def ejecutar():
        try:
            frase = entry_frase.get()
            simbolo = entry_simbolo.get()
            res = generador.generar_contraseña_desde_frase_aleatoria(frase, simbolo)
            entry_res.delete(0, tk.END)
            entry_res.insert(0, res)
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=v)
            
    tk.Button(v, text="Generar", bg="#E0E0E0", command=ejecutar).grid(row=2, column=0, columnspan=2, pady=10)

def abrir_f7():
    v = tk.Toplevel(ventana)
    v.title("Función 7: Passphrase")
    v.geometry("450x280")
    v.columnconfigure(1, weight=1)
    
    tk.Label(v, text="Cantidad de palabras:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_cant = tk.Entry(v)
    entry_cant.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Separador (- _ ! #):").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_sep = tk.Entry(v)
    entry_sep.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Número final:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_num = tk.Entry(v)
    entry_num.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Resultado:").grid(row=4, column=0, padx=10, pady=10, sticky="w")
    entry_res = tk.Entry(v, font=("Courier", 11, "bold"))
    entry_res.grid(row=4, column=1, padx=10, pady=10, sticky="ew")
    
    def ejecutar():
        try:
            cant = int(entry_cant.get())
            separador = entry_sep.get()
            num_final = int(entry_num.get())
            res = generador.generar_contraseña_passphrase(cant, separador, num_final)
            entry_res.delete(0, tk.END)
            entry_res.insert(0, res)
        except ValueError as error:
            messagebox.showerror("Error", str(error), parent=v)
            
    tk.Button(v, text="Generar", bg="#E0E0E0", command=ejecutar).grid(row=3, column=0, columnspan=2, pady=10)

def abrir_f8_f9():
    v = tk.Toplevel(ventana)
    v.title("Función 8 y 9: Evaluar Fortaleza")
    v.geometry("450x250")
    v.columnconfigure(1, weight=1)
    
    tk.Label(v, text="Contraseña a evaluar:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_pwd = tk.Entry(v)
    entry_pwd.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Salida Numérica (Patrones F9):").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    lbl_patrones = tk.Label(v, text="-", font=("Arial", 10, "bold"))
    lbl_patrones.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    
    tk.Label(v, text="Clasificación de Fortaleza (F8):").grid(row=3, column=0, padx=10, pady=10, sticky="w")
    lbl_clase = tk.Label(v, text="-", font=("Arial", 10, "bold"))
    lbl_clase.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    
    def ejecutar():
        pwd = entry_pwd.get()
        f9_val = evaluador.deteccion_patrones_inseguros(pwd)
        clase, pts = evaluador.evaluar_fortaleza_contraseña(pwd)
        
        lbl_patrones.config(text=str(f9_val))
        lbl_clase.config(text=f"{clase} ({pts} pts)")
        
    tk.Button(v, text="Evaluar Contraseña", bg="#E0E0E0", command=ejecutar).grid(row=1, column=0, columnspan=2, pady=10)

def abrir_f10():
    v = tk.Toplevel(ventana)
    v.title("Función 10: Fuerza Bruta")
    v.geometry("450x250")
    v.columnconfigure(1, weight=1)
    
    tk.Label(v, text="Contraseña objetivo (2 a 5 characteres):").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_obj = tk.Entry(v)
    entry_obj.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Caracteres a probar:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_chars = tk.Entry(v)
    entry_chars.insert(0, "0123456789")
    entry_chars.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
    
    tk.Label(v, text="Longitud máxima de contraseña:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_max = tk.Entry(v)
    entry_max.insert(0, "4")
    entry_max.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    
    def ejecutar():
        obj = entry_obj.get()
        chars = entry_chars.get()
        try:
            lon_max = int(entry_max.get())
            if len(obj) < 2 or len(obj) > 5:
                messagebox.showerror("Error", "La contraseña objetivo debe ser de 2 a 5 caracteres.", parent=v)
                return
            
            resultado_ataque = ataques.simulacion_fuerza_bruta_recursiva(obj, chars, lon_max)
            messagebox.showinfo("Simulación Completa", resultado_ataque, parent=v)
        except ValueError:
            messagebox.showerror("Error", "Ingrese una longitud máxima entera válida.", parent=v)
        
    tk.Button(v, text="Iniciar Simulación", bg="#E0E0E0", command=ejecutar).grid(row=3, column=0, columnspan=2, pady=10)

# -------------------------------------------------------------------------
# INTERFAZ DE USUARIO PRINCIPAL (F12)
# -------------------------------------------------------------------------
ventana = tk.Tk()
ventana.title("TEC - Gestor de Contraseñas (ATI)")
ventana.geometry("550x450")

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

tk.Label(ventana, text="GESTOR DE CONTRASEÑAS", font=("Arial", 13, "bold")).grid(row=0, column=0, columnspan=2, pady=15)

tk.Button(ventana, 
          text="F1: Numérica Simple",
          width=25, 
          command=abrir_f1).grid(row=1, column=0, padx=15, pady=6, sticky="ew")
tk.Button(ventana, 
          text="F2: Alfabética Simple",
          width=25, 
          command=abrir_f2).grid(row=1, column=1, padx=15, pady=6, sticky="ew")
tk.Button(ventana,
          text="F3: Alfanumérica",
          width=25, 
          command=abrir_f3).grid(row=2, column=0, padx=15, pady=6, sticky="ew")
tk.Button(ventana, 
          text="F4: Contraseña Robusta", 
          width=25, 
          command=abrir_f4).grid(row=2, column=1, padx=15, pady=6, sticky="ew")
tk.Button(ventana, 
          text="F5: Basada en Frase", 
          width=25, 
          command=abrir_f5).grid(row=3, column=0, padx=15, pady=6, sticky="ew")
tk.Button(ventana, 
          text="F6: Frase Aleatoria", 
          width=25, 
          command=abrir_f6).grid(row=3, column=1, padx=15, pady=6, sticky="ew")
tk.Button(ventana, 
          text="F7: Passphrase", 
          width=25, 
          command=abrir_f7).grid(row=4, column=0, padx=15, pady=6, sticky="ew")

tk.Label(ventana, text="Módulos de Análisis y Ataque", font=("Arial", 10, "italic")).grid(row=5, column=0, columnspan=2, pady=15)

tk.Button(ventana, text="F8/F9: Evaluar Fortaleza y Patrones", command=abrir_f8_f9).grid(row=6, column=0, columnspan=2, padx=15, pady=6, sticky="ew")
tk.Button(ventana, text="F10: Simulación Fuerza Bruta", command=abrir_f10).grid(row=7, column=0, columnspan=2, padx=15, pady=6, sticky="ew")

ventana.mainloop()