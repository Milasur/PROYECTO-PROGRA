import tkinter as tk
from tkinter import messagebox
from logica import historial
from logica import generador
from logica import evaluador
from logica import ataques

# ── Paleta de colores ──────────────────────────────────────────────────────────
BG = "#0D1B2A"   # fondo oscuro principal
BG_SUB = "#1B2838"   # fondo sub-ventanas
AZUL = "#2979FF"   # botones generadores
ROJO = "#EF5350"   # botones análisis / ataque
TEXTO = "#E8F4FD"   # texto general
TEXTO2 = "#90CAF9"   # texto secundario / subtítulos
ENTRY_BG = "#243447"   # fondo de campos de entrada
ENTRY_FG = "#FFFFFF"   # texto en campos

F_TITULO = ("Helvetica", 15, "bold")
F_LABEL = ("Helvetica", 10)
F_BTN = ("Helvetica", 10, "bold")
F_RES = ("Courier", 12, "bold")

# ── Helpers de estilo ──────────────────────────────────────────────────────────


def _label(padre, texto, **kw):
    return tk.Label(padre, text=texto, bg=BG_SUB, fg=TEXTO, font=F_LABEL, **kw)


def _entry(padre, **kw):
    return tk.Entry(padre, bg=ENTRY_BG, fg=ENTRY_FG,
                    insertbackground=ENTRY_FG, relief="flat",
                    font=F_LABEL, **kw)


def _entry_res(padre):
    return tk.Entry(padre, bg=ENTRY_BG, fg="#64FF9E",
                    insertbackground="#64FF9E", relief="flat",
                    font=F_RES, state="normal")


def _btn(padre, texto, cmd, color=AZUL):
    return tk.Button(padre, text=texto, command=cmd,
                     bg=color, fg="#FFFFFF", font=F_BTN,
                     relief="flat", cursor="hand2",
                     activebackground="#1565C0", activeforeground="#FFFFFF",
                     padx=10, pady=4)


def _setup_subventana(v, titulo, geo="430x220"):
    v.title(titulo)
    v.geometry(geo)
    v.configure(bg=BG_SUB)
    v.resizable(False, False)
    v.columnconfigure(1, weight=1)

# ── Sub-ventanas ───────────────────────────────────────────────────────────────


def abrir_f1(raiz):
    v = tk.Toplevel(raiz)
    _setup_subventana(v, "F1 · Numérica Simple")

    _label(v, "Longitud deseada:").grid(
        row=0, column=0, padx=14, pady=12, sticky="w")
    e_long = _entry(v)
    e_long.grid(row=0, column=1, padx=14, pady=12, sticky="ew")

    e_res = _entry_res(v)
    e_res.grid(row=2, column=1, padx=14, pady=12, sticky="ew")
    _label(v, "Resultado:").grid(row=2, column=0, padx=14, sticky="w")

    def ejecutar():
        try:
            res = generador.generar_contraseña_numerica(int(e_long.get()))

            fortaleza, _ = evaluador.evaluar_fortaleza_contraseña(res)

            historial.registrar_contrasena(
                res,
                "Numérica",
                len(res),
                fortaleza
            )

            e_res.delete(0, tk.END)
            e_res.insert(0, res)
        except ValueError as err:
            messagebox.showerror("Error", str(err), parent=v)

    _btn(v, "Generar", ejecutar).grid(row=1, column=0, columnspan=2, pady=8)


def abrir_f2(raiz):
    v = tk.Toplevel(raiz)
    _setup_subventana(v, "F2 · Alfabética Simple")

    _label(v, "Longitud deseada:").grid(
        row=0, column=0, padx=14, pady=12, sticky="w")
    e_long = _entry(v)
    e_long.grid(row=0, column=1, padx=14, pady=12, sticky="ew")

    e_res = _entry_res(v)
    e_res.grid(row=2, column=1, padx=14, pady=12, sticky="ew")
    _label(v, "Resultado:").grid(row=2, column=0, padx=14, sticky="w")

    def ejecutar():
        try:
            res = generador.generar_contraseña_letras(int(e_long.get()))

            fortaleza, _ = evaluador.evaluar_fortaleza_contraseña(res)

            historial.registrar_contrasena(
                res, "Alfabética", len(res), fortaleza)

            e_res.delete(0, tk.END)
            e_res.insert(0, res)
        except ValueError as err:
            messagebox.showerror("Error", str(err), parent=v)

    _btn(v, "Generar", ejecutar).grid(row=1, column=0, columnspan=2, pady=8)


