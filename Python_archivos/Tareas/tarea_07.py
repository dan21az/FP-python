
################################################################
#                         Funciones                            #
################################################################
####  TEMA1  ####
def nota(calificacion):
    if calificacion >= 90:
        return "A"
    elif calificacion >= 80:
        return "B"
    elif calificacion >= 70:
        return "C"
    elif calificacion >= 60:
        return "D"
    else:
        return "F"
    

####  TEMA4  ####
def cambiar_extension(nombre,extension = "txt"):
    nombre = nombre.split(".")
    nuevo_nombre = f"{'.'.join(nombre[:-1])}.{extension}"
    return nuevo_nombre


################################################################
#                            MAIN                              #
################################################################
####  TEMA2  ####
num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))
print("Operaciones Aritméticas\n\t1 Sumar\n\t2 Dividir")
operador = input("Seleccione una opción (ingrese número 1 - 2): ")
resultado = None

if operador == "1" and operador == "2":
    operador = int(operador)
    if operador == 1:
        resultado = num1 + num2
        print(f"El resultado es {resultado}")
    else:
        if num2 == 0:
            print("No se puede divir para cero")
        else:
            resultado = num1 / num2
            print(f"El resultado es {resultado}")
else:
    print("Opción no válida")


####  TEMA3  ####
email = input("Ingrese un correo")
password = input("Ingrese la contraseña")
usuario = email.split("@")[0]
if len(password) >=8:
    seguridad = "tiene 8 o más caracteres"
else:
    seguridad = "tiene menos de 8 caracteres"
print(f"Nombre de Usuario: {usuario}\nSu contraseña {seguridad}")
