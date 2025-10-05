# Lista de temperaturas registradas
temp = [25.5, 30.1, -5.0, 18.7, -10.2, 22.0, 17.3, -3.5, 19.8]

# Lista vacía para almacenar temperaturas válidas
temp_validas = []

# Recorrer las primeras 30 temperaturas (o menos si la lista es más corta)
for temperatura in temp[:30]:
    if -50 < temperatura < 60:
        temp_validas.append(temperatura)

# Calcular el promedio de temperaturas válidas
promedio = sum(temp_validas) / len(temp_validas) if temp_validas else 0

# Calcular variaciones entre días consecutivos
variaciones = []
for i in range(1, len(temp_validas)):
    diferencia = abs(temp_validas[i] - temp_validas[i-1])
    variaciones.append(diferencia)

# Encontrar el día con mayor variación
if variaciones:
    indice_max_variacion = variaciones.index(max(variaciones))
    dia_mayor_variacion = indice_max_variacion + 2
else:
    dia_mayor_variacion = None

# Contar días con temperatura mayor a 45°C
dias_calurosos = 0
for temperatura in temp_validas:
    if temperatura > 45:
        dias_calurosos += 1

# Mostrar resultados
print(f"Promedio de temperaturas válidas: {promedio:.2f}°C")
print(f"Día con mayor cambio de temperatura: Día {dia_mayor_variacion}")
print(f"Días con temperatura mayor a 45°C: {dias_calurosos}")