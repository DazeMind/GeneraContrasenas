import random
import string

def generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    contraseña_generada = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña_generada

def obtener_respuesta_si_no(pregunta):
    while True:
        respuesta = input(pregunta).strip().lower()
        if respuesta == 's' or respuesta == 'n':
            return respuesta
        else:
            print("| Por favor, ingresa 'S' o 'N'.")

def obtener_longitud_contraseña():
    while True:
        try:
            longitud = int(input("| Longitud de la contraseña (solo números): "))
            return longitud
        except ValueError:
            print("| Por favor, ingresa un número válido.")

if __name__ == "__main__":
    print("_____________________________________________________")
    print("| Generador de Contraseñas")
    longitud = obtener_longitud_contraseña()
    incluir_mayusculas = obtener_respuesta_si_no("| ¿Incluir mayúsculas? (S/N):") == 's'
    incluir_numeros = obtener_respuesta_si_no("| ¿Incluir números? (S/N):") == 's'
    incluir_simbolos = obtener_respuesta_si_no("| ¿Incluir símbolos? (S/N): ") == 's'

    contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_numeros, incluir_simbolos)
    print("| Contraseña generada: ", contraseña)
    print("|_____________________________________________________")
