################################################################
#                         Funciones                            #
################################################################
def dia_correspondiente(numero):
  dias_semana = ["lunes", "martes", "miercoles","jueves","viernes","sabado","domingo"]
  dia = dias_semana[numero-1]
  return dia

def reparar(texto):
  return texto[::-1].lower().replace("."," ")

def verificar_web (url, dominios):
  url = url.lower().split(".")
  comprobacion_longitud = len(url) == 3
  comprobacion_inicio = url[0] == "www"
  comprobacion_organizacion = url[1] != ""
  comprobacion_dominio = url[2] in dominios
  comprobacion_final = comprobacion_longitud and comprobacion_inicio and comprobacion_organizacion and comprobacion_dominio
  mensaje_final= f"{'.'.join(url)}\nretorna: {comprobacion_final}"
  return mensaje_final

def obtener_datos(inscritos, resultados, id):
  id = int(id)-1
  inscritos = inscritos[id]
  resultados = int(resultados[id])
  return inscritos, resultados


################################################################
#                            MAIN                              #
################################################################
print(f"1 corresponde a {dia_correspondiente(1)}")
print(f"2 corresponde a {dia_correspondiente(2)}")
print(f"3 corresponde a {dia_correspondiente(3)}")
print(f"4 corresponde a {dia_correspondiente(4)}")

print("\n")
frase = "OsOiCiLaM.aMaRgOrP.nU.rOp.OdAcAtA.rEs.eD.sEtNa.AtIrCsE.eSaRf.AnU.sE.aTsE" 
reparada=reparar(frase)
print(f'La frase: \n\t"{frase}"\nha sido reparada. El resultado es:\n\t"{reparada}"')

print("\n")
print(verificar_web("www.organizacion.net.edu", ["net", "com", "org" ]) )
print(verificar_web("www.organizacion.net.net", ["net", "com", "org" ]) )
print(verificar_web("www.organizacion.net", ["net", "com", "org" ]) )
print(verificar_web("www.organizacion.net", [ "com", "org" ]) )

print("\n") #ta mal, corregir
inscritos= ['Usain Bolt', 'Jefferson Perez',  'Glenda Morejón',  'Martha Tenorio' ]
resultados=['0003','0001', '0004','0002']
consulta=input("ingrese id: ")
nombre,lugar=obtener_datos(inscritos, resultados, consulta)
print(f"El corredor con id: '{consulta}' es '{nombre}' y llego en lugar: {lugar}")

print("\n")
nombre,lugar=obtener_datos(['A','B','C','D'], ['0003','0001','0004','0002'], '0003')
print(f"El corredor con id: '0003' es '{nombre}' y llegó en lugar: {lugar}")
