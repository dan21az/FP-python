def calcular_imc (nombres,pesos,alturas):
    imc_resultado = []
    for i in nombres:
        imc_resultado.append(int((pesos[nombres.index(i)]/(alturas[nombres.index(i)]**2)*100))/100)
    return imc_resultado

names = ["Maria", "Juan", "Pedro"]
mass = [62,80,65]
altura = [1.62,1.72,1.59]

test = calcular_imc(names,mass,altura)
print(test)

isbn = input("Ingrese ISBN: ")
isbn = list(isbn.replace("-",""))
isbn_lista = []

if len(isbn) == 13:
    for i in isbn:
        isbn_lista.append(int(i))
        print(isbn_lista[:3])
    if isbn_lista[:3] == [9, 7, 8] or isbn_lista[:3] == [9, 7, 9]:
        acumulado13 = 0
        for indice13,valor13 in enumerate(isbn_lista[:12]):
            coeficiente13 = [1,3,1,3,1,3,1,3,1,3,1,3]
            acumulado13 += (coeficiente13[indice13]*valor13)
            print(acumulado13)
        comprobacion13 = 10 - (acumulado13 % 10)
        if comprobacion13 == 10:
            comprobacion13 = 0
        if comprobacion13 == isbn_lista[-1]:
            print("Correcto")
        else:
            print(f"Dígito verificador no válido, debería ser {comprobacion13}")
    else:
        print("Prefijo no válido")
elif len(isbn) == 10:
    pass
else:
    print("No es valido")