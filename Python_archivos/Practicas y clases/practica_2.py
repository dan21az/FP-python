goleadores =["cifuente", "orejuela"]
tuit = input("Ingrese un mensaje de Twitter: ")

def contar_votos(mensaje,jugadores):
    if "#goleador" in mensaje: #Verificamos que #goleador se encuentre en el mensaje
        partes = mensaje.lower().split(" ") 
        i = partes.index("#goleador") 
        if i+1 < len(partes): #Buscamos que exista una palabra despues de #goleador
            nombre = partes[i+1]
            if nombre in jugadores: #Ya que asumimos que el nombre va despues del #goleador y este existe, buscamos que se encuentra en la lista de goleadores
                mensaje_final = f"Su voto por el goleador {nombre.upper()} es un voto válido."
            else:
                mensaje_final= "Su voto no es un voto válido."
        else:
            mensaje_final = "Su voto no es un voto válido."
    else:
        mensaje_final = "Su voto no es un voto válido."
    return mensaje_final     
print(contar_votos(tuit,goleadores))