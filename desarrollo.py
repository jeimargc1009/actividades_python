def bienvenida(idioma):
    # Funcion que imprime un mensaje de bienvenida al usuario.
    if idioma == "es":
        print("¡Bienvenido al programa!")
    elif idioma == "en":
        print("¡welcome to the program!")

def factorial(numero):
    # Funcion que calcula el factorial de un numero enter utilizando un ciclo for.
    if numero < 0:
        return "No puede calcular el factorial de un numero negativo."
    if numero == 0:
        return 1

    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado

def es_primo(numero):
    # Funcion que determina si un numero es primo.
    if numero <=  1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

if __name__ == "__main__":
    bienvenida("es") 

    try:
        # Pide al usuario que ingrese un numero para calcular su factorial
        numero_primo_input = int(input("Ingresa un numero para verificar si es primo: "))
        if numero_primo_input < 0:
            print("No se puede determinar si un numero negativo es primo")
        else:
            print(f"¿El numero {numero_primo_input} es primo? {es_primo(numero_primo_input)}")

    except ValueError:
        print("Entrada invalida. Por favor, ingresa solo numeros enteros")
