def obtener_datos(inscritos, resultados, id):
  id = int(id)-1
  inscritos = inscritos[id]
  resultados = int(resultados[id])
  return inscritos, resultados

print("\n")
inscritos= ['Usain Bolt', 'Jefferson Perez',  'Glenda Morejón',  'Martha Tenorio' ]
resultados=['0003','0001', '0004','0002']
consulta=input("ingrese id: ")
nombre,lugar=obtener_datos(inscritos, resultados, consulta)
print(f"El corredor con id: '{consulta}' es '{nombre}' y llego en lugar: {lugar}")

print("\n")
nombre,lugar=obtener_datos(['A','B','C','D'], ['0003','0001','0004','0002'], '0003')
print(f"El corredor con id: '0003' es '{nombre}' y llego en lugar: {lugar}")