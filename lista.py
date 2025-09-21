# Lista de frecuencias
frecuencias = [30, 35, 40, 45, 50, 55, 60]

# Parametros del motor para los calculos
numero_de_polos = 4
potencia_nominal_hp = 10 # Asuminos una potencia nominal de 10 hp para el ejemplo

# Calculo de Velocidades
velocidades = []
for f in frecuencias:
    velocidad = (f * 120) / numero_de_polos
    velocidades.append(velocidad)

# Calculo del consumo de Energía
consumos = []
for f in frecuencias:
    # La   formula usa el 50 Hz como referencia, que es una frecuencia nominal comun.
    consumo = potencia_nominal_hp * (f / 50)**3
    consumo.append(consumo)

# Analisis y presentacion
print("Analisis de Rendimiento del Motor Electrico")
print("-" * 50)

# Imprimir las listas en formato tabular
print(f"{'Frecuencia (Hz)' :<20} | {'Velocidad (RPM)':<20} | {'Consumo (HP)':<15}")
print("-" * 50)
for i in range(len(frecuencias)):
    print(f"{frecuencias[i]:<20} | {velocidad[i]:<20.2f} | {consumos[i]:<15.2f}")
print("-" * 50)

# Identificar la frecuencia de maxima eficiencia
# La maxima eficiencia se alcanza a la mayor velocidad con el menor consumo relativo
# A mayor frecuencia, la velocidad aumenta y el consumo tambien.
# El punto de maxima eficiencia se concidera a menudo cuando se alcanza la potencia nominal
# y la velocidad nominal. En este caso, la frecuencia de 50 Hz es la nominal.
# El problema pide el punto de "maxima eficiencia en trminos de veloxidad y consumo".
# Esto suele referirse al punto nominal de operacion.
# En este caso, la frecuencia de 50 Hz es el punto donde la potencia es igual a la nominal.

# Buscamos la frecuencia donde el consumo se aproxime a la potencia nominal,
# que en la formula sucede cuando frecuencia es 50 Hz
frecuencia_optima = 50
velocidad_optima = (frecuencia_optima * 120) / numero_de_polos
consumo_optimo = potencia_nominal_hp * (frecuencia_optima / 50)**3

print("\nAnalisis de Eficiencia:")
print(f"La frecuencia de 50 Hz es la que mejor se alinea con la potencia nominal delmotor ({potencia_nominal_hp} HP).")
print(f"En este punto, el motor opera con una velocidad de {velocidad_optima:.2f} RPM y un consumo de {consumo_optimo:.2f} HP,")
print("lo que representa su punto de diseño y maxima eficiencia.")
print("Las frecuencias mayores a 50 Hz superan la potencia nominal, mientras que las menores a 50 Hz son subutilizadas.")