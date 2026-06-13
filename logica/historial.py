import os
import json
from datetime import datetime
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import base64

# ───────────────────────────────────°──────────
# CONFIGURACIÓN DEL CIFRADO
# ─────────────────────────────────────────────

# Clave de 24 bytes para 3DES (¡en un proyecto real nunca hardcodear!)
CLAVE_3DES = b"ProyectoTI1401ClaveSeg!!"  # exactamente 24 bytes
IV_3DES = b"InicioIV"                  # exactamente 8 bytes
# Ruta absoluta basada en el directorio del proyecto
ARCHIVO_HISTORIAL = os.path.join(os.path.dirname(
    os.path.dirname(__file__)), "historial.enc")


# ─────────────────────────────────────────────
# FUNCIONES DE CIFRADO / DESCIFRADO
# ─────────────────────────────────────────────

def cifrar_texto(texto: str) -> str:
    """
    Cifra un texto plano usando 3DES en modo CBC.
    Retorna el texto cifrado codificado en base64.
    """
    cipher = DES3.new(CLAVE_3DES, DES3.MODE_CBC, IV_3DES)
    datos = pad(texto.encode("utf-8"), DES3.block_size)
    cifrado = cipher.encrypt(datos)
    return base64.b64encode(cifrado).decode("utf-8")


def descifrar_texto(texto_cifrado: str) -> str:
    """
    Descifra un texto cifrado en base64 usando 3DES en modo CBC.
    Retorna el texto plano original.
    """
    cipher = DES3.new(CLAVE_3DES, DES3.MODE_CBC, IV_3DES)
    datos = base64.b64decode(texto_cifrado)
    descifrado = unpad(cipher.decrypt(datos), DES3.block_size)
    return descifrado.decode("utf-8")


# ─────────────────────────────────────────────
# FUNCIÓN 11: HISTORIAL DE CONTRASEÑAS
# ─────────────────────────────────────────────

def registrar_contrasena(contrasena: str, algoritmo: str,
                         longitud: int, fortaleza: str) -> None:
    """
    Registra una contraseña generada en el historial cifrado.

    Parámetros:
        contrasena : La contraseña generada.
        algoritmo  : Nombre del algoritmo usado (ej: "Numérica", "Robusta").
        longitud   : Longitud de la contraseña.
        fortaleza  : Clasificación de fortaleza (Débil/Media/Fuerte/Muy fuerte).
    """
    # Cargar historial existente (si hay)
    historial = cargar_historial()

    # Crear nuevo registro
    nuevo_registro = {
        "contrasena": contrasena,
        "algoritmo": algoritmo,
        "longitud": longitud,
        "fortaleza": fortaleza,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    historial.append(nuevo_registro)

    # Convertir a JSON y cifrar
    json_texto = json.dumps(historial, ensure_ascii=False, indent=2)
    contenido_cifrado = cifrar_texto(json_texto)

    # Guardar en archivo
    with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as archivo:
        archivo.write(contenido_cifrado)

    print(f"✅ Contraseña registrada en el historial ({ARCHIVO_HISTORIAL})")


def cargar_historial() -> list:
    """
    Carga y descifra el historial de contraseñas desde el archivo.
    Si el archivo no existe, retorna una lista vacía.

    Retorna:
        Lista de diccionarios con los registros del historial.
    """
    if not os.path.exists(ARCHIVO_HISTORIAL):
        return []

    with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as archivo:
        contenido_cifrado = archivo.read()

    json_texto = descifrar_texto(contenido_cifrado)
    return json.loads(json_texto)


def mostrar_historial() -> None:
    """
    Muestra en consola todos los registros del historial de contraseñas.
    """
    historial = cargar_historial()

    if not historial:
        print("📭 El historial está vacío.")
        return

    print("\n" + "═" * 60)
    print(f"{'HISTORIAL DE CONTRASEÑAS':^60}")
    print("═" * 60)

    for i, registro in enumerate(historial, start=1):
        print(f"\n  Registro #{i}")
        print(f"Fecha      : {registro['fecha']}")
        print(f"Contraseña : {registro['contrasena']}")
        print(f"Algoritmo  : {registro['algoritmo']}")
        print(f"Longitud   : {registro['longitud']}")
        print(f"Fortaleza  : {registro['fortaleza']}")
        print("  " + "-" * 56)

    print(f"\n  Total de registros: {len(historial)}")
    print("═" * 60 + "\n")


def borrar_historial() -> bool:
    """
    Borra todo el contenido del historial cifrado.
    Crea un archivo con una lista vacía cifrada.
    Retorna True si se ejecutó correctamente, False si hubo error.
    """
    try:
        # Crear un historial vacío (lista vacía en JSON)
        historial_vacio = []
        json_texto = json.dumps(historial_vacio, ensure_ascii=False, indent=2)
        contenido_cifrado = cifrar_texto(json_texto)

        # Escribir el archivo vacío cifrado
        with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as archivo:
            archivo.write(contenido_cifrado)

        print(f"🗑️ Historial eliminado ({ARCHIVO_HISTORIAL})")
        return True
    except Exception as e:
        print(f"❌ Error al borrar historial: {e}")
        return False
