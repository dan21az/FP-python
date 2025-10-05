

def registros_meteorologicos(datos): # Seguimos el algoritmo como una función por si existen varias listas de registros con distintos nombres
    ciudades = []
    temperaturas_validas = [] #Temperaturas de los registros válidos
    indice_validos = [] #Indice de los datos válidos de la lista de registros

    for indice, dato in enumerate(datos): 
        dato1 = dato.split(",") #Separamos cada registro de la lista para obtener los datos necesarios
        fecha = dato1[0]
        temperatura = float(dato1[1])
        lluvia = float(dato1[2])
        ciudad = dato1[3]

        if temperatura >= -20.0 and temperatura <= 40.0 and lluvia >= 0.0 and len(fecha) == 10 and fecha.count("-") == 2: #Condiciones que indica el problema
            temperaturas_validas.append(temperatura)
            indice_validos.append(indice) 
            if ciudad not in ciudades: #Comprobar que la ciudad analizada ya no se haya contado antes
                ciudades.append(ciudad)

    promedio = sum(temperaturas_validas)/len(temperaturas_validas) 
    indice_temperatura_minima = temperaturas_validas.index(min(temperaturas_validas)) #Encontramos indice del valor minimo en las temperaturas validas
    indice_en_lista_minimo = indice_validos[indice_temperatura_minima] #Buscamos el indice de la temperatura minima según la lista de registro inicial
    fecha_minima = datos[indice_en_lista_minimo].split(",")[0] #La fecha de la temepratura minima es el primer valor del registro que encontramos anteriormente
    print(f"El promedio de temperaturaas es: {promedio}°")
    print(f"La fecha con menor temperatura entre los registros válidos fue el {fecha_minima} con promedio {temperaturas_validas[indice_temperatura_minima]}")
    print(f"Las ciudades con registros válidos son: {", ".join(ciudades[:-1])} y {ciudades[-1]}")

registros = [
 "2024-05-15,28,0.1,Madrid",
 "2024-05-15,32,-1.2,Sevilla",
 "2024-05-16,25,3.4,Valencia",
 "2024-05-16,25,0.0,Valencia",
 "2024-05-17,31,0.0,Madrid",
 "2024-05-17,42,0.0,Córdoba",
 "2024-05-18,-30,0.0,Granada",
 "2024-05-18,35,0.3,Granada",
 "2024-05-19,20,0.0,Valencia",
 "2024-05-19,22,0.0,Málaga",
 "2024/05/20,23,0.1,Málaga"
]

datos = [
 "2024-05-15,28,0.1,Madrid",
 "2024-05-15,32,-1.2,Sevilla",
 "2024-05-16,25,3.4,Valencia",
 "2024-05-16,25,0.0,Valencia",
 "2024-05-17,31,0.0,Madrid",
 "2024-05-17,40,0.0,Córdoba"
]

registros_meteorologicos(registros) #Aplicamos la función con la lista de regi