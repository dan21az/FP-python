import pandas as pd

frutas =["aguacate","cereza","ciruela","fresa","kiwi","limon","mandarina","manzana","melon"]
tipo=["verde","roja","otra","otra","verde","verde","otra", "roja","otra"]
energias = [134,58,45,34,53,39,39,41,37]
agua = [79,82,84,88,83,87,86,85,88]
hidratos = [1.3,14.5,11.0,7.0,14.5,9.0,14.5,10.5,8.4]
fibras = [2.4,1.5,2.1,2.2,1.5,1.0,1.9,2.3,0.8]
grasas = [13.8,0.5,0.15,0.5,0.44,0.3,0.19,0.2,20.28]
proteinas= [1.3,0.8,0.6,0.7,1.0,0.7,0.8,0.3,0.9]

frutas = pd.Series(["aguacate", "cereza", "ciruela", "fresa", "kiwi", "limon", "mandarina", "manzana", "melon"])
tipo = pd.Series(["verde", "roja", "otra", "otra", "verde", "verde", "otra", "roja", "otra"])
energias = pd.Series( [134,  58,   45,   34,  53,   39,  39,   41,   37])
fibras = pd.Series(   [2.4,  1.5,  2.1,  2.2, 1.5,  1.0, 1.9,  2.3,  0.8])
hidratos = pd.Series( [1.3,  14.5, 11.0, 7.0, 14.5, 9.0, 14.5, 10.5, 8.4])
agua = pd.Series(     [79,   82,   84,   88,  83,   87,  86,   85,   88])
grasas = pd.Series(   [13.8, 0.5,  0.15, 0.5, 0.44, 0.3, 0.19, 0.2,  20.28])
proteinas = pd.Series([1.3,  0.8,  0.6,  0.7, 1.0,  0.7, 0.8,  0.3,  0.9])

# 1. ¿Cuál es el número de fibras de la fruta que tiene mayor hidratos?
print(1)
mask = hidratos.argmax()
fruta_mayor = frutas[mask]
fibras_mayor = fibras[mask]
frutas_fibras = pd.Series([fibras_mayor], index=[fruta_mayor])
print(frutas_fibras)

# 2. ¿Cuál es el número de fibras de la fruta que tiene mayor hidratos (*asuma son 
# varios → mostrar todos)? 
print(2)
mask = hidratos.max() == hidratos
frutas_mask = frutas[mask]
fibras_mask = fibras[mask]
fibras_frutas = pd.Series(list(fibras_mask), index=frutas_mask)
print(fibras_frutas)

# 3. ¿Qué frutas tienen porcentaje de agua mayor al promedio? 
print(3)
mask = agua > agua.mean()
frutas_mask = frutas[mask]
agua_mask = list(agua[mask])
frutas_agua = pd.Series(agua_mask,index=frutas_mask)
print(frutas_agua)


# 4. ¿Cuál es la energía de la fruta verde con mayor grasa?
print(4)
mask_verdes = tipo == "verde"
energia_verdes = energias[mask_verdes]
frutas_verdes = frutas[mask_verdes]
mask_energia = energia_verdes.max() == energia_verdes
energia_max = list(energia_verdes[mask_energia])
frutas_max = frutas_verdes[mask_energia]
frutas_energia = pd.Series(energia_max, index=frutas_max)
print(frutas_energia)

# 5. ¿Cuáles son las 3 frutas con menos grasa? 
print(5)
top3low_grasas = list(grasas.sort_values()[0:3])
top3low_frutas = frutas[grasas.argsort()[0:3]]
top3low_frutas_grasas = pd.Series(top3low_grasas, index=top3low_frutas)
print(top3low_frutas_grasas)

# 6. ¿Qué tipo de fruta tiene el promedio de proteína más alto? (en los ejemplos tiene 
# tipos "verde", "roja", "otra", pero podrían variar)
print(6)
tipos_unicos = tipo.unique()
promedios = pd.Series([])
for i in list(tipos_unicos):
    mask_tipo = tipo == i
    promedio = proteinas[mask_tipo].mean()
    promedios[i] = promedio
print(promedios)

print("Holap world--:D xddddddddd")



