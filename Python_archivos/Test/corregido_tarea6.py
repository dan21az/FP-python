
#Ultimo ejercicio
def obtener_datos(inscritos, resultados, id):
  i = int(id)
  inscritos = inscritos[i-1]
  resultados = int(resultados.index(id))+1
  return inscritos, resultados

inscritos= ['Usain Bolt', 'Jefferson Perez',  'Glenda Morejón',  'Martha Tenorio' ]
resultados=['0003','0001', '0004','0002']
consulta=input("ingrese id: ")

nombre,lugar=obtener_datos(inscritos, resultados, consulta)
print(f"El corredor con id: {consulta} es '{nombre}' y llegó en lugar: {lugar}")
