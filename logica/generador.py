import random
import string

# Se definen variables que se usarán en todas las funciones.

mayusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
digitos = string.digits
simbolos = "!@#$%&*"

# Funcion 1: generar


# Funcion 4 -  Contraseña Robusta


"""
ENTRADAS:
Longitud deseada de la contraeña (int) 
SALIDAS:
Una contraseña robusta (str) 
RESTRICCIONES:
La longitud debe ser al menos 10 caracteres.
Debe incluir al menos una letra mayúscula, una letra minúscula, 
un número y un simbolo ( @ # $ % & *)
"""


def generar_contraseña_robusta(longitud):
    if longitud < 10:
        raise ValueError("La longitud de la contraseña debe ser de al menos 10 "
                         "caracteres para que sea robusta.")
