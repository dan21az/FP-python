def validar(mensaje):
    while True:
        try:
            data = int(input("Ingresa "+mensaje))
            if data <= 20 and data >= 1:
                return data
            else:
                print("NO es un número válido (Entre 1 y 20).")
        except ValueError:
            print("NO es un número entero válido.")
        

import random as rd
tablero = rd.choices(range(10,21),k=20)
print(tablero)
print("\tBienvenido al juego Encuentra los Pares\nDebes ingresar dos números de casillas (entre 1 y 20) y encontrar tres pares. ")
turnos = 1
par_encontrado = 0
while turnos <= 6 and par_encontrado < 3:
    print(f"Turno: {turnos}")
    casilla1 = validar("un número de casilla: ")
    casilla2 = validar("otro número de casilla: ")
    if casilla1 == casilla2:
        print("NO ingreses los mismos números\n")
    else:
        turnos+=1
        print(f"Has encontrado las casillas {tablero[casilla1-1]} y {tablero[casilla2-1]}")
        if tablero[casilla1-1] == tablero[casilla2-1]:
            print("Has encontrado un par")
            par_encontrado += 1
        else:
            print("Las casillas NO son un par")
        print(f"Hasta ahora has encontrado {par_encontrado} pares\n")

if par_encontrado == 3:
    print(f"Ganaste\nEncontraste 3 pares en {turnos-1} turnos.")
else:
    print(f"Perdiste\nNO encontrastes 3 pares, solo encontrastes {par_encontrado} pares en {turnos-1} turnos.")