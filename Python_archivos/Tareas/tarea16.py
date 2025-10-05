#Ejercicio 1
ise = {"202300001":4, "202400001":8, "202400002":2, "202300002":7,
"202400003":4, "202400004":3} 
registros= { "MATG1045": ["202300001", "202400002"],
 "FISG1005": ["202400004"],
 "CCPG1043": ["202300001", "202400001", "202400002"],
 "IDIG2012": ["202400004", "202400002", "202400003"],
}

def calcular_ISE_materia (ise, registros, materia_consulta):
    matriculas = registros.get(materia_consulta,[])
    ise1 = []
    if len(matriculas) > 0 :
        for i in matriculas:
            temp = ise.get(i)
            ise1.append(temp)
        promedio = int(sum(ise1)/len(ise1))
    else:
        promedio = "Materia no encontrada"
    return promedio

print(calcular_ISE_materia(ise,registros,"MATG1045"))

#Ejercicio 2

estudiantes = ["202145678,Juan Guerra,cálculo 1|física 1|química,7.3|8.4|6.5",
"202234348,Pedro Perez,estadística|computación,8.5|7.4",
"202233021,Roberto Lara,cálculo 2|redes 1,9.0|8.9"]

def obtener_info_estudiantes(estudiantes):
    dic_info = {}
    for linea in estudiantes:
        linea = linea.split(",")
        matricula = int(linea[0])
        nombre = linea[1]
        materias = linea[2].split("|")
        promedios = list(map(float,linea[3].split("|")))
        dic_info[matricula] = [nombre,materias,promedios]
    return dic_info

def calcular_promedios(dic_info):
    dic_promedios = {}
    for matricula,datos in dic_info.items():
        calificaciones = datos[2]
        promedio = sum(calificaciones)/len(calificaciones)
        dic_promedios[matricula] = round(promedio,2)
    return dic_promedios

def obtener_mejores_promedios(dic_promedios, inicial=8.5, final=10.0):
    matriculas_promedios_mejores = []
    for matricula, promedio in dic_promedios.items():
        if promedio >= inicial and promedio <= final:
            matriculas_promedios_mejores.append(matricula)
    return matriculas_promedios_mejores

##### MAIN

rango_inicial = float(input("promedio minimo"))
rango_final = float(input("promedio maximo"))

info_estudiantes = obtener_info_estudiantes(estudiantes)
promedios_estudiantes = calcular_promedios(info_estudiantes)
mejores_matriculas = obtener_mejores_promedios(promedios_estudiantes,rango_inicial,rango_final)
if len(mejores_matriculas) > 0:
    for matricula in mejores_matriculas:
        promedio_general = promedios_estudiantes[matricula]
        lista = info_estudiantes[matricula]
        nombres = lista[0]
        print(f"Nombre: {nombres}\tPromedio General: {promedio_general}")
else:
    print("No hay estudiantes dentro del rango de promedio ingresado")
