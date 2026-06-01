from logica.generador import MAYUSCULAS
from logica.generador import MINUSCULAS
from logica.generador import DIGITOS
from logica.generador import SIMBOLOS

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
    aparicionesMayusculas = 0

    for caracteres in contraseña:
        if caracteres in MAYUSCULAS:
            aparicionesMayusculas += 1
    if aparicionesMayusculas == 0:
        puntuacion += -1
    elif aparicionesMayusculas >= 3:
        puntuacion += 3
    elif aparicionesMayusculas >= 1:
        puntuacion += 1

    aparicionesMinusculas = 0

    for caracteres in contraseña:
        if caracteres in MINUSCULAS:
            aparicionesMinusculas += 1
    if aparicionesMinusculas == 0:
        puntuacion += -1
    elif aparicionesMinusculas >= 3:
        puntuacion += 3
    elif aparicionesMinusculas >= 1:
        puntuacion += 1

    aparicionesDigitos = 0

    for digitos in contraseña:
        if digitos in DIGITOS:
            aparicionesDigitos += 1
    if aparicionesDigitos == 0:
        puntuacion += -1
    elif aparicionesDigitos >= 1:
        puntuacion += 1
    elif aparicionesDigitos >= 3:
        puntuacion += 2
    elif aparicionesDigitos >= 5:
        puntuacion += 3

    aparicionesSimbolos = 0
    for simbolo in contraseña:
        if simbolo in SIMBOLOS:
            aparicionesSimbolos += 1
    if aparicionesSimbolos == 0:
        puntuacion += -1
    elif aparicionesSimbolos >= 1:
        puntuacion += 1
    elif aparicionesSimbolos >= 3:
        puntuacion += 3
    return puntuacion
