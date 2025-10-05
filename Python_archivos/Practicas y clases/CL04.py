#Nombre: Daniel Anzules
# Lista de temperaturas registradas
temp = [43, 46, 68, 42, 47, 48, 40, 39, 38, 35]

# Lista vacía para almacenar temperaturas válidas
temp_validas = []

# Contador de temperaturas válidas
contador_validas = 0

# Recorremos la lista de temperaturas
for temperatura in temp:
    # Verificamos si la temperatura está en el rango válido y no hemos alcanzado el límite
    if -50 < temperatura < 60 and contador_validas < 30:
        temp_validas.append(temperatura)
        contador_validas += 1
    # Si ya tenemos 30 datos, salimos del bucle
    if contador_validas >= 30:
        break

# Calculamos el promedio de temperaturas válidas
if temp_validas:  # Verificamos que la lista no esté vacía
    promedio = sum(temp_validas) / len(temp_validas)
else:
    promedio = 0  # Valor por defecto si no hay temperaturas válidas

# Calculamos las variaciones de temperatura entre días consecutivos
variaciones = []
for i in range(1, len(temp_validas)):
    diferencia = abs(temp_validas[i] - temp_validas[i-1])
    variaciones.append(diferencia)

# Identificamos el día con mayor variación
if variaciones:  # Solo si hay variaciones calculadas
    indice_max_variacion = variaciones.index(max(variaciones))
    # Sumamos 1 porque las variaciones comienzan desde el segundo día
    dia_max_variacion = indice_max_variacion + 1
    valor_max_variacion = variaciones[indice_max_variacion]
else:
    dia_max_variacion = 0
    valor_max_variacion = 0.0

# Contador de días calurosos (temperatura > 28°C)
dias_calurosos = 0
for temperatura in temp_validas:
    if temperatura > 28:
        dias_calurosos += 1

# Contador de temperaturas extremadamente altas (>45°C)
contador_extremo_calor = 0
for temperatura in temp_validas:
    if temperatura > 45:
        contador_extremo_calor += 1

# Mostramos los resultados
print("\n" + "="*50)
print("RESULTADOS DEL ANÁLISIS DE TEMPERATURAS")
print("="*50)
print(f"Promedio de temperaturas válidas: {promedio:.2f}°C")
print(f"Día con cambio más brusco: Día {dia_max_variacion} (Variación: {valor_max_variacion:.2f}°C)")
print(f"Días calurosos (>28°C): {dias_calurosos}")
print(f"Días con temperatura extrema (>45°C): {contador_extremo_calor}")
print("="*50 + "\n")