"""Nombres: Diego Apolo
            Daniel Anzules"""

datos = [
 "2025-05-14,28,3.0,Madrid,60,nublado,Se detectó humedad elevada en la zona norte.",
 "2025-05-15,30,1.2,Sevilla,45,soleado,Soleado y caluroso sin incidentes.",
 "2025-05-16,25,0.6,Granada,3,lluvioso,Lluvia débil en la mañana.",
 "2025-05-17,26,2.3,Córdoba,40,despejado,Sin precipitaciones. Buen clima.",
 "2025-05-19,25,1.0,Valencia,15,ventoso,Clima cambiante con viento moderado.",
 "2025-05-20,29,1.1,Zaragoza,25,lluvioso,Error al registrar datos del sensor.",
 "2025-05-18,27,0.0,Málaga,70,nublado,Monitoreo estable.",
 "2025-05-21,31,2.5,Bilbao,50,soleado,Condiciones normales para la fecha.",
 "2025-05-22,33,1.3,Murcia,8,lluvioso,Error: batería baja en estación.",
 "2025-05-23,24,1.0,Salamanca,12,nublado,Todo normal, sin anomalías."
]

# CÓDIGO ENTREGADO POR COMPAÑEROS:

#dias_sin_lluvia, contador_indice, reportes_validos = 0
#condiciones = ["nublado", "lluvioso", "soleado", "despejado"]
#ciudades, promedio = []
#dias_mas_calurosos, i = 0
#while dias_sin_lluvia == 0 and len(datos):
#    i += 1
#    linea.split(",")
#    if linea[5] in condiciones:

# CÓDIGO NUESTRO CORREGIDO:
dias_sin_lluvia, reportes_validos, i, temp_caluroso = 0, 0, 0, 0
condiciones = ["nublado", "lluvioso", "soleado", "despejado"]
ciudades, promedios = [], []
i = 0
condicion_dia_caluroso = None

while dias_sin_lluvia == 0 and i < len(datos):
    linea = datos[i].split(",")
    if linea[5] in condiciones and "error" not in linea[6].lower() and float(linea[4]) > 5:
        promedios.append(float(linea[4]))
        reportes_validos += 1
        if linea[3] not in ciudades:
            ciudades.append(linea[3])
        if float(linea[2]) == 0.0:
            dias_sin_lluvia += 1
        if float(linea[1]) > temp_caluroso:
            temp_caluroso = float(linea[1])
            condicion_dia_caluroso = linea[5]
    i += 1

promedio = sum(promedios) / len(promedios) if promedios else 0
ciudades1 = f"{ciudades[0]} y {ciudades[1]}" if len(ciudades) == 2 else f"{(", ").join(ciudades[:-1])} y {ciudades[-1]}" if len(ciudades) > 0 else "Ninguna"

print(f"Reportes válidos: {reportes_validos}\nCiudades: {ciudades1}\nPromedio de temperatura: {promedio:.2f}\nCondición del día más caluroso: {condicion_dia_caluroso}")