def abrir_f3(raiz):
    v = tk.Toplevel(raiz)
    _setup_subventana(v, "F3 · Alfanumérica")

    _label(v, "Longitud deseada (mín 6):").grid(
        row=0, column=0, padx=14, pady=12, sticky="w")
    e_long = _entry(v)
    e_long.grid(row=0, column=1, padx=14, pady=12, sticky="ew")

    e_res = _entry_res(v)
    e_res.grid(row=2, column=1, padx=14, pady=12, sticky="ew")
    _label(v, "Resultado:").grid(row=2, column=0, padx=14, sticky="w")

    def ejecutar():
        try:
            res = generador.generar_contraseña_alfanumerica(int(e_long.get()))

            fortaleza, _ = evaluador.evaluar_fortaleza_contraseña(res)

            historial.registrar_contrasena(
                res, "Alfanumérica", len(res), fortaleza)

            e_res.delete(0, tk.END)
            e_res.insert(0, res)
        except ValueError as err:
            messagebox.showerror("Error", str(err), parent=v)

    _btn(v, "Generar", ejecutar).grid(row=1, column=0, columnspan=2, pady=8)


def abrir_f4(raiz):
    v = tk.Toplevel(raiz)
    _setup_subventana(v, "F4 · Contraseña Robusta")

    _label(v, "Longitud deseada (mín 10):").grid(
        row=0, column=0, padx=14, pady=12, sticky="w")
    e_long = _entry(v)
    e_long.grid(row=0, column=1, padx=14, pady=12, sticky="ew")

    e_res = _entry_res(v)
    e_res.grid(row=2, column=1, padx=14, pady=12, sticky="ew")
    _label(v, "Resultado:").grid(row=2, column=0, padx=14, sticky="w")

    def ejecutar():
        try:
            res = generador.generar_contraseña_robusta(int(e_long.get()))

            fortaleza, _ = evaluador.evaluar_fortaleza_contraseña(res)

            historial.registrar_contrasena(res, "Robusta", len(res), fortaleza)

            e_res.delete(0, tk.END)
            e_res.insert(0, res)
        except ValueError as err:
            messagebox.showerror("Error", str(err), parent=v)

    _btn(v, "Generar", ejecutar).grid(row=1, column=0, columnspan=2, pady=8)


def abrir_f5(raiz):
    v = tk.Toplevel(raiz)
    _setup_subventana(v, "F5 · Basada en Frase", "450x260")

    _label(v, "Frase base (mín 5 palabras):").grid(
        row=0, column=0, padx=14, pady=10, sticky="w")
    e_frase = _entry(v)
    e_frase.grid(row=0, column=1, padx=14, pady=10, sticky="ew")

    _label(v, "Símbolo final:").grid(
        row=1, column=0, padx=14, pady=10, sticky="w")
    e_simbolo = _entry(v)
    e_simbolo.grid(row=1, column=1, padx=14, pady=10, sticky="ew")

    e_res = _entry_res(v)
    e_res.grid(row=3, column=1, padx=14, pady=10, sticky="ew")
    _label(v, "Resultado:").grid(row=3, column=0, padx=14, sticky="w")

    def ejecutar():
        try:
            res = generador.generar_contraseña_desde_frase(
                e_frase.get(), e_simbolo.get())

            fortaleza, _ = evaluador.evaluar_fortaleza_contraseña(res)

            historial.registrar_contrasena(
                res, "Basada en frase", len(res), fortaleza)

            e_res.delete(0, tk.END)
            e_res.insert(0, res)
        except ValueError as err:
            messagebox.showerror("Error", str(err), parent=v)

    _btn(v, "Generar", ejecutar).grid(row=2, column=0, columnspan=2, pady=8)


def abrir_f6(raiz):
    v = tk.Toplevel(raiz)
    _setup_subventana(v, "F6 · Frase Aleatoria", "450x260")

    _label(v, "Frase base (mín 5 palabras):").grid(
        row=0, column=0, padx=14, pady=10, sticky="w")
    e_frase = _entry(v)
    e_frase.grid(row=0, column=1, padx=14, pady=10, sticky="ew")

    _label(v, "Símbolo final:").grid(
        row=1, column=0, padx=14, pady=10, sticky="w")
    e_simbolo = _entry(v)
    e_simbolo.grid(row=1, column=1, padx=14, pady=10, sticky="ew")

    e_res = _entry_res(v)
    e_res.grid(row=3, column=1, padx=14, pady=10, sticky="ew")
    _label(v, "Resultado:").grid(row=3, column=0, padx=14, sticky="w")

    def ejecutar():
        try:
            res = generador.generar_contraseña_desde_frase_aleatoria(
                e_frase.get(), e_simbolo.get())

            fortaleza, _ = evaluador.evaluar_fortaleza_contraseña(res)

            historial.registrar_contrasena(
                res, "Frase aleatoria", len(res), fortaleza)

            e_res.delete(0, tk.END)
            e_res.insert(0, res)
        except ValueError as err:
            messagebox.showerror("Error", str(err), parent=v)

    _btn(v, "Generar", ejecutar).grid(row=2, column=0, columnspan=2, pady=8)


def abrir_f7(raiz):
    v = tk.Toplevel(raiz)
    _setup_subventana(v, "F7 · Passphrase", "450x300")

    _label(v, "Cantidad de palabras (mín 3):").grid(
        row=0, column=0, padx=14, pady=10, sticky="w")
    e_cant = _entry(v)
    e_cant.grid(row=0, column=1, padx=14, pady=10, sticky="ew")

    _label(v, "Separador (- _ ! #):").grid(row=1,
                                           column=0, padx=14, pady=10, sticky="w")
    e_sep = _entry(v)
    e_sep.grid(row=1, column=1, padx=14, pady=10, sticky="ew")

    _label(v, "Número final:").grid(
        row=2, column=0, padx=14, pady=10, sticky="w")
    e_num = _entry(v)
    e_num.grid(row=2, column=1, padx=14, pady=10, sticky="ew")

    e_res = _entry_res(v)
    e_res.grid(row=4, column=1, padx=14, pady=10, sticky="ew")
    _label(v, "Resultado:").grid(row=4, column=0, padx=14, sticky="w")

    def ejecutar():
        try:
            res = generador.generar_contraseña_passphrase(
                int(e_cant.get()), e_sep.get(), int(e_num.get()))
            fortaleza, _ = evaluador.evaluar_fortaleza_contraseña(res)

            historial.registrar_contrasena(
                res, "Passphrase", len(res), fortaleza)

            e_res.delete(0, tk.END)
            e_res.insert(0, res)
        except ValueError as err:
            messagebox.showerror("Error", str(err), parent=v)

    _btn(v, "Generar", ejecutar).grid(row=3, column=0, columnspan=2, pady=8)


def abrir_f8_f9(raiz):
    v = tk.Toplevel(raiz)
    _setup_subventana(v, "F8 / F9 · Evaluar Fortaleza", "470x270")

    _label(v, "Contraseña a evaluar:").grid(
        row=0, column=0, padx=14, pady=12, sticky="w")
    e_pwd = _entry(v)
    e_pwd.grid(row=0, column=1, padx=14, pady=12, sticky="ew")

    _label(v, "Patrones (F9):").grid(
        row=2, column=0, padx=14, pady=8, sticky="w")
    lbl_patrones = tk.Label(v, text="—", bg=BG_SUB,
                            fg=TEXTO2, font=("Helvetica", 11, "bold"))
    lbl_patrones.grid(row=2, column=1, padx=14, sticky="w")

    _label(v, "Clasificación (F8):").grid(
        row=3, column=0, padx=14, pady=8, sticky="w")
    lbl_clase = tk.Label(v, text="—", bg=BG_SUB,
                         fg="#64FF9E", font=("Helvetica", 11, "bold"))
    lbl_clase.grid(row=3, column=1, padx=14, sticky="w")

    def ejecutar():
        pwd = e_pwd.get()
        f9_val = evaluador.deteccion_patrones_inseguros(pwd)
        clase, pts = evaluador.evaluar_fortaleza_contraseña(pwd)
        lbl_patrones.config(text=str(f9_val))
        lbl_clase.config(text=f"{clase}  ({pts} pts)")

    _btn(v, "Evaluar Contraseña", ejecutar).grid(
        row=1, column=0, columnspan=2, pady=10)


