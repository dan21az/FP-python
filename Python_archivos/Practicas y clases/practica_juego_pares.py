import random as rd
tablero = rd.choices(range(10,21),k=20)
print("Bienvenido al juego Encuentra los Pares\n")
turnos = 1
par_encontrado = 0
while turnos <= 6 and par_encontrado < 3:
    print(f"Turno: {turnos}")
    casilla1 = input("Ingrese un número de casilla: ")
    casilla2 = input("Ingrese otro número de casilla: ")
    if casilla1.isdigit() and casilla2.isdigit():
            casilla1 = int(casilla1)
            casilla2 = int(casilla2)        
            if casilla1 <= 20 and casilla1 >= 1 and casilla2 <= 20 and casilla2 >= 1:
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
            else:
                print("Ingresa números válidos (Entre 1 y 20)")
    else:
        print("Ingresa números válidos (Entre 1 y 20)")
if par_encontrado == 3:
    print("Ganaste\nEncontraste 3 pares.")
else:
    print(f"Perdiste\nNO encontrastes 3 pares, solo encontrastes {par_encontrado} pares.")