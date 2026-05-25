import random

#Funcion 1: generar_contraseña
'''Entradas: longitud (int)
Salidas: contraseña (str)
Restricciones: La longitud debe ser mayor que 3,  solo se deben utilizar dígitos del 0 al 9, debe considerarse una contraseña de baja seguridad,
cada dígito se podrá repetir a lo sumo 3 veces.
'''

def generar_contraseña_numerica(longitud):
    contraseña = ""
    for i in range(longitud):
        dígito_aleatorio = random.randint(0, 9)
        contraseña += str(dígito_aleatorio)
    return contraseña
print(generar_contraseña_numerica(8))

#Funcion 2: generar_contraseña_letras
'''Entradas: longitud (int)
Salidas: generar_contraseña_letras (str)
Restricciones: La longitud debe ser mayor que 3,  solo se deben utilizar letras minúsculas, no debe incluir números ni símbolos
'''
def generar_contraseña_letras(longitud):
    contraseña = ""
    for i in range(longitud):
        letra_aleatoria = random.choice("abcdefghijklmnopqrstuvwxyz")
        contraseña += letra_aleatoria
    return contraseña
print(generar_contraseña_letras(8))

#Funcion 3: generar_contraseña_alfanumerica
'''Entradas: longitud (int)
Salidas: generar_contraseña_alfanumerica (str)
Restricciones: La longitud minima debe ser 6,  debe conteener al menos una letra minuscula, debe de tener al menos un numero, sin simbolos
'''
def generar_contraseña_alfanumerica(longitud):
    contraseña = ""
    for i in range(longitud):
        if i % 2 == 0:
            letra_aleatoria = random.choice("abcdefghijklmnopqrstuvwxyz")
            contraseña += letra_aleatoria
        else:
            dígito_aleatorio = random.randint(0, 9)
            contraseña += str(dígito_aleatorio)
    return contraseña
print(generar_contraseña_alfanumerica(8))