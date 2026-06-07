# Se importan las librerías que se van a usar.
import random
import string
from datos.banco_palabras import BANCO

# Se definen variables que se usarán en todas las funciones.

MAYUSCULAS = string.ascii_uppercase
MINUSCULAS = string.ascii_lowercase
DIGITOS = string.digits
SIMBOLOS = "!@#$%&*"

# Funcion 1: generar_contraseña

"""
Entradas: 
    longitud (int)
Salidas:    
    contraseña (str)
Restricciones: 
    La longitud debe ser mayor que 3,
    solo se deben utilizar dígitos del 0 al 9, debe considerarse una contraseña
    de baja segurida    d,cada dígito se podrá repetir a lo sumo 3 veces.
"""


def generar_contraseña_numerica(longitud):
    if longitud <= 3:
        raise ValueError("La longitud de la contraseña debe ser mayor que 3.")
    contraseña = ""
    for i in range(longitud):
        digito_aleatorio = random.randint(0, 9)
        contraseña += str(digito_aleatorio)
    return contraseña


# Funcion 2: generar_contraseña_letras
"""
Entradas: 
    longitud (int)
Salidas: 
    generar_contraseña_letras (str)
Restricciones: 
    La longitud debe ser mayor que 3,
    solo se deben utilizar letras minúsculas,
    no debe incluir números ni símbolos
"""


def generar_contraseña_letras(longitud):
    if longitud <= 3:
        raise ValueError("La longitud de la contraseña debe ser mayor que 3.")
    contraseña = ""
    for i in range(longitud):
        letra_aleatoria = random.choice(MINUSCULAS)
        contraseña += letra_aleatoria
    return contraseña


# Funcion 3: generar_contraseña_alfanumerica
"""
Entradas: 
    longitud (int)
Salidas: 
    generar_contraseña_alfanumerica (str)
Restricciones: 
    La longitud minima debe ser 6,
    debe conteener al menos una letra minuscula, 
    debe de tener al menos un numero, sin simbolos
"""


def generar_contraseña_alfanumerica(longitud):
    if longitud < 6:
        raise ValueError(
            "La longitud de la contraseña debe ser de al menos 6 caracteres.")
    minuscula_aleatoria = random.choice(MINUSCULAS)
    digito_aleatorio = random.choice(DIGITOS)
    contraseña = ""
    for i in range(longitud - 2):
        caracter_aleatorio = random.choice(MINUSCULAS + DIGITOS)
        contraseña += caracter_aleatorio
    contraseña = minuscula_aleatoria + digito_aleatorio + contraseña
    return contraseña


# Funcion 4 - Contraseña Robusta
"""
ENTRADAS:
    longitud (int): longitud deseada de la contraseña
SALIDAS:
    Una contraseña robusta (str)
RESTRICCIONES:
    La longitud debe ser al menos 10 caracteres.
    Debe incluir al menos una letra mayúscula, una letra minúscula,
    un número y un simbolo ( ! @ # $ % & *)
"""


def generar_contraseña_robusta(longitud):
    if longitud < 10:
        raise ValueError("La longitud de la contraseña debe ser de al menos 10 "
                         "caracteres para que sea robusta.")
    digito_aleatorio = random.choice(DIGITOS)
    mayuscula_aleatoria = random.choice(MAYUSCULAS)
    minuscula_aleatoria = random.choice(MINUSCULAS)
    simbolo_aleatorio = random.choice(SIMBOLOS)
    caracteres_posibles = MAYUSCULAS + MINUSCULAS + DIGITOS + SIMBOLOS
    contrasena_robusta = [digito_aleatorio, mayuscula_aleatoria,
                          minuscula_aleatoria, simbolo_aleatorio]
    for i in range(longitud - 4):
        contrasena_robusta += [random.choice(caracteres_posibles)]
    random.shuffle(contrasena_robusta)
    contrasena_robusta = "".join(contrasena_robusta)
    return contrasena_robusta


