"""
TEMA1
Solicitar nombre y promedio de la parte práctica y teórica  (ambas sobre 100) de FP y mostrar el promedio final.
"""
nombre = input("Ingrese su nombre: ")
prom_practico = float(input("Ingrese su promedio de la parte práctica sobre 100 de FP: "))
prom_teorico = float(input("Ingrese su promedio de la parte teórica sobre 100 de FP: "))
prom_final = (prom_practico * 0.3 ) + (prom_teorico * 0.7)
print(prom_final)


"""
TEMA2
  Solicite la temperatura en grados centígrados y muestre su valor en grados Fahrenheit.
"""
temp_centigrados = float(input("Ingrese la temperatura en grados centígrados: "))
temp_fahrenheit = (temp_centigrados * (9/5)) + 32 
print(temp_fahrenheit)


"""
TEMA3
Solicite peso y altura e imprima el Indice de Masa Corporal (IMC = peso [kg]/ estatura al cuadrado [m2]).
"""
peso = float(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(imc)
