"""
1) Pida una cadena de caracteres por teclado y presente por pantalla las operaciones aplicadas a la cadena de caracteres ingresada.
"""
palabra = input("Ingrese una palabra: ")
num_caracter = len(palabra)
print(f"El número total de caracteres es: {num_caracter} caracteres")
print(f"La cadena repetida conforme el número de caracteres que tiene es: {palabra * (num_caracter)}")
print(f"Los tres primeros caracteres de la cadena son: {palabra[:3]}")
print(f"Los tres últimos caracteres de la cadena son: {palabra [-3:]}")
print(f"La palabra escrita al revés es: {palabra[::-1]}")
print(f"La palabra en mayúsculas es: {palabra.upper()}")
sin_vocal_a = (palabra.lower()).replace("a","")
print(f"La palabra sin letras 'a' es: {sin_vocal_a}")
sin_vocal_e = sin_vocal_a.replace("e","")
sin_vocal_i = sin_vocal_e.replace("i","")
sin_vocal_o = sin_vocal_i.replace("o","")
sin_vocal_u = sin_vocal_o.replace("u","")
print(f"La palabra sin vocales es: {sin_vocal_u}")


"""
2) Solicite el ingreso de 2 cadenas de caracteres y combinar las 2 cadenas de caracteres para crear una nueva variable. La nueva variable debe juntar las 2 cadenas separándolas por un espacio y debe intercambiar los 2 primeros caracteres de cada una.
"""
cadena1 = input("Ingrese cadena1: ")
cadena2 = input("Ingrese cadena2: ")
inicial_1 = cadena1[0:2]
restante_1 = cadena1[2:]
inicial_2 = cadena2[0:2]
restante_2 = cadena2[2:]
final = inicial_2 + restante_1 + " " + inicial_1 + restante_2
print(f"Resultado: {final.lower()}")


"""
3) Solicite el ingreso de una palabra y muestre por pantalla, mediante un True o un False, si es la palabra es palíndroma. 
"""
cadena = (input("Ingrese cadena: "))
minuscula = cadena.lower()
inverso = minuscula[::-1]
comprobacion = minuscula == inverso 
print(f"{cadena} es palíndroma: {comprobacion}")