temperaturas = [23.5, 24.0, 22.8, 25.1, 26.3, 24.9, 23.0, 22.5, 24.4, 25.0,
                23.7, 24.2, 23.9, 22.1, 24.8, 25.3, 26.1, 23.6, 24.5, 25.7,
                23.3, 22.7, 24.6, 25.2, 26.0, 24.3, 23.4, 22.9, 25.5, 24.7]

contador = 0
temperaturas_validas = []

while contador < 30:
    dato = temperaturas[contador]
    if -50 <= dato <= 60:
        temperaturas_validas.append(dato)
    contador += 1

promedio = sum(temperaturas_validas) / len(temperaturas_validas)

dias_muy_calidos = 0
for temp in temperaturas_validas:
    if temp > 45:
        dias_muy_calidos += 1

record_variacion = 0
record_indice = None
diferencias = []

for i in range(1, len(temperaturas)):
    actual = temperaturas[i]
    anterior_valida = temperaturas_validas[i - 1]
    diferencia = actual - anterior_valida
    if diferencia < 0:
        diferencia = -diferencia
    diferencias.append(diferencia)
    
    if diferencia > record_variacion:
        record_variacion = diferencia
        record_indice = i

print(f"Promedio de temperaturas válidas: {promedio:.2f}")
print(f"Día de cambio más brusco (índice): {record_indice}")
print(f"Número de días con temperatura mayor a 45°C: {dias_muy_calidos}")
