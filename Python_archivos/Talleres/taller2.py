'''
Integrantes:
1.- Daniel Anzules
2.- Adriel Celi
3.- 
4.-
'''

###########################################################
#                         Funciones                       #
###########################################################

#### 1
def mostrar_biblioteca_completa(ids,songs,artists,years,genres,durations):
    contador = 0
    for indice,id in enumerate(ids):
        contador = contador + 1
        mensaje = f"{contador}: [{id}] {songs[indice]} - {artists[indice]} ({years[indice]}), {genres[indice]}, {durations[indice]} segundos"
        print(mensaje)

#### 3
def filtrar_decada(ids,years,consulta="80s"):
    consulta1 = int(consulta[-3])
    canciones_ids = []
    for indice,year in enumerate(years):
        if str(consulta1) == str(year)[2]:
            canciones_ids.append(ids[indice])
    return canciones_ids

#### 4
def contar_canciones_genero(genres):
    return None

#### 5
def cancion_larga(durations):
    maximo = max(durations)
    indice = durations.index(maximo)
    return indice




################################################################
#                            MAIN                              #
################################################################
ids=['0KL','5FK','XO2','UI1','JZE','9US','095','4C4','3W0','NA3','C7C','S8B','G6B','X1V','1K8','DYQ','YUF','10A','KK7','MCB','7BC','0GU','YHS','5O1','5JL','KEC','KS3','30X','OJH','4W3','XWR','YCX','PQH','GAB','5FP','6VA','MFW','7LQ','DCK','1H7','BM5','KOB','G7O','889','C8Z','73P','7QJ','D3T','PD6','VD4']
songs= ["Bohemian Rhapsody","Imagine","Hotel California","Stairway to Heaven","Like a Rolling Stone","Smells Like Teen Spirit","Radio ga ga","Hey Jude","Sweet Child o' Mine","Thriller","Respect","What a Wonderful World","Purple Rain","Let It Be","London Calling","Good Vibrations","Comfortably Numb","No Woman,No Cry","Every Breath You Take","One","Back in Black","Sweet Home Alabama","Heroes","Beat It","One Dance","Shape of You","Rolling in the Deep","Uptown Funk","Blinding Lights","Shake It Off","Despacito","Bad Guy","Hotline Bling","Shallow","All Star","Crazy in Love","Lose Yourself","Hallelujah","Wonderwall","Livin' on a Prayer","I Will Always Love You","Mr. Brightside","Someone Like You","Poker Face","Royals","Take On Me","Sweet Dreams (Are Made of This)","Gangsta's Paradise","Creep","In the End"]
artists = ["Queen","John Lennon","Eagles","Led Zeppelin","Bob Dylan","Nirvana","Queen","The Beatles","Guns N' Roses","Michael Jackson","Aretha Franklin","Louis Armstrong","Prince","The Beatles","The Clash","The Beach Boys","Pink Floyd","Bob Marley","The Police","Metallica","AC/DC","Lynyrd Skynyrd","David Bowie","Michael Jackson","Drake","Ed Sheeran","Adele","Mark Ronson ft. Bruno Mars","The Weeknd","Taylor Swift","Luis Fonsi ft. Daddy Yankee","Billie Eilish","Drake","Lady Gaga & Bradley Cooper","Smash Mouth","Beyoncé","Eminem","Leonard Cohen","Oasis","Bon Jovi","Whitney Houston","The Killers","Adele","Lady Gaga","Lorde","a-ha","Eurythmics","Coolio ft. L.V.","Radiohead","Linkin Park"]
years = [1975,1971,1976,1971,1965,1991,1984,1968,1987,1982,1967,1967,1984,1970,1979,1966,1979,1975,1983,1989,1980,1974,1977,1982,2016,2017,2010,2014,2019,2014,2017,2019,2015,2018,1999,2003,2002,1984,1995,1986,1992,2003,2011,2008,2013,1985,1983,1995,1992,2001]
genres = ["Rock","Pop","Rock","Rock","Folk rock","Grunge","Pop","Rock","Hard rock","Pop","Soul","Jazz","Pop","Rock","Punk rock","Pop","Progressive rock","Reggae","Rock","Metal","Hard rock","Southern rock","Art rock","Pop","Dancehall","Pop","Soul","Funk","Synthpop","Pop","Reggaeton","Alternative pop","R&B","Pop rock","Alternative rock","Pop","Hip hop","Folk","Britpop","Rock","R&B","Alternative rock","Soul","Pop","Electropop","Pop","Synthpop","Hip hop","Alternative rock","Metal"]
durations = [354,183,391,482,369,301,354,431,356,420,149,141,248,243,199,216,384,256,252,447,255,283,233,258,173,233,228,270,200,219,282,194,267,215,201,235,326,283,258,249,273,221,285,221,208,225,249,241,238,216]

mostrar_biblioteca_completa(ids,songs,artists,years,genres,durations)

consulta = input("Ingrese una década específica (70s, 80s, 90s, etc.)")
mensaje = filtrar_decada(ids,years,consulta)
print(mensaje)

print(cancion_larga(durations))