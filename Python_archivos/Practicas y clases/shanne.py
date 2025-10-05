estudiantes = [
 "DIANA,estudiante025,Loja,66,64,67,21,3,9,Ingeniería Ambiental,diana@ejemplo.com,2002-02-28,F,activa,merito,SI",
 "GABRIEL,estudiante024,Milagro,48,52,60,22,5,6,Psicología,gabriel@ejemplo.com,2001-06-06,M,activa,ninguna,NO",
 "ESTEFANY,estudiante027,Ambato,59,62,65,19,2,12,Economía,estefany@ejemplo.com,2004-04-17,F,activa,merito,SI",
 "LUIS,estudiante005,Quito,55,50,58,23,4,9,Ingeniería Eléctrica,luis@ejemplo.com,2000-10-30,M,activa,economica,NO",
 "NATALIA,estudiante013,Ambato,67,65,66,21,3,7,Enfermería,natalia@ejemplo.com,2002-01-01,F,activa,merito,SI",
 "ISABEL,estudiante011,Loja,88,90,0,19,0,14,Biología,isabel@ejemplo.com,2004-03-17,F,activa,merito,SI",
 "MARIO,estudiante012,Quito,52,49,60,20,5,6,Ingeniería Ambiental,mario@ejemplo.com,2003-02-14,M,activa,economica,NO",
 "SEBASTIAN,estudiante030,Guayaquil,53,57,60,21,4,8,Ingeniería en Sistemas,sebastian@ejemplo.com,2002-05-07,M,activa,economica,NO",
 "OMAR,estudiante003,Milagro,75,70,0,19,2,12,Arquitectura,omar@ejemplo.com,2004-07-15,M,activa,economica,SI",
 "SOFIA,estudiante023,Guayaquil,77,79,0,18,0,14,Ingeniería Mecánica,sofia@ejemplo.com,2005-08-15,F,activa,merito,SI",
 "KARLA,estudiante007,Cuenca,40,45,65,22,7,3,Psicología,karla@ejemplo.com,2002-09-12,F,activa,ninguna,NO",
 "PEDRO,estudiante014,Cuenca,75,80,0,18,0,13,Economía,pedro@ejemplo.com,2005-06-30,M,activa,ninguna,SI",
 "MELISSA,estudiante017,Milagro,55,58,62,23,7,5,Ingeniería en Sistemas,melissa@ejemplo.com,2000-12-24,F,activa,merito,NO",
 "JUAN,estudiante008,Portoviejo,78,80,0,20,2,11,Administración de Empresas,juan@ejemplo.com,2003-06-08,M,activa,economica,SI",
 "RAUL,estudiante028,Cuenca,42,45,55,24,6,4,Ingeniería Eléctrica,raul@ejemplo.com,1999-08-29,M,activa,ninguna,NO",
 "DAVID,estudiante016,Guayaquil,45,50,59,20,4,10,Contabilidad,david@ejemplo.com,2003-10-19,M,activa,ninguna,SI",
 "FABIOLA,estudiante021,Cuenca,90,92,0,19,0,16,Ingeniería Industrial,fabiola@ejemplo.com,2004-01-03,F,activa,merito,SI",
 "DANIEL,estudiante004,Loja,65,68,70,21,6,5,Ingeniería Mecánica,daniel@ejemplo.com,2002-05-11,M,activa,ninguna,NO",
 "RUBEN,estudiante020,Ambato,35,40,50,20,9,2,Ingeniería Civil,ruben@ejemplo.com,2003-07-27,M,activa,ninguna,NO",
 "CARLOS,estudiante018,Loja,88,86,0,21,1,12,Arquitectura,carlos@ejemplo.com,2002-04-13,M,activa,economica,SI",
 "JULIA,estudiante015,Portoviejo,60,65,70,22,6,9,Psicología,julia@ejemplo.com,2002-09-05,F,activa,economica,SI",
 "ANITA,estudiante019,Quito,62,60,64,22,2,11,Medicina,anita@ejemplo.com,2002-11-11,F,activa,merito,SI",
 "VERÓNICA,estudiante029,Portoviejo,81,83,0,20,0,13,Biología,veronica@ejemplo.com,2003-12-31,F,activa,merito,SI",
 "PAULINA,estudiante002,Guayaquil,70,74,0,22,1,8,Ingeniería Civil,paulina@ejemplo.com,2001-12-20,F,activa,merito,SI",
 "MIGUEL,estudiante022,Portoviejo,70,68,75,20,3,7,Derecho,miguel@ejemplo.com,2003-03-20,M,activa,economica,NO",
 "KEVIN,estudiante026,Quito,74,70,72,23,2,10,Contabilidad,kevin@ejemplo.com,2000-09-09,M,activa,economica,SI",
 "ANDREA,estudiante001,Guayaquil,50,54,60,20,3,10,Ingeniería en Sistemas,andrea@ejemplo.com,2003-04-10,F,activa,ninguna,SI",
 "FERNANDO,estudiante010,Milagro,60,50,55,24,8,4,Derecho,fernando@ejemplo.com,1999-11-22,M,activa,ninguna,NO",
 "LINA,estudiante009,Guayaquil,68,70,0,21,1,10,Ingeniería Industrial,lina@ejemplo.com,2002-08-09,F,activa,merito,NO",
 "MARÍA,estudiante006,Ambato,90,88,0,18,0,15,Medicina,maria@ejemplo.com,2005-01-25,F,activa,merito,SI" ]

def diccionario_nombres(estudiantes):
    diccionario_nombres = {}

    for linea in estudiantes:
        linea = linea.split(",")
        nombre = linea[0]
        id = linea[1]
        diccionario_nombres[id] = nombre

    for id,estudiantes in diccionario_nombres.items():
        print(f"{id}: {estudiantes}")

diccionario_nombres(estudiantes)


def diccionario_promedios(estudiantes):
    diccionario_promedios = {}

    for linea in estudiantes:
        linea = linea.split(",")
        notas = sum(sorted(list(map(float,linea[3:6])), reverse=True)[0:2])/2
        id = linea[0]
        diccionario_promedios[id] = notas

    for id,promedio in diccionario_promedios.items():
        print(f"{id}: {promedio}")

diccionario_promedios(estudiantes)

def diccionario_carreras(estudiantes):
    diccionario_carreras = {}
    for linea in estudiantes:
        linea = linea.split(",")
        carrera = linea[9]
        if carrera not in diccionario_carreras:
            diccionario_carreras[carrera] = 1
        else:
            diccionario_carreras[carrera] += 1
    total = sum(diccionario_carreras.values())

    for carrera, contador in diccionario_carreras.items():
        print(f"{carrera}: {contador}")
    print(f"En total hay {total} estudiantes.")

diccionario_carreras(estudiantes)

def diccionario_ciudad(estudiantes):
    diccionario_ciudad = {}
    for linea in estudiantes:
        linea = linea.split(",")
        ciudad = linea[2]
        edad = linea[6]
        if ciudad not in diccionario_ciudad:
            diccionario_ciudad[ciudad] = [int(edad)]
        else:
            temp = diccionario_ciudad[ciudad] 
            temp.append(int(edad))
            diccionario_ciudad[ciudad] = temp
    for ciudad, edades in diccionario_ciudad.items():
        print(f"En {ciudad} hay personas con edades de: {", ".join(map(str,edades[:-1]))} y {edades[-1]}")

diccionario_ciudad(estudiantes)