####################################################
#                      TEMA 1                      #
####################################################

dominios = ["net", "com", "org", "edu", "gob", "mil", "info", "int"]
url = input("Ingrese la dirección web: ").lower().split(".")
comprobacion_longitud = len(url) == 3
comprobacion_inicio = url[0] == "www"
comprobacion_organizacion = url[1] != ""
comprobacion_dominio = url[2] in dominios
comprobacion_final = comprobacion_longitud and comprobacion_inicio and comprobacion_organizacion and comprobacion_dominio
print("La dirección web es válida:", comprobacion_final)

####################################################
#                      TEMA 2                      #
####################################################

import random
nombres = ["Juan","Pedro","Maria","Stefany","Daniel", "Jose", "Santiago", "Paola"]
nombre_aleatorio = random.choices(nombres,k=2)
comprobacion = nombre_aleatorio[0] == nombre_aleatorio[1]
print(f"{nombre_aleatorio[0]} es igual a {nombre_aleatorio[1]}: {comprobacion}")
num = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14 , 15]
print(random.sample(num[0:11], 4))
print(random.choices(num[0:6], k=10))