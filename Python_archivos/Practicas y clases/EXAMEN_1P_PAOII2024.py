# def buscar_clave(datos,clave):
#     clave = clave.upper()
#     lista_datos = datos.split(" ")
#     for indice,dato in enumerate(lista_datos):
#         if dato == clave:
#             valor = int(lista_datos[indice+1])
#             break
#         else:
#             valor = -1
#     return valor

# mensaje = buscar_clave("ALT 60 DIST 110 PRESION 2 TEMP 33 PAS 4", "ALT")
# print(mensaje)




# l_vehiculos = ['GKL-4522|Camioneta|Azul|123487 KM',
# 'GKX-3522|Bus|Blanco|183513KM',
# 'GKA-1512|Camioneta|Negra|48455 KM']

# placa_input = "GKX-6522"

# if "-" in placa_input:
#     placa1 = placa_input.split("-")
#     comprobacion = placa1[0].isalpha() and placa1[0].isupper() and len(placa1[0]) == 3 and placa1[1].isdigit() and len(placa1[1]) == 4
#     if comprobacion == True:
#         for placa in l_vehiculos:
#             placa2 = placa.split("|")
#             if placa2[0] == placa_input:
#                 valor = f"{placa2[1]}, {placa2[2]}, {placa2[3]}"
#                 break
#             else:
#                 valor = "[-] Placa No Registrada"
#         print(valor)
#     else:
#         print("[-] Formato incorrecto")
# else:
#     print("[-] Formato incorrecto")

import random as rd

print("Juego MEMORIA\n=============")
lista_numeros = rd.choices(range(101,109),k=25)
turnos = 0
pares = 0
for i in range(5):
    if pares == 3:
        print(f"Ganaste! Descubriste {pares} pares")
        break
    else:
        print(f"Turno: {turnos+1} \t Pares Descubiertos: {pares}")
        indice1 = int(input("Ingrese un primer indice: "))
        indice2 = int(input("ingrese un segundo indice: "))
        if lista_numeros[indice1] == lista_numeros[indice2]:
            turnos+=1
            pares+=1
            print(f"\tNúmeros destapados: {lista_numeros[indice1]} y {lista_numeros[indice2]}\n\tNuevo par descubierto! ")
        else:
            turnos+=1
            print(f"\tNúmeros destapados: {lista_numeros[indice1]} y {lista_numeros[indice2]}\n\tNo hay par! ")

if turnos == 5:
    print(f"Perdiste! Solo lograste descubrir {pares} pares")