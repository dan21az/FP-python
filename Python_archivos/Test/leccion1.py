#Datos del Ejercicio
datos=[
'50792,Aptenodytes forsteri,Emperor Penguin,-67.234,65.084,1997-07-24 08:20',
'50797,Thalassarche chrysostoma,Albatross Grey-headed,-60.7,-66.179,2022-12-02 12:00',
'56012,Pygoscelis adeliae,Adelie Penguin,-66.473,62.537,1996-01-13 10:30',
'53019,Pygoscelis adeliae,Adelie Penguin,-67.230,65.481,2016-08-11 11:00' ]

#Funcion que provee el ejercicio
def retornar_indices_ordenados ( lista ):
    def obtener_dato(indice):
        return lista[indice]
    indices = list(range(len(lista)))
    indices_ordenados = sorted(indices, key=obtener_dato)
    return indices_ordenados

#Del examen
# def extraer_datos (registros,especies="Adelie Penguin"):
#     id = []
#     años = []
#     coordenadas = []
#     for datos in registros:
#         lista_datos = datos.split(",")
#         fecha = lista_datos[5].split("-")
#         nombre = lista_datos[2]
#         if nombre in especies:
#             id.append(int(lista_datos[0]))
#             años.append(int (fecha[0]))
#             coordenada1 = []
#             coordenada1.append(float(lista_datos[3]))
#             coordenada1.append(float(lista_datos[4]))
#             coordenadas.append(coordenada1)
#     return id, años,coordenadas

# print(extraer_datos(datos))


#Corrección y mejor.
def extraer_datos (registros,especies="Adelie Penguin"):
    id,años, coordenadas = [], [], []
    for datos in registros:
        lista_datos = datos.split(",")
        if lista_datos[2] in especies:
            id.append(int(lista_datos[0]))
            años.append(int (lista_datos[5].split("-")[0]))
            coordenada1 = []
            coordenada1.append(float(lista_datos[3]))
            coordenada1.append(float(lista_datos[4]))
            coordenadas.append(coordenada1)
    return id, años,coordenadas

especie = input("Ingrese el nombre de una especie: ")

#Main, mostrar registros por orden alfabetico
id, años, coordenadas = extraer_datos(datos)
indices = retornar_indices_ordenados(años)

print(f"Coordenas\t\tAño")
for i in indices[::-1]:
    print(f"{coordenadas[i]}\t{años[i]}")
