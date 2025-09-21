import time

def mostrar_estado_y_alertas(nivel_actual, capacidad_total, nivel_objetivo):
    """
    Funcion que evalua el nivel del tanque y muestra alertas.
    """
    # Definimos los niveles de alerta en porcentaje
    NIVEL_MUY_BAJO = 10
    NIVEL_BAJO = 25
    NIVEL_ALTO = 75
    NIVEL_MUY_ALTO = 90

    # Convertimos el nivel actual a porcentaje
    porcentaje_nivel = (nivel_actual / capacidad_total) * 100

    print(f"Nivel actual del tanque: {nivel_actual:.2f} /{capacidad_total} ({porcentaje_nivel:.2f}%)")

    if porcentaje_nivel <= NIVEL_MUY_BAJO:
        print("ALERTA: Nivel muy bajo. ¡El tanque esta casi vacido!")
    elif porcentaje_nivel <= NIVEL_BAJO:
        print("ALERTA: Nivel Bajo. Llenado en curso...")
    elif porcentaje_nivel >= NIVEL_MUY_ALTO:
        print("ALETA: Nivel Muy Alto. El llenado esta a punto de completarse.")
    elif porcentaje_nivel >= NIVEL_ALTO:
        print("ALRTA: Nivel Alto. Se aproxima al nivel objetivo.")
    else:
        print("Estado de la bomba: APAGADA")

    print("-" * 30) # Separador par mejorar la lectura

#--- Configuracion inicial del sistema ---
capacidad_tanque = 100 # Litros o unidad de medida
nivel_inicial= 20
nivel_objetivo = 85

# --- Bucle de llenado ---
nivel_actual = nivel_inicial
print(f"Iniciando llenado del tanque desde {nivel_inicial} hasta {nivel_objetivo}...")
print("Presione Ctrl+C para detener el proceso")

try:
    while nivel_actual < nivel_objetivo:
        # Simula el aumento del nivel del tanque 
        incremento = 1.5 # simula el flujo de la bomba
        nivel_actual += incremento

        # Limita el nivel para no exeder la capacidad total
        if nivel_actual > capacidad_tanque:
            nivel_actual = capacidad_tanque

        mostrar_estado_y_alertas(nivel_actual, capacidad_tanque, nivel_objetivo)
        time.sleep(0.5) # pausa de 0.5 segundos para simular el tiempo real
    print("\nProceso de llenado finalizado. Nivel objetivo alcanzado.")

except KeyboardInterrupt:
    print("\nProceso de llenado intrrrumpido por el usuario.")
      
