import random
import string

def generar_contrasena(longitud):
    if longitud < 4:
        print("La contraseña debe tener al menos 4 caracteres.")
        return ""

    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    print("🔐 Generador de Contraseñas Seguras 🔐")
    try:
        longitud = int(input("¿Cuántos caracteres deseas en tu contraseña?: "))
        resultado = generar_contrasena(longitud)
        if resultado:
            print(f"Tu contraseña es: {resultado}")
    except ValueError:
        print("Por favor, ingresa un número válido.")

if __name__ == "__main__":
    main()
