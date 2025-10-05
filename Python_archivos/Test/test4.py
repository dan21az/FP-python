temp = [-72, 55, -65, 12, 48, -80, 63, -15, -70, 58, -68, 25, 52, -90, 70, -5, -75, 67, -55, 30, -83, 72, -20, 49, -95, 78, -30, 45, -62, 60, -50, 15, -88, 65, -10, 53, -78, 80, -25, 42]

#Extraer las primeras 30 temperaturas en el rango valido
temp_validas = []

for dia in range(len(temp)):
    temp_dia = temp[dia]
    if dia == 29:
        break
    else:
        if temp_dia > -50 and temp_dia < 60:
            temp_validas.append(temp_dia)

#Promediar las 30 primeras temperaturas validas
promedio = sum(temp_validas)/len(temp_validas)
print(promedio)


#Calcular la variacion entre las temperaturas validos 
variacion = 0
lista_variaciones = []

for dia in range(len(temp_validas)):
    if dia == 0:
        variacion = 0
    else:
        variacion = temp_validas[dia] - temp_validas[dia-1]
        if variacion < 0:
            variacion = -1*variacion
        lista_variaciones.append(variacion)

dia_variacion = lista_variaciones.index(max(lista_variaciones))+1
print(dia_variacion)


#Contar los dias que superaron los 45 grados
dias_calurosos = 0

for temperatura in temp_validas:
    if temperatura > 45:
        dias_calurosos+=1

print(dias_calurosos)


