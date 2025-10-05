import random

def expedicion_mar():
    print("Bienvenido a la Expedición en el Mar")
    print("Eres un buzo que se sumergirá 5 metros para recolectar especies.")
    print("¡Cuidado con las especies letales! Si recolectas 2, perderás el juego.")
    print("Para ganar, debes sumergirte 5 metros sin recolectar 2 especies letales y recolectar al menos 2 especies buenas.\n")
    
    especies_letales = 0
    especies_buenas = 0
    metros_sumergidos = 0
    
    while metros_sumergidos < 5:
        metros_sumergidos += 1
        print(f"\nEstás a {metros_sumergidos} metro(s) de profundidad.")
        
        # Generar una especie (70% letal, 30% buena)
        es_letal = random.random() < 0.7
        tipo_especie = "letal" if es_letal else "buena"
        
        decision = input(f"Aparece una especie {tipo_especie}. ¿Deseas recolectarla? (s/n): ").lower()
        
        if decision == 's':
            if es_letal:
                especies_letales += 1
                print(f"¡Oh no! Recolectaste una especie letal. Llevas {especies_letales} especie(s) letal(es).")
            else:
                especies_buenas += 1
                print(f"¡Bien! Recolectaste una especie buena. Llevas {especies_buenas} especie(s) buena(s).")
            
            # Verificar si perdió
            if especies_letales >= 2:
                print("\n¡Has recolectado 2 especies letales! Perdiste el juego.")
                return
        
        else:
            print("Decidiste no recolectar esta especie.")
    
    # Verificar condiciones de victoria
    print("\n¡Llegaste a los 5 metros de profundidad!")
    if especies_letales < 2 and especies_buenas >= 2:
        print("¡Felicidades! Ganaste el juego:")
        print(f"- Recolectaste {especies_buenas} especies buenas (se necesitaban al menos 2)")
        print(f"- Solo recolectaste {especies_letales} especies letales (menos de 2)")
    else:
        print("Lo siento, no cumpliste con los requisitos para ganar:")
        if especies_letales >= 2:
            print("- Recolectaste 2 o más especies letales")
        if especies_buenas < 2:
            print(f"- Solo recolectaste {especies_buenas} especies buenas (se necesitaban al menos 2)")

# Iniciar el juego
expedicion_mar()