def abrir_f10(raiz):
    v = tk.Toplevel(raiz)
    _setup_subventana(v, "F10 · Simulación Fuerza Bruta", "470x260")

    _label(v, "Contraseña objetivo (2–5 caracteres):").grid(
        row=0, column=0, padx=14, pady=10, sticky="w")
    e_obj = _entry(v)
    e_obj.grid(row=0, column=1, padx=14, pady=10, sticky="ew")

    _label(v, "Caracteres a probar:").grid(
        row=1, column=0, padx=14, pady=10, sticky="w")
    e_chars = _entry(v)
    e_chars.insert(0, "0123456789")
    e_chars.grid(row=1, column=1, padx=14, pady=10, sticky="ew")

    _label(v, "Longitud máxima:").grid(
        row=2, column=0, padx=14, pady=10, sticky="w")
    e_max = _entry(v)
    e_max.insert(0, "4")
    e_max.grid(row=2, column=1, padx=14, pady=10, sticky="ew")

    def ejecutar():
        obj = e_obj.get()
        try:
            lon_max = int(e_max.get())
            if len(obj) < 2 or len(obj) > 5:
                messagebox.showerror(
                    "Error", "La contraseña objetivo debe ser de 2 a 5 caracteres.", parent=v)
                return
            resultado = ataques.simulacion_fuerza_bruta_recursiva(
                obj, e_chars.get(), lon_max)
            messagebox.showinfo("Simulación Completa", resultado, parent=v)
        except ValueError:
            messagebox.showerror(
                "Error", "Ingrese una longitud máxima entera válida.", parent=v)

    _btn(v, "Iniciar Simulación", ejecutar, color=ROJO).grid(
        row=3, column=0, columnspan=2, pady=10)


def abrir_f13(raiz):
    v = tk.Toplevel(raiz)
    _setup_subventana(v, "F13 · Leetspeak Compuesta", "450x260")

    _label(v, "Frase (mín 3 palabras):").grid(
        row=0, column=0, padx=14, pady=10, sticky="w")
    e_frase = _entry(v)
    e_frase.grid(row=0, column=1, padx=14, pady=10, sticky="ew")

    _label(v, "Número final:").grid(
        row=1, column=0, padx=14, pady=10, sticky="w")
    e_numero = _entry(v)
    e_numero.grid(row=1, column=1, padx=14, pady=10, sticky="ew")

    e_res = _entry_res(v)
    e_res.grid(row=3, column=1, padx=14, pady=10, sticky="ew")
    _label(v, "Resultado:").grid(row=3, column=0, padx=14, sticky="w")

    def ejecutar():
        try:
            res = generador.generar_contraseña_leetspeak(
                e_frase.get(), int(e_numero.get()))

            fortaleza, _ = evaluador.evaluar_fortaleza_contraseña(res)

            historial.registrar_contrasena(
                res, "Leetspeak", len(res), fortaleza)

            e_res.delete(0, tk.END)
            e_res.insert(0, res)
        except ValueError as err:
            messagebox.showerror("Error", str(err), parent=v)

    _btn(v, "Generar", ejecutar).grid(row=2, column=0, columnspan=2, pady=8)


# ── Ventana principal ──────────────────────────────────────────────────────────

