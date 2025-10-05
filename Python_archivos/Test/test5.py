# Lista de temperaturas registradas
temp = [23, -45, 60, 15, 70, -55, 10, 25, 30, -10, 5, 40, 55, 58, -49, -51, 0, 35, 20, 18,
        61, 59, -60, -30, -20, 45, 50, 52, -48, 33, 22, -52, 17, 19, 21, -25, 12, 11, 29, 27]

# Lista vacía para almacenar las temperaturas válidas
temp_validas = []

# Agregar temperaturas válidas: mayores a -50 y menores a 60, hasta tener 30
for t in temp:
    if -50 < t < 60:
        temp_validas.append(t)
    if len(temp_validas) == 30:
        break

# Calcular el promedio de las temperaturas válidas
promedio = sum(temp_validas) / len(temp_validas)

# Calcular variaciones absolutas entre días consecutivos
variaciones = []
for i in range(1, len(temp_validas)):
    variacion = abs(temp_validas[i] - temp_validas[i - 1])
    variaciones.append(variacion)

# Identificar el día con el cambio más brusco de temperatura
indice_mayor_variacion = variaciones.index(max(variaciones))
dia_mayor_cambio = indice_mayor_variacion + 2  # +2 porque variaciones empieza desde el día 2

# Contador para los días con temperatura mayor a 45 °C
dias_calurosos = 0

# Contar días con temperatura mayor a 45 °C
for t in temp_validas:
    if t > 45:
        dias_calurosos += 1

# Imprimir resultados
print(f"Promedio de temperaturas válidas: {promedio:.2f} °C")
print(f"Día con el cambio de temperatura más brusco: Día {dia_mayor_cambio}")
print(f"Número de días con temperatura mayor a 45°C: {dias_calurosos}")
