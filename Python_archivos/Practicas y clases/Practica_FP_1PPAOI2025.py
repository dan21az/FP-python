letras=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
valor=[1,3,3,2,1,4,2,4,1,9,5,1,3,1,1,3,10,1,1,1,1,4,4,9,4,10]



palabra = input("ingrese una palabra: ")
lista_palabras = palabra.split(",")
lista_puntos = []
puntos = 0
for palabra in lista_palabras:
    for indice, letra in enumerate(palabra):
        if letra != "*" and letra.isupper():
            posicion_letra = letras.index(letra)
            valor_letra= valor[posicion_letra]
            if palabra[indice+1]=="*":
                puntos+=valor_letra*2
            else:
                puntos+=valor_letra
    lista_puntos.append(puntos)
    puntos=0

for i in range(len(enumerate)):
    lista_palabras[i] = lista_palabras[i].replace("*","")
    