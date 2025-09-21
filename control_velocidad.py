import time

def monitorear_velocidad(velocidad_actual_rpm):
    """
    Evalua la velocidad actual y muestra un mensaje o alerta.

    Args:
         celocidad_actual_rpm (float): La velocidad actual del motor en RPM.
    """
    # Rangos de velocidad del motor (pueden ser modificados)
    VELOCIDAD_MINIMA_RPM = 1000
    VELOCIDAD_MAXIMA_RPM = 1500

    print(f"velocidad actual: {velocidad_actual_rpm} RPM")

    if velocidad_actual_rpm < VELOCIDAD_MINIMA_RPM:
        print("¡ALERTA! La velocidad es demaciado baja. Se recomienda aumentar la velocidad.")
    elif velocidad_actual_rpm > VELOCIDAD_MAXIMA_RPM:
        print("¡ALERTA¡ La velocidad es demasiado alta. se recomiendo reducir la velocidad.")
    else:
        print("La velocidad esta dentro del rango operativo. Estado: OK.")

    print("-" * 30) # separador para una mejor visualizacion

# Bucle principal que simula el monitoreo en tiempo real
print("--- Monitoreo de Velocidad de la Banda Transportadora ---")
print("presione Ctrl+C para detener el monitoreo.")

while True:
    try:
        # Simula la lectura del sensor
        velocidad_ingresada = float(input("Ingrese la velocidad del motor en RPM: "))
        monitorear_velocidad(velocidad_ingresada)

        # Espera 1 segundo antes de la siguiente lectura (simula "tiempo real")
        time.sleep(1)

    except ValueError:
        print("Entrada no valida. Por favor, ingrese un numero.")
    except KeyboardInterrupt:
        print("\nMonitoreo detenido.")
        break        
        