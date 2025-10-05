# Estado del jugador
jugador = {
    "vida": 100,
    "puntos": 0,
    "inventario": [],
    "cuarto_actual": "refugio_subterraneo"
}

# Diccionario de objetos
objetos = {
    "botiquin": {"cuarto": "refugio_subterraneo", "descripcion": "Recupera 20 de vida", "puntos": 0, "vida": 20},
    "traje_protector": {"cuarto": "estacion_abandonada", "descripcion": "Permite entrar al laboratorio", "puntos": 0, "vida": 0},
    "semilla": {"cuarto": "cueva_del_eco", "descripcion": "La última esperanza del planeta", "puntos": 0, "vida": 0},
    "mapa": {"cuarto": "bosque_seco", "descripcion": "Revela rutas seguras", "puntos": 10, "vida": 0}
}

# Diccionario de cuartos
cuartos = {
    "refugio_subterraneo": {
        "descripcion": "Un refugio frío y silencioso bajo tierra.",
        "norte": "desierto_rojizo",
        "efecto_vida": 0,
        "efecto_puntos": 0
    },
    "desierto_rojizo": {
        "descripcion": "Un desierto árido y peligroso.",
        "sur": "refugio_subterraneo",
        "este": "estacion_abandonada",
        "efecto_vida": 0,
        "efecto_puntos": 0
    },
    "estacion_abandonada": {
        "descripcion": "Una estación antigua, llena de chatarra útil.",
        "oeste": "desierto_rojizo",
        "este": "laboratorio_colapsado",
        "sur": "rio_contaminado",
        "efecto_vida": 0,
        "efecto_puntos": 0
    },
    "laboratorio_colapsado": {
        "descripcion": "Un laboratorio tóxico y peligroso.",
        "oeste": "estacion_abandonada",
        "efecto_vida": -30,
        "efecto_puntos": 0
    },
    "rio_contaminado": {
        "descripcion": "Un río con residuos tóxicos.",
        "norte": "estacion_abandonada",
        "sur": "templo_del_bosque",
        "efecto_vida": 0,
        "efecto_puntos": -15
    },
    "bosque_seco": {
        "descripcion": "Árboles moribundos y una brisa esperanzadora.",
        "norte": "cueva_del_eco",
        "efecto_vida": +10,
        "efecto_puntos": 0
    },
    "cueva_del_eco": {
        "descripcion": "Un lugar místico donde crece la última semilla.",
        "sur": "bosque_seco",
        "efecto_vida": 0,
        "efecto_puntos": 0
    },
    "templo_del_bosque": {
        "descripcion": "El lugar sagrado donde la semilla puede florecer.",
        "norte": "rio_contaminado",
        "efecto_vida": 0,
        "efecto_puntos": 0
    }
}

# Función para mover al jugador
def mover(direccion):
    actual = jugador["cuarto_actual"]
    if direccion in cuartos[actual]:
        siguiente = cuartos[actual][direccion]
        # Comprobar efecto del cuarto
        efecto = cuartos[siguiente]
        jugador["vida"] += efecto["efecto_vida"]
        jugador["puntos"] += efecto["efecto_puntos"]
        if siguiente == "laboratorio_colapsado" and "traje_protector" not in jugador["inventario"]:
            print("¡Entraste sin el traje! Moriste por la radiación.")
            jugador["vida"] = 0
        jugador["cuarto_actual"] = siguiente
        print(f"Te moviste a: {siguiente}")
    else:
        print("No puedes ir en esa dirección.")

# Función para recoger objetos
def recoger_objeto(nombre_objeto):
    cuarto_actual = jugador["cuarto_actual"]
    if nombre_objeto in objetos and objetos[nombre_objeto]["cuarto"] == cuarto_actual:
        jugador["inventario"].append(nombre_objeto)
        jugador["vida"] += objetos[nombre_objeto]["vida"]
        jugador["puntos"] += objetos[nombre_objeto]["puntos"]
        print(f"Has recogido {nombre_objeto}.")
        # Eliminar del mapa
        objetos[nombre_objeto]["cuarto"] = None
    else:
        print("No hay ese objeto aquí.")

# Función para mostrar estado
def mostrar_estado():
    print("\n=== ESTADO DEL JUGADOR ===")
    print(f"Vida: {jugador['vida']}")
    print(f"Puntos: {jugador['puntos']}")
    print(f"Inventario: {jugador['inventario']}")
    print(f"Ubicación: {jugador['cuarto_actual']}")
    print(cuartos[jugador['cuarto_actual']]['descripcion'])

# Condición de victoria y derrota
def revisar_condiciones():
    if jugador["vida"] <= 0:
        print("¡Has perdido toda tu vida! Game Over.")
        return True
    if jugador["cuarto_actual"] == "templo_del_bosque" and "semilla" in jugador["inventario"]:
        print("¡Plantaste la última semilla! ¡Has salvado el mundo! 🪴")
        return True
    return False

# Juego principal
def jugar():
    mostrar_estado()
    while True:
        comando = input("\n¿Qué deseas hacer? (norte/sur/este/oeste/recoger [objeto]/estado): ").lower()
        if comando in ["norte", "sur", "este", "oeste"]:
            mover(comando)
        elif comando.startswith("recoger"):
            _, obj = comando.split()
            recoger_objeto(obj)
        elif comando == "estado":
            mostrar_estado()
        else:
            print("Comando no reconocido.")
        if revisar_condiciones():
            break

# Iniciar juego
jugar()