# Funcion 5 - Contraseña desde frase
"""
ENTRADAS:
    frase (str): frase de al menos 5 palabras
    simbolo (str): símbolo que se agrega al final de la contraseña
SALIDAS:
    Una contraseña basada en la frase (str)
RESTRICCIONES:
    La frase debe contener al menos 5 palabras.
    Se toma la letra inicial de cada palabra.
    Si la frase contiene números, estos se conservan en el orden en que aparecen.
    El símbolo debe ser uno de: ! @ # $ % & *
    El símbolo se agrega al final de la contraseña.
"""


def generar_contraseña_desde_frase(frase, simbolo):
    palabras = frase.split()
    contraseña = ""
    if len(palabras) < 5:
        raise ValueError("La frase debe tener al menos 5 palabras.")
    for palabra in palabras:
        if palabra.isdigit():
            contraseña += palabra
        else:
            contraseña += palabra[0]
    contraseña += simbolo
    return contraseña


# Funcion 6 - Contraseña desde frase aleatoria
"""
ENTRADAS:
    frase (str): frase de al menos 5 palabras
    simbolo (str): símbolo que se agrega al final de la contraseña
SALIDAS:
    Una contraseña basada en la frase (str)
RESTRICCIONES:
    La frase debe contener al menos 5 palabras.
    Se toma un carácter aleatorio de cada palabra.
    Si la frase contiene números, estos se conservan en el orden en que aparecen.
    El símbolo debe ser uno de: ! @ # $ % & *
    El símbolo se agrega al final de la contraseña.
"""


def generar_contraseña_desde_frase_aleatoria(frase, simbolo):
    palabras = frase.split()
    contraseña = ""
    if len(palabras) < 5:
        raise ValueError("La frase debe tener al menos 5 palabras.")
    for palabra in palabras:
        if palabra.isdigit():
            contraseña += palabra
        else:
            contraseña += random.choice(palabra)
    contraseña += simbolo
    return contraseña

# Funcion 7 -  Generación de passphrase


"""
ENTRADAS:
    Cantidad de palabras que se tomarán del banco de palabras. (int)
    Símbolo separador de entre "-_!#" (string)
    Número que irá al final de la contraseña (int)
SALIDAS:
    Contraseña generada incluyendo las palabras tomadas del banco,
    el símbolo separador, y el número proporcionados por el usuario en la entrada (string)
RESTRICCIONES:
    Deben ser al menos 3 palabras.
    Las palabras deben seleccionarse desde un banco predefinido en datos/banco_palabras.py
    El seperador debe ser alguno entre "-_!#"
    Debe agregar al menos un número.

"""


def generar_contraseña_passphrase(cantidad_palabras, separador, numero_final):
    SEPARADORES = "-_!#"
    contraseña = ""
    if cantidad_palabras < 3:
        raise ValueError("Deben ser al menos 3 palabras.")
    if separador not in SEPARADORES:
        raise ValueError("El separador debe ser uno de: - _ ! #")
    palabras_elegidas = random.sample(BANCO, cantidad_palabras)
    for palabra in palabras_elegidas:
        contraseña += palabra + separador
    contraseña += str(numero_final)
    return contraseña


if __name__ == "__main__":
    print(generar_contraseña_alfanumerica(8))
    print(generar_contraseña_robusta(12))
    try:
        print(generar_contraseña_robusta(8))
    except ValueError as error:
        print(f"Falló lo que tenía que fallar: {error}")
    print(generar_contraseña_desde_frase("Me llamo Josué Valles Sánchez", "!"))
    print(generar_contraseña_desde_frase("Mi clave es 42 segura hoy", "#"))
    try:
        print(generar_contraseña_desde_frase("corta frase", "@"))
    except ValueError as error:
        print(f"Falló lo que tenía que fallar {error}")
    print(generar_contraseña_desde_frase_aleatoria("Hola me llamo Josu XD", "!"))
    print(generar_contraseña_passphrase(3, "-", 78))
    try:
        print(generar_contraseña_passphrase(2, "-", 78))
    except ValueError as error:
        print(f"Falló lo que tenía que fallar {error}")
    print(generar_contraseña_passphrase(5, "-", 78))