def abrir_historial(raiz):
    v = tk.Toplevel(raiz)
    _setup_subventana(v, "Historial de Contraseñas", "700x400")

    historial_data = historial.cargar_historial()

    if not historial_data:
        _label(v, "No hay contraseñas registradas.").pack(pady=20)
        return

    texto = tk.Text(
        v,
        bg=ENTRY_BG,
        fg=TEXTO,
        font=("Courier", 10)
    )
    texto.pack(fill="both", expand=True, padx=10, pady=10)

    for i, registro in enumerate(historial_data, start=1):
        texto.insert(tk.END, f"Registro #{i}\n")
        texto.insert(tk.END, f"Fecha: {registro['fecha']}\n")
        texto.insert(tk.END, f"Contraseña: {registro['contrasena']}\n")
        texto.insert(tk.END, f"Algoritmo: {registro['algoritmo']}\n")
        texto.insert(tk.END, f"Longitud: {registro['longitud']}\n")
        texto.insert(tk.END, f"Fortaleza: {registro['fortaleza']}\n")
        texto.insert(tk.END, "-" * 50 + "\n")

    texto.config(state="disabled")

    def _on_borrar():
        if not messagebox.askyesno("Confirmar", "¿Borrar todo el historial? Esta acción no se puede deshacer.", parent=v):
            return
        ok = historial.borrar_historial()
        if ok:
            texto.config(state="normal")
            texto.delete("1.0", tk.END)
            texto.insert(tk.END, "No hay contraseñas registradas.")
            texto.config(state="disabled")
            messagebox.showinfo(
                "Borrado", "Historial borrado correctamente.", parent=v)
        else:
            messagebox.showinfo(
                "Información", "No había historial para borrar.", parent=v)

    btn_frame = tk.Frame(v, bg=BG_SUB)
    btn_frame.pack(fill="x", padx=10, pady=(0, 10))
    _btn(btn_frame, "Borrar Historial", _on_borrar, color=ROJO).pack(side="right")


def iniciar_app():
    ventana = tk.Tk()
    ventana.title("TEC · Gestor de Contraseñas")
    ventana.geometry("560x480")
    ventana.configure(bg=BG)
    ventana.resizable(False, False)

    ventana.columnconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)

    # Título
    tk.Label(ventana, text="GESTOR DE CONTRASEÑAS",
             bg=BG, fg=TEXTO, font=F_TITULO).grid(
        row=0, column=0, columnspan=2, pady=18)

    # Botones generadores
    def boton(texto, fn, fila, col, ancho=22):
        tk.Button(ventana, text=texto, width=ancho,
                  bg=AZUL, fg="#FFFFFF", font=F_BTN,
                  relief="flat", cursor="hand2",
                  activebackground="#1565C0", activeforeground="#FFFFFF",
                  command=fn).grid(row=fila, column=col, padx=12, pady=5, sticky="ew")

    boton("F1 · Numérica Simple", lambda: abrir_f1(ventana),  1, 0)
    boton("F2 · Alfabética Simple", lambda: abrir_f2(ventana),  1, 1)
    boton("F3 · Alfanumérica", lambda: abrir_f3(ventana),  2, 0)
    boton("F4 · Contraseña Robusta", lambda: abrir_f4(ventana),  2, 1)
    boton("F5 · Basada en Frase", lambda: abrir_f5(ventana),  3, 0)
    boton("F6 · Frase Aleatoria", lambda: abrir_f6(ventana),  3, 1)
    boton("F7 · Passphrase", lambda: abrir_f7(ventana),  4, 0)
    boton("F13 · Leetspeak Compuesta", lambda: abrir_f13(ventana), 4, 1)

    # Separador análisis
    tk.Label(ventana, text="── Análisis y Ataque ──",
             bg=BG, fg=TEXTO2, font=("Helvetica", 10, "italic")).grid(
        row=5, column=0, columnspan=2, pady=12)

    # Botones análisis (rojo)
    tk.Button(ventana, text="F8 / F9 · Evaluar Fortaleza y Patrones",
              bg=ROJO, fg="#FFFFFF", font=F_BTN,
              relief="flat", cursor="hand2",
              activebackground="#C62828", activeforeground="#FFFFFF",
              command=lambda: abrir_f8_f9(ventana)).grid(
        row=6, column=0, columnspan=2, padx=12, pady=5, sticky="ew")

    tk.Button(ventana, text="F10 · Simulación de Fuerza Bruta",
              bg=ROJO, fg="#FFFFFF", font=F_BTN,
              relief="flat", cursor="hand2",
              activebackground="#C62828", activeforeground="#FFFFFF",
              command=lambda: abrir_f10(ventana)).grid(
        row=7, column=0, columnspan=2, padx=12, pady=5, sticky="ew")

    tk.Button(ventana, text="F11 · Ver Historial",
              bg=ROJO, fg="#FFFFFF", font=F_BTN,
              relief="flat", cursor="hand2",
              activebackground="#C62828", activeforeground="#FFFFFF",
              command=lambda: abrir_historial(ventana)).grid(
        row=8, column=0, columnspan=2, padx=12, pady=5, sticky="ew")

    ventana.mainloop()
