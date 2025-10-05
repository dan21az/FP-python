def cambiar_extension(nombre,extension="txt"):
    nombre = nombre.split(".")
    nuevo_nombre = f"{'.'.join(nombre[:-1])}.{extension}"
    return nuevo_nombre

nom1 = "datos.2.1.jpg"
nom2 = "xls"
print(cambiar_extension(nom1,nom2))