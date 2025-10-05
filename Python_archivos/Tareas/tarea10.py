datos=[

"ANDREA,estudiante001,Guayaquil,50,54,60",
"PAULINA,estudiante002,Guayaquil,70,74,0",
"OMAR,estudiante003,Milagro,75,70,0",
"ALEX,estudiante004,Portoviejo,60,50,65",
"EMILY,estudiante005,Portoviejo,75,84,85",
"ALEJANDRO,estudiante006,Duran,70,72,0",
"JOSE,estudiante007,Guayaquil,50,54,0",
"AMY,estudiante008,Milagro,70,70,0",
"OSWALDO,estudiante009,Guayaquil,50,54,60",
"KAREN,estudiante010,Portoviejo,35,64,0",
"MICHAEL,estudiante011,Guayaquil,70,75,0",
"MICHELLE,estudiante012,Guayaquil,60,60,0",
"LUIS,estudiante013,Milagro,65,60,70",
"BRYAN,estudiante014,Portoviejo,80,74,80"
]

ciudad_promedio_alto = None
promedio_alto = 0

for linea in datos:
    partes = linea.split(",")
    ciudad = partes[2]
    notas = list(map(int,partes[3:6]))
    promedio = sum(notas)/ 3
    if promedio > promedio_alto:
        promedio_alto = promedio_alto
        ciudad_promedio_alto = ciudad
print(f"El estudiante con mayor promedio es de la ciudad de: {ciudad_promedio_alto}")

lista_ciudades = []

for linea in datos:
    partes = linea.split(",")
    ciudad = partes[2]
    if ciudad in lista_ciudades:
        pass
    else:
        lista_ciudades.append(ciudad)
ciudades = ", ".join(lista_ciudades)
print(f"Los estudiantes son de las ciudades de: {ciudades}")
