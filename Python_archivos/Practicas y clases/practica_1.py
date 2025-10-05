# -------- 1 -------
#  Defina una función que recibe una palabra y un sufijo. La función retorna el verbo
# infinitivo, para lo cual debe remover el sufijo de la palabra y se añadirle la letra “r” al
# final.
# Ejemplo:
# palabra 'cocinabamos', sufijo 'bamos' retorna cocinar
# palabra 'perderian' , sufijo 'rian' retorna perder

def verbo_infinitvo(palabra,sufijo):
    if sufijo in palabra:
        verbo = palabra.replace(sufijo,"r")
    else:
        verbo = "No válido"
    return verbo

palabra = "cocinabamos"
sufijo = "bamos"
print(verbo_infinitvo(palabra,sufijo))
# ----------- 2 ----------
# Implementar una función que recibe una lista de países, ciudades y una ciudad a
# buscar. La función retorna el país al que pertenece la ciudad que se busca o None si
# no existe la ciudad. Por ejemplo:
# paises= [ "Ecuador", "Colombia", ..., "Peru"]
# ciudades=[["Guayaquil","Quito",...,"Tarapoa"],["Tunja",...,"Bogota"], ..., ["Lima"] ]
# Para LIMA, se debe retornar Peru

def buscar_pais(paises, ciudades, ciudad_buscada):
    ciudad_buscada = ciudad_buscada.lower() 
    for i in range(len(ciudades)):
        for ciudad in ciudades[i]:
            if ciudad.lower() == ciudad_buscada:
                return paises[i]
    return None



paises= [ "Ecuador", "Colombia", "Peru"]
ciudades=[["Guayaquil","Quito","Tarapoa"],["Tunja","Bogota"], ["Lima"] ]

ciudad = "Bogota"

print(buscar_pais(paises,ciudades,ciudad))

# Defina una función que recibe una frase y una lista de palabras comunes (ambas en
# minúsculas). La función genera una sigla utilizando las iniciales en mayúsculas de
# cada palabra de la frase. Se debe omitir las palabras comunes definidas en la lista
# de palabras comunes, a menos que sean la primera o la última palabra de la frase.
# Asuma que en la frase no existen signos de puntuación. Ejemplo de entrada
frase = "el yin y el yang son conceptos filosóficos de la cultura china"
palabras_comunes = ["el", "y", "de", "la", "son"]
# Ejemplo de salida
"EYYCFCC " #El Yin y el Yang son Conceptos Filosóficos de la Cultura China