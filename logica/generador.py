#Funcion 1: generar

def funcionContrasenaSimple():
    import random
    import string

    longitud_contrasena = 8
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud_contrasena))
    
    return contrasena
