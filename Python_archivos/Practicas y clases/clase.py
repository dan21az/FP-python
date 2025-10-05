import pandas as pd
frutas =["aguacate","cereza","ciruela","fresa","kiwi","limon","mandarina","manzana","melon"]
tipo=["verde","roja","otra","otra","verde","verde","otra", "roja","otra"]
energias = [134,58,45,34,53,39,39,41,37]
agua = [79,82,84,88,83,87,86,85,88]
hidratos = [1.3,14.5,11.0,7.0,14.5,9.0,14.5,10.5,8.4]
fibras = [2.4,1.5,2.1,2.2,1.5,1.0,1.9,2.3,0.8]
grasas = [13.8,0.5,0.15,0.5,0.44,0.3,0.19,0.2,20.28]
proteinas= [1.3,0.8,0.6,0.7,1.0,0.7,0.8,0.3,0.9]

frutas = pd.Series(frutas)
tipo = pd.Series(tipo)
energias = pd.Series(energias)
agua = pd.Series(agua)
hidratos = pd.Series(hidratos)
fibras = pd.Series(fibras)
grasas= pd.Series(grasas)
proteinas = pd.Series(proteinas)

# 1. ¿Cuál es el número de fibras de la fruta que tiene mayor hidratos?
i_max_hidrato = hidratos.argmax()
fibra_max_hidrato = fibras[i_max_hidrato]
fruta_max_hidrato = frutas[i_max_hidrato]
print(f"{fruta_max_hidrato} tiene la mayor cantidad de hidratos y su números de fibras es:{fibra_max_hidrato }")

# 2. ¿Cuál es el número de fibras de la fruta que tiene mayor hidratos (*asuma son
# varios → mostrar todos)?
max_hidrato = hidratos.max()
ind_max_hidratos = hidratos == max_hidrato
frutas_max = frutas[ind_max_hidratos]
fibras_max = list(fibras[ind_max_hidratos])
frutas_fibras_max = pd.Series(fibras_max, index=frutas_max)
print(frutas_fibras_max)

# 3. ¿Qué frutas tienen porcentaje de agua mayor al promedio?
mask_agua = agua > agua.mean()
frutas_agua = frutas[mask_agua]
print(frutas_agua)

# 4. ¿Cuál es la energía de la fruta verde con mayor grasa?
frutas_verdes = tipo == "verde"
grasas_verde = grasas[frutas_verdes]
energia_verde = energias[frutas_verdes]
frut_verde = frutas[frutas_verdes]
max_grasa_verde = grasas_verde.argmax()
max_energia_verde = energia_verde[max_grasa_verde]
max_fruta_verde= frutas[max_grasa_verde]
print(max_fruta_verde, energia_verde)


# 5. ¿Cuáles son las 3 frutas con menos grasa?
grasas_ordenadas = grasas.sort_values()
menores_grasas = grasas_ordenadas[0:3]
print(frutas[grasas.argsort()][0:3])


# 6. ¿Qué tipo de fruta tiene el promedio de proteína más alto? (en los ejemplos tiene
# tipos "verde", "roja", "otra", pero podrían variar)


