"""
1)  Dada una línea de texto:
Imprima: De qué ciudad es y cuál es su promedio
"""
texto1="ANDREA,estudiante001,Guayaquil,50,54,60"
texto2="PAULINA,estudiante002,Guayaquil,70,74,0"
texto3="OMAR,estudiante003,Milagro,75,70,0"
texto4="ALEX,estudiante004,Portoviejo,60,50,65"
texto5="EMILY,estudiante005,Portoviejo,75,84,85"
texto6="ALEJANDRO,estudiante006,Duran,70,72,0"
texto7="JOSE,estudiante007,Guayaquil,50,54,0"
texto8="AMY,estudiante008,Milagro,70,70,0"
texto9="OSWALDO,estudiante009,Guayaquil,50,54,60"
texto10="KAREN,estudiante010,Portoviejo,35,64,0"
texto11="MICHAEL,estudiante011,Guayaquil,70,75,0"
texto12="MICHELLE,estudiante012,Guayaquil,60,60,0"
texto13="LUIS,estudiante013,Milagro,65,60,70"
texto14="BRYAN,estudiante014,Portoviejo,80,74,80"

#En su codigo solo utilice la variable texto, para probar con otra linea, cambie texto = texto1 por la linea que quiere probar. Por ejemplo texto = texto8
texto = texto14

ciudad = texto[texto.index(",")+15:texto.index(",", texto.index(",")+15)]
nota1 = float(texto[texto.index(",", texto.index(",")+15)+1 : texto.index(",", texto.index(",")+15)+3])
nota2 = float(texto[texto.index(",", texto.index(",")+15)+4 : texto.index(",", texto.index(",")+15)+6])
nota3 = float(texto[texto.index(",", texto.index(",")+15)+7:])
promedio = (nota1 + nota2 + nota3) / 3
print(f"Ciudad: {ciudad}, Promedio: {promedio}")

"""
2) Escriba un programa que solicite al usuario ingresar un texto y que cuente el número de artículos en dicho texto. Los artículos que debe contar son los siguientes: "un", "uno", "una", "la", "lo"
"""
texto_1 = input("Ingrese un texto: ")
num_un = texto_1.count(" un ") + texto_1.count("Un ") + texto_1.count(" UN ") + texto_1.count("UN ")
num_uno = texto_1.count(" uno ") + texto_1.count("Uno ") + texto_1.count(" UNO ") + texto_1.count("UNO ")
num_una = texto_1.count(" una ") + texto_1.count("Una ") + texto_1.count(" UNA ") + texto_1.count("UNA ")
num_la = texto_1.count(" la ") + texto_1.count("La ") + texto_1.count(" LA ") + texto_1.count("LA ")
num_lo = texto_1.count(" lo ") + texto_1.count("Lo ") + texto_1.count(" LO ")
print(f"El cantidad de los siguiente artículos en el texto es: \nun: {num_un} \nuno: {num_uno} \nuna: {num_una} \nla: {num_la} \nlo: {num_lo}")
