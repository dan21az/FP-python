# def determinar_pais (lista_paises, universidades_por_pais, universidad):
#     for i in range(len(lista_paises)):
#         if universidad in universidades_por_pais[i]:
#             return lista_paises[i]
#     return " "


# def crear_lista_estudiantes(lista_paises, universidades_por_pais, datos, pais):
#     estudiantes = []
#     if pais in lista_paises:
#         n = lista_paises.index(pais)
#         universidades_pais = universidades_por_pais[n]
#         for registro in datos:
#             nombre, uni = registro.split(",")
#             if uni in universidades_pais:
#                 estudiantes.append(nombre)
#     return estudiantes

# def posibles_buddies (lista_estudiantes1, lista_estudiantes2):
#     combinaciones = []
#     for elem1 in lista_estudiantes1:
#         for elem2 in lista_estudiantes2:
#             combinaciones.append(f"{elem1}-{elem2}")
#     return combinaciones

# ######################################################################################
# #               Ejercicio 1
# ######################################################################################
# paises=['USA', 'Japan', 'United Kingdom','Ecuador']
# universidades=[['Harvard University','University of Pennsylvania'],['University of Tokyo','Kyoto University'],['University of Cambridge','University of Oxford'],['ESPOL']]
# registros=["Ashitaka,University of Tokyo","Carlitos,ESPOL","Setsuko,University of Tokyo","Donald,University of Pennsylvania","Fulano,ESPOL","Sosuke,Kyoto University"]

# estudiantes=crear_lista_estudiantes(paises, universidades, registros, 'Japan')
# print(estudiantes)

# ######################################################################################
# #               Ejercicio 2
# ######################################################################################
# lista =["www.espol.edu.ec","www.google.com","www.sri.gob.ec","www.fiec.espol.edu.ec","www.uess.edu.ec","www.FIEC.espol.edu.ec","www.fict.espol.edu.ec","www.fcnm.Espol.edu.ec","www.ucsg.edu.ec","www.Stanford.edu","www.harvard.edu","www.stanford.edu","www.UCSG.edu.ec","www.google.com.ec","www.facebook.com","www.opensource.org","www.educacionbc.edu.mx" ]

# universidades = []
# n = 0
# for url in lista:
#     url = url.upper().split(".")
#     if "EDU" in url:
#         if len(url) == 3 or len(url) == 4:
#             if url[1] not in universidades:
#                 universidades.append(url[1])
#                 n = n+1
#                 print(f"{n}.) {url[1]}")
#         elif len(url) == 5:
#             if url[2] not in universidades:
#                 universidades.append(url[2])
#                 n = n+1
#                 print(f"{n}.) {url[2]}")

lista = ["Facto N°",1,"Ricardo vale v",True]
print(lista)

