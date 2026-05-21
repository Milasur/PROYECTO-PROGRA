# Funcion 1: generar


# Funcion 2: generar_contenido

print("Hola, soy el generador de contenido.")


def generar_contenido():
    print("Generando contenido...")
    # Aquí puedes agregar la lógica para generar el contenido deseado
    contenido = "Este es el contenido generado."
    return contenido


if __name__ == "__main__":
    contenido_generado = generar_contenido()
    print("Contenido generado:", contenido_generado)
