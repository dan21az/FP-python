import pandas as pd

# Crear la función aprobados(nombres, leccion, examen, tarea) que retorna los
# nombres de los estudiantes que aprueban la materia (promedio de las 3 es mayor o
# igual a 60).
nombres = pd.Series(["Juan", "Maria", "Pedro", "Sara"])
leccion = pd.Series([70, 62, 80, 40] )
examen = pd.Series([50, 52, 71, 70] )
tarea = pd.Series([0 , 75, 72, 60] )


#1
def aprobados(nombres,leccion,examen,tarea):
    aprobados = nombres[(leccion+ examen + tarea)/3 >= 60]
    # promedio = (leccion + examen + tarea)/3
    # mask = promedio >= 60
    # aprobados = nombres[mask]
    return aprobados

print(aprobados(nombres,leccion,examen,tarea))

nombres = pd.Series(["Juan", "Maria", "Pedro", "Sara"])
leccion1= pd.Series([70, 62, 80, 45] )
leccion2= pd.Series([73, 52, 71, 70] )
#2
mejorados = nombres[leccion2 > leccion1]
print(mejorados)

#3
nombres_l1 = sum(leccion1>65)
print(nombres_l1)

#4
mask = leccion2 > leccion2.mean()
aprobados = leccion2[mask]
suma = sum(aprobados)
print(suma)
