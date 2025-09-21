import math

# Crear una lista para almacenar las temperaturas
temperaturas = []
dias = 8

# Usa un bucle 'for' para pedirle al usuario las temperaturas de 8 dias
for i in range(dias):
    while True:
        try: 
            #pedir la temperatura al usuario
            temp = float(input(f"Ingresa la temperatura del dia {i + 1}: "))
            temperaturas.append(temp)
            break
        except ValueError:
            # Manejar el error si el usurio ingresa algo que no es un número
            print("Entrda no válida. Por favor, Ingrresa un número.")

# Calcular las estadisticas
if temperaturas:  # Asegurarse de que la lista no esté vacía
    # Calcular el promedio
    promedio = sum(temperaturas) / len(temperaturas)

    # Encontrar el vañor máximo y mínimo
    maximo = max(temperaturas)
    minimo = min(temperaturas)

    # Calcular la desviacion estándar
    # Primero, calcular la varianza (la suma dde las diferenciaas al cuadrado entre cada
    # valor y promedi, dividida por el número de elementos).
    sum_diferencias_cuadrado = sum([(temp - promedio) ** 2 for temp in temperaturas])
    varianza = sum_diferencias_cuadrado / len(temperaturas)

    # Luego, la desviación estándar es la raíz cuadrada de la varianza.
    desviacion_estandar = math.sqrt(varianza)

    # Mostrar los resultados en pantalla 
    print("\n--- Resultados del Análisis de temperaturas ---")
    print(f"Temperaturas ingresadas: {temperaturas}")
    print(f"promedio: {promedio:.2f} °C")
    print(f"Valor máximo: {maximo} °C")
    print(f"Valor Mínimo: {minimo} °C")
    print(f"Desviación Estándar: {desviacion_estandar:.2f} °C")
else:
    print("No se ingresaron temperaturaas.")
