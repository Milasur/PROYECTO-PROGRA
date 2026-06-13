import itertools

# Función 10: Simulación de ataque por fuerza bruta

"""
ENTRADAS:
    ● Contraseña objetivo.
    ● Conjunto de caracteres a probar.
    ● Longitud máxima de intento.
Restricciones:
    ● La longitud máxima recomendada para la simulación debe ser pequeña,
    por ejemplo 2 a 5 caracteres.
    ● El sistema debe mostrar la cantidad de intentos realizados.
SALIDAS:
    ● Indicación de si la contraseña fue encontrada o no.
El sistema genera combinaciones posibles con los caracteres permitidos. Luego
compara cada intento con la contraseña objetivo. Si coincide, informa que la
contraseña fue encontrada y muestra cuántos intentos tomó.
"""


def simulacion_fuerza_bruta_recursiva(contraseña_objetivo, caracteres, longitud, intentos=0, contador=1):
    # Caso base: si la longitud llega a 0, significa que no se encontró la contraseña
    if contador > longitud:
        return f"La contraseña no pudo ser descifrada. Se realizaron {intentos} intentos."

    # Evaluar todas las combinaciones de la longitud actual
    for opciones in itertools.product(caracteres, repeat=contador):
        intento_actual = ''.join(opciones)
        intentos += 1

        # Caso de éxito
        if intento_actual == contraseña_objetivo:
            return f"Contraseña encontrada en {intentos} intentos: {intento_actual}"

    # Se llama a la función reduciendo la longitud y pasando los intentos acumulados
    return simulacion_fuerza_bruta_recursiva(contraseña_objetivo, caracteres, longitud, intentos, contador + 1)
