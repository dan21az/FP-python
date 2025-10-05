import random as rd

'''
Defina la función ingresa_n_nombres(n) que pide el ingreso de n nombres y retorna una lista con los nombres en forma alfabética. Si no se define la cantidad de nombres a pedir, la función pide 3 nombres por defecto.
'''
def ingresa_n_nombres(n=3):
  lista_nombres=[] #Se crea una lista vacia en donde se almacenaran todos los nombres ingresados
  #Se debe pedir ingreso de nombres un numero de veces conocido (n), por lo que se puede utilizar un lazo de repeticion fija (inicio: 0, fin: n-1)
  for i in range(n):
    nombre=input(f"Ingrese nombre: ") #Se solicita ingreso de nombre
    lista_nombres.append(nombre) #Se agrega el nombre ingresado a la lista que almacena todos los nombres
  lista_nombres.sort() #Se ordena la lista en forma alfabetica antes de retornarla
  return lista_nombres #Se retorna la lista

'''
Defina la función contar_palabras(texto, lista_palabras_buscadas) que recibe una frase (solo palabras sin signos de puntuación) junto a una lista de palabras y retorna el número total de palabras de la lista que tiene la frase. 
'''
def contar_palabras(texto, lista_palabras_buscadas):
  lista_texto=texto.lower().split() #Se convierte la frase a minusculas y luego se la separa tomando los espacios en blanco como referencia (espacio en blanco es el valor por defecto de split), obteniendo una lista de palabras
#OJO: primero se hace minuscula la frase y luego se la transforma a lista. A la inversa ( frase.split().lower() )se produciria un error ya que se estaria tratando de cambiar a minuscula una lista y no un str
  acumulador=0 #Se inicializa la variable que va a ir sumando el numero de palabras buscadas
  #Se va a contar cuantas veces aparece cada palabra buscadas, como sabemos cuantas palabras son las que vamos a contar (estan en una lista) se puede realizar un lazo fijo
  for palabra in lista_palabras_buscadas:
    acumulador+=lista_texto.count(palabra.lower())
  return acumulador #retornamos el valor total de palabras buscadas


'''
Defina la función filtrar_palabras_menores(lista_palabras, n) que recibe una lista de palabras y un número n. La función retorna una nueva lista de palabras que solamente contiene las palabras con longitud menor a n. El valor por defecto de n es 6.
'''
def filtrar_palabras_menores(lista_palabras, n=6):
  lista_nueva=[] #Se inicializa la nueva lista como una lista vacia
  #Se necesita recorrer la lista de palabras e ir chequeando sus valores (para saber la longitud),
  # por lo que se puede recorrer la lista por valor o por indice (pero preferiblemente por valor),
  # ademas conocemos la secuencia exacta sobre la que se va a ejecutar, por lo que se puede aplicar un lazo fijo.
  for palabra in lista_palabras:
    if len(palabra) < n:
      lista_nueva.append(palabra) #Si la palabra tiene longitud menor a n, la agrego a la nueva lista
  return lista_nueva

#
# FORMA ABREVIADA DE CREAR NUEVAS LISTAS  (Comprensión de listas)
# La creacion de una nueva lista que cumpla condiciones a partir de otra lista se la puede realizar en una sola linea combinando las instrucciones for e if
# No es necesario conocer esta forma, pero ayuda a crear programas mas rapido y eficientemente.
def filtrar_palabras_menores_ABREVIADA(lista_palabras, n=6):
  lista_nueva=[palabra for palabra in lista_palabras if len(palabra) < n ]
  return lista_nueva


'''
Defina la función numeros_azar(n,inicio,fin) que recibe 3 números enteros y retorna una lista de n números entre inicio y fin, generados aleatoriamente en donde puede haber repetidos. 
'''
def numeros_azar(n,inicio,fin):
  lista_numeros=[] # Se crea una lista vacia en donde se almacenaran todos los numeros generados aleatoriamente
  #Se debe generar numeros n veces, por lo que se puede utilizar un lazo de repeticion fija (desde 0 hasta n-1)
  for i in range(n):
    lista_numeros.append(rd.randint(inicio,fin)) #Se genera un numero aleatorio y se lo almacena en la lista
  return lista_numeros #El return debe estar fuera del lazo for

#La instruccion choices del modulo random hace lo mismo que la funcion escrita arriba,
# la funcion equivalente a la de arriba seria:
def numeros_azar2(n,inicio,fin):
  lista_numeros=rd.choices(range(inicio,fin+1), k=n)
  return lista_numeros
  

'''
Defina la función numeros_unicos_azar(n,inicio,fin) que recibe 3 números enteros y retorna una lista de n números sin repetir entre inicio y fin, generados aleatoriamente. 
'''
def numeros_unicos_azar(n,inicio,fin):
  if fin-inicio+1<n: #Si el rango entre inicio y fin es menor a la cantidad n de numeros, se disminuye n al maximo posible
    n=fin-inicio+1
  numeros = list(range(inicio, fin + 1)) # Se crea la lista de numeros a usar
  rd.shuffle(numeros)  # Para darle aletoriedad se los mezcla (baraja)
  return numeros[:n]  # Usamos slicing para tomar los primeros 'n' elementos (los cuales ya estan al azar)

#La instruccion sample del modulo random hace lo mismo que la funcion escrita arriba,
# la funcion equivalente a la de arriba seria:
def numeros_unicos_azar2(n,inicio,fin):
  if fin-inicio+1<n: #Si el rango entre inicio y fin es menor a la cantidad n de numeros, se disminuye n al maximo posible
    n=fin-inicio+1
  lista_numeros=rd.sample(range(inicio,fin+1), n)
  return lista_numeros


'''
Defina una función que dadas dos listas de números, retorne una lista que contenga los elementos que aparecen al menos una vez en ambas listas. La lista generada no debe tener números repetidos
'''
def comunes(lista1,lista2):
  lista_final = [] #Lista vacia
  for numero in lista1: #Recorro lista1: la variable numero toma el valor de cada elemento de la lista1
    if numero in lista2 and numero not in lista_final:#chequeo si el numero (de la lista1) se encuentra en la lista2 (esto para ver si son comunes) y chequeo si el numero no esta en la lista_final (esto para no repetirlo en la lista final)
      lista_final.append(numero) #agrego el numero a la lista final
  return lista_final


'''
Defina la función filtrar_palabras(lista_palabras) que dada una lista de palabras, retorne una lista con las palabras que tienen una longitud de 2 o más caracteres y que además el primer y último caracter de la palabra sean iguales. 
'''
def filtrar_palabras(lista_palabras):
  lista_final=[] #Se inicializa la nueva lista como una lista vacia
  for palabra in lista_palabras:
    if len(palabra) >= 2 and palabra[0]== palabra[-1]:#Es importante que primero se verifique longitud antes de pedir indices
      lista_final.append(palabra)
  return lista_final

  #Forma abreviada
  lista_final=[palabra for palabra in lista_palabras if len(palabra)>=2 and palabra[0]== palabra[-1] ] 


'''
Escriba la función contar_hashtags(lista_textos) que lea una lista de textos y retorne 2 listas paralelas. La primera contiene las palabras que comiencen con '#' y la segunda contiene el número de veces que aparece cada palabra.
'''
def contar_hashtags(lista_textos):
  lista_palabras=[] # Se crea una lista vacia en donde se almacenaran todas las palabras que comiencen con '#'
  lista_veces=[] # Se crea una lista vacia en donde se almacenaran el numero de veces que aparece cada palabra
  for texto in lista_textos: # Se recorre cada texto de la lista de textos
    for palabra in texto.lower().split():# A cada texto se lo transforma en una lista de palabras por medio de split, y se recorre dicha lista. En el ejemplo se guardan las palabras en minusculas por lo que aplicamos lower
      if palabra.startswith('#'): # Solo nos interesan las palabras que comienzan con #
        palabra = palabra[1:] # En el ejemplo se guardan las palabras sin el primer caracter (#), por lo que aplicamos slicing
        if palabra not in lista_palabras:  # Si es la primera vez que aparece la palabra
          lista_palabras.append(palabra) # se la agrega a la lista de palabras y
          lista_veces.append(1)          # se agrega 1 como el numero de veces que ha aparecido
        else: # Si la palabra ya ha aparecido antes, se debe buscar el indice en el cual esta guardada en la lista_palabras y el numero de veces que aparece en lista_veces en dicho indice se actualiza sumandole 1
          lista_veces[lista_palabras.index(palabra)]+=1
  return lista_palabras,lista_veces
