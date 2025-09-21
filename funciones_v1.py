def bienvenida(idioma): 
    # Funcion que imprime un mensaje de bienvenida al usuario.

    if idioma == "es":
        print("¡Bienvenido al programa!")
    elif idioma == "en":
        print("¡Welcome to the program!")

def factorial(numero):
    #funcion que calcula el factorial de un numero entero utilizando un ciclo for.

    resultado = 1
    for i in range(1, numero + 1):
        resultado = resultado * i
    return resultado

def es_primo(numero):
    # Funcion que determina si un numero es primo.

    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

if __name__ == "__main__":
    bienvenida("en")  

    numero = 6
    print(f"Factorial de {numero}: {factorial(numero)}")

    numero = 20
    print(f"¿El numero {numero_primo} es primo? {es_primo(numero _primo)}")               # type: ignore
            

    