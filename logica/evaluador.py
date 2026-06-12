from logica.generador import MAYUSCULAS
from logica.generador import MINUSCULAS
from logica.generador import DIGITOS
from logica.generador import SIMBOLOS
from datos.patrones import SECUENCIAS_NUMERICAS, PATRONES_COMUNES, CARACTERES_REPETIDOS
from datos.palabras_comunes import PALABRAS_COMUNES

# Funcion 8: Evaluar la fortaleza de una contraseña
'''
ENTRADAS:
    contraseña (str): contraseña a evaluar
SALIDAS:
    Fortaleza de la contraseña (int)
RESTRICCIONES:
    La fortaleza se calcula como el número de tipos de caracteres presentes.
    Tipos de caracteres: mayúsculas, minúsculas, dígitos, símbolos.'''


def evaluar_fortaleza_contraseña(contraseña):
    puntuacion = 0
    if len(contraseña) >= 4 and len(contraseña) <= 5:
        puntuacion += 1
    if len(contraseña) >= 6 and len(contraseña) <= 9:
        puntuacion += 2
    if len(contraseña) >= 10:
        puntuacion += 3
    apariciones_mayusculas = 0

    # Primero se cuenta la cantidad de mayusculas en la contraseña.
    for caracteres in contraseña:
        if caracteres in MAYUSCULAS:
            apariciones_mayusculas += 1

    # Luego se compara y se denota la puntuacion, de mayor a menor.

    if apariciones_mayusculas == 0:
        puntuacion += -1
    elif apariciones_mayusculas >= 3:
        puntuacion += 3
    elif apariciones_mayusculas >= 1:
        puntuacion += 1

    apariciones_minusculas = 0

    for caracteres in contraseña:
        if caracteres in MINUSCULAS:
            apariciones_minusculas += 1

    if apariciones_minusculas == 0:
        puntuacion += -1
    elif apariciones_minusculas >= 3:
        puntuacion += 3
    elif apariciones_minusculas >= 1:
        puntuacion += 1

    apariciones_digitos = 0

    for digitos in contraseña:
        if digitos in DIGITOS:
            apariciones_digitos += 1

    if apariciones_digitos == 0:
        puntuacion += -2
    elif apariciones_digitos >= 5:
        puntuacion += 3
    elif apariciones_digitos >= 3:
        puntuacion += 2
    elif apariciones_digitos >= 1:
        puntuacion += 1

    apariciones_simbolos = 0
    for simbolo in contraseña:
        if simbolo in SIMBOLOS:
            apariciones_simbolos += 1

    if apariciones_simbolos == 0:
        puntuacion += -1
    elif apariciones_simbolos >= 3:
        puntuacion += 3
    elif apariciones_simbolos >= 1:
        puntuacion += 1

    puntuacion += deteccion_patrones_inseguros(contraseña.lower())

    if puntuacion <= 5:
        clase = "Contraseña muy débil"
    elif puntuacion <= 8:
        clase = "Contraseña Media"
    elif puntuacion <= 12:
        clase = "Contraseña Fuerte"
    else:
        clase = "Contraseña Muy Fuerte"

    return clase, puntuacion


# Funcion 9: Evaluar la fortaleza de una contraseña
'''
ENTRADAS:
    contraseña (str): contraseña a evaluar
SALIDAS:
    Fortaleza de la contraseña (int)
RESTRICCIONES:
    La fortaleza se calcula como el número de tipos de caracteres presentes.
    Tipos de caracteres: mayúsculas, minúsculas, dígitos, símbolos.'''


TODOS_LOS_PATRONES = SECUENCIAS_NUMERICAS + \
    PATRONES_COMUNES + CARACTERES_REPETIDOS + PALABRAS_COMUNES


def deteccion_patrones_inseguros(contraseña, patrones=TODOS_LOS_PATRONES, indice=0, puntuacion=0):
    contraseña = contraseña.lower()

    if indice == len(patrones):
        if puntuacion == 0:
            return 3
        return puntuacion

    if patrones[indice] in contraseña:
        puntuacion -= 1

    return deteccion_patrones_inseguros(
        contraseña,
        patrones,
        indice + 1,
        puntuacion
    )
