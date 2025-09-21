import math # Importamos el modo math para usar la funcion de raiz cuadrada

def calcular_corriente_nominal(potencia_hp, tension, eficiencia, fp):
    """
    Calcula la corriente nominal de un motor trifasico.

    Args:
        potencia_hp (float): Potencia del motor en HP.
        tension (float): Tension de la alimentacion en voltios (v).
        fp (float): Factor de potencia del motor. Por defecto 0.8.
        eficiencia (float): Eficiencia del motor. Por defecto 0.85.

    Returns:
        float: Corriente nominal en amperios       
    """
    # 1. Conversion de potencia de HP a Watts
    potencia_watts = potencia_hp * 746

    # Formula para la corriente nominal en un sistema trifasio
    # In = P_out / (sqrt(3) * V * eficiencia * fp)
    denominador = math.sqrt(3) * tension * eficiencia * fp

    # La funcion debe retornar el calculo, no  la funcion misma
    return potencia_watts / denominador

def calcular_calibre_y_caida_tension(corriente_nominal, longitud, tension) :
    """
    Calcula el calibre del conductor y la caida de tension.

    Args:
       corriente_nominal (float): Corriente nominal del motor.
       longitud (float): Longitud del conductor en metros.
       tension (float) : La tension de alimentacion en voltios.

    Returns:
           tuple: Un par de valores (calibre_recomendado, caida_tension_porcentaje).
    """
    #Tabla de ampacidad y resistencia de condutores de cobre (basada en AWG)
    tabla_conductores = {
        '14 AWG': {'amperaje': 20, 'resistencia_ohm_por_km': 8.44},
        '12 AWG': {'amperaje': 25, 'resistencia_ohm_por_km': 5.31},
        '10 AWG': {'amperaje': 35, 'resistencia_ohm_por_km': 3.34},
        '8 AWG': {'amperaje': 50, 'resistencia_ohm_por_km': 2.10},
        '6 AWG': {'amperaje': 65, 'resistencia_ohm_por_km': 1.32},
        '4 AWG': {'amperaje': 85, 'resistencia_ohm_por_km': 0.83},
        '2 AWG': {'amperaje': 115, 'resistencia_ohm_por_km': 0.52},
        '1 AWG': {'amperaje': 130, 'resistencia_ohm_por_km': 0.32},
        '1/0 AWG': {'amperaje': 150, 'resistencia_ohm_por_km': 0.26},
        '2/0 AWG': {'amperaje': 175, 'resistencia_ohm_por_km': 0.20},
        '3/0 AWG': {'amperaje': 200, 'resistencia_ohm_por_km': 0.16}
    }

    # Usamos un factor de seguridad para el calibre (125% de la corriente nominal)
    corriente_diseno = corriente_nominal * 1.25
    calibre_recomendado = "No encontrado"
    resistencia_seleccionada = 0

    # Buscamos el calibre recomendado en la tabla
    for calibre, datos in tabla_conductores.items():
        if datos['amperaje'] >= corriente_diseno:
            calibre_recomendado = calibre
            resistencia_seleccionada = datos['resistencia_ohm_por_km']
            break

    # Si no se encuentra el calibre en la tabla, se usa un valor por defecto
    if calibre_recomendado == 'No encontrado':
        return 'No encontrado', 0

    # Formula para la caida de tension en un sitema trifasico
    # %V = (2 * L * I * R_cond * sqrt(3)) / V_nominal * 100
    # La resistencia por metro es la resistencia por km dividida por 1000
    resistencia_por_metro = resistencia_seleccionada / 1000

    caida_tension_v = math.sqrt(3) * corriente_nominal * ( longitud * resistencia_por_metro)
    caida_tension_porcentaje = (caida_tension_v / tension) * 100

    return calibre_recomendado, caida_tension_porcentaje

# ---Dato principal---

EFICIENCIA = 0.8
FP = 0.8
POTENCIA_HP = 0
TENSION = 0
LONGITUD = 0

print("--- Calculadora para Motor de Banda Transportadora ---")
try:
    POTENCIA_HP = float(input("Ingrese la potencia del motor en HP: "))
    TENSION = float(input("Ingrese la tension de alimentacion en V (ej. 220):"))
    LONGITUD = float(input("Ingrese la longitud del conductor en metros: "))
except ValueError:
    print("¡Error! por favor, ingrese solo numeros. Intente de nuevo.")
    exit()

# Realizamos los calculos usando las funciones
corrite_nominal = calcular_corriente_nominal(POTENCIA_HP, TENSION, EFICIENCIA, FP)
calibre, caida_tension_porcentaje = calcular_calibre_y_caida_tension(corrite_nominal, LONGITUD, TENSION)

#--- Mostramos los resultados---
print("/n--- Resultados ---")
print(f"Corriente nominal (In): {corrite_nominal:.2f} A")
print(f"Calibre del conductor recomendado: {calibre}")
print(f"Caida de tension: {caida_tension_porcentaje:.2f}%")

# --- Damos una advertencia si la caida de tension es alta ---
if caida_tension_porcentaje > 3.0:
    print("\n¡ADVERTENCIA! La caida de tension excede el 3% recomendado.")
    print("Considere usar un calibre de conductor mayor o reducir la distancia.")
else:
    print("\nLa caida de tension esta dentro de los limites recomendados.")
    