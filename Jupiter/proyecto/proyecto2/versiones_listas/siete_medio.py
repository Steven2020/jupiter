import random

def mensaje_inicio():
	print("     _                 _            _             ")
	print(" ___(_)_ __ ___  _   _| | __ _  ___(_) ___  _ __  ")
	print("/ __| | '_ ` _ \| | | | |/ _` |/ __| |/ _ \| '_ \ ")
	print("\__ \ | | | | | | |_| | | (_| | (__| | (_) | | | |")
	print("|___/_|_| |_| |_|\__,_|_|\__,_|\___|_|\___/|_| |_|")
	print("               JUEGO SIETE Y MEDIO")                                  

def mezclar_baraja():
    baraja = [1, 2, 3, 4, 5, 6, 7, "sota", "caballo", "rey"] * 4 #baraja de 40 cartas
    random.shuffle(baraja)
    return baraja

def imprimir_cartas(cartas):
    print ([str(carta) if carta != 1 else "1" for carta in cartas ])

def valor_carta(carta):
    if carta in ["sota", "caballo", "rey"]:
        return 0.5
    else:
        return carta

def valor_mano(lista):
    if lista == []:
        return 0
    else:
        return valor_carta(lista[0]) + valor_mano(lista[1:])

def obtener_puntaje(cartas):
    return valor_mano(cartas)

# Funciones para jugar los turnos
def jugar_turno_jugador(cartas):
    print ("Sus cartas son:")
    imprimir_cartas(cartas[0])
    print ("Las cartas del repartidor son:")
    imprimir_cartas(cartas[1])
    if obtener_puntaje(cartas[0]) < 7.5 and bool(input("Si quiere pedir mas cartas ingrese 1. De lo contrario presione enter: ")):
        return jugar_turno_jugador([cartas[0] + [cartas[2][0]]] + [cartas[1]] + [cartas[2][1:]])
    else:
        return cartas

def jugar_turno_repartidor(cartas):
    if obtener_puntaje(cartas[1]) < 7 and (obtener_puntaje(cartas[1]) < obtener_puntaje(cartas[0]) and obtener_puntaje(cartas[0]) <=7.5):
        return jugar_turno_repartidor([cartas[0]] + [cartas[1] + [cartas[2][0]]] + [cartas[2][1:]])            
    else:
        return cartas

# Funcion para imprimir el resultado del juego segun puntajes
def imprimir_resultado(puntaje_jugador, puntaje_repartidor):
    print ("Puntaje jugador: " + str(puntaje_jugador) + ". Puntaje repartidor: " + str(puntaje_repartidor))
    if puntaje_jugador > 7.5 and puntaje_jugador > puntaje_repartidor:
        print ("Jugador PIERDE el juego.")
    elif puntaje_jugador == 7.5 and (puntaje_repartidor > 7.5 or puntaje_repartidor < 7.5):
        print ("Jugador GANA el juego.")
    elif puntaje_jugador == 7.5 and puntaje_repartidor == 7.5:
        print ("Igualados, el Jugador PIERDE el juego.")
    elif puntaje_jugador < 7.5 and (puntaje_repartidor > 7.5 or puntaje_repartidor < puntaje_jugador):
        print ("Jugador GANA el juego.")
    elif puntaje_jugador < 7.5 and puntaje_repartidor > puntaje_jugador:
        print ("Jugador PIERDE el juego.")
    elif (puntaje_jugador > 7.5 and puntaje_repartidor >7.5) and puntaje_jugador < puntaje_repartidor :
        print ("el jugador estuvo mas cerca")
    else:
        print ("Igualados, el Jugador PIERDE el juego...")    

# Funcion que guia el desarrollo del juego
def juego(cartas, turnoJugadorHecho, turnoRepartidorHecho):
    
    if cartas[2] == []:
        print ("\nPreparando la baraja...")
        juego(cartas[0:2] + [mezclar_baraja()], turnoJugadorHecho, turnoRepartidorHecho)
    elif cartas[0] == []:
        print ("\nRepartiendo cartas al jugador...")
        juego([cartas[2][0:1]] + [cartas[1]] + [cartas[2][2:]], turnoJugadorHecho, turnoRepartidorHecho)
    elif cartas[1] == []:
        print ("\nColocando carta del repartidor...")
        juego([cartas[2][0:1]] + [cartas[0]] + [cartas[2][1:]], turnoJugadorHecho, turnoRepartidorHecho)
    elif not turnoJugadorHecho:
        print ("\n** COMIENZO TURNO JUGADOR:\n")
        juego(jugar_turno_jugador(cartas), True, turnoRepartidorHecho)
    elif not turnoRepartidorHecho:
        print ("\n** COMIENZO TURNO REPARTIDOR...\n")
        juego(jugar_turno_repartidor(cartas), turnoJugadorHecho, True)        
    else:
        print ("Las cartas finales del repartidor son:")
        imprimir_cartas(cartas[1])
        print ("\n** RESULTADO DEL JUEGO:\n")        
        imprimir_resultado(obtener_puntaje(cartas[0]), obtener_puntaje(cartas[1]))        

# Funcion de inicio
def jugar_siete():
    mensaje_inicio()
    juego([[], [], []], False, False)
    print ("\nJUEGO TERMINADO.")

# Iniciar juego
jugar_siete()
