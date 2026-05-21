import random

# Funcion 1: generar


def generar():
    print("Generando el código...")
    # Aquí puedes agregar la lógica para generar el código
    print("Código generado exitosamente.")

# Funcion 4 -  Contraseña Robusta


"""
ENTRADAS:
Longitud deseada de la contraeña (int) 
SALIDAS:
Una contraseña robusta (str) 
RESTRICCIONES:
La longitud debe ser al menos 10 caracteres.
Debe incluir al menos una letra mayúscula, una letra minúscula, un número y un simbolo ( @ # $ % & *)
"""


def generar_contraseña_robusta(longitud):

    # Casos de prueba:


print(generar_contraseña_robusta(12))  # Ejemplo de salida: "A1b@C3d$E5f"
# Ejemplo de salida: "Error: La longitud debe ser al menos 10 caracteres."
print(generar_contraseña_robusta(8))
