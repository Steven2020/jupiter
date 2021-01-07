import random

def mensaje_inicio():
	print("     _                 _            _             ")
	print(" ___(_)_ __ ___  _   _| | __ _  ___(_) ___  _ __  ")
	print("/ __| | '_ ` _ \| | | | |/ _` |/ __| |/ _ \| '_ \ ")
	print("\__ \ | | | | | | |_| | | (_| | (__| | (_) | | | |")
	print("|___/_|_| |_| |_|\__,_|_|\__,_|\___|_|\___/|_| |_|")
	print("               JUEGO SIETE Y MEDIO                ")
	print()                           

cont = 0 #Almacena las veces que gana la casa
cont1 = 0 #Almacena las veces que gana el jugador
simulaciones = 100 #Aqui se coloca el numero de simulaciones a ejecutar

#Funcion que baraja las cartas
def mezclar_baraja():
    baraja = [1, 2, 3, 4, 5, 6, 7, "sota", "caballo", "rey"] * 4 #baraja de 40 cartas
    random.shuffle(baraja)
    return baraja

#Funcion que transforma las cartas con figuras en medio punto
def valor_carta(carta):
    if carta in ["sota", "caballo", "rey"]:
        return 0.5
    else:
        return carta

#Esta funcion suma el valor de las cartas en la mano
def valor_mano(lista):
    if lista == []:
        return 0
    else:
        return valor_carta(lista[0]) + valor_mano(lista[1:])

#Funcion para obtener los puntajes
def obtener_puntaje(cartas):
    return valor_mano(cartas)

#Funcion para que la casa realize estrategia del medio punto
def estrategia_medio_punto(cartas):
    return valor_mano(cartas)+0.5

#Funcion para los turnos del jugador
def turno_jugador(cartas):
    if obtener_puntaje(cartas[0]) <= 5.5:
        return turno_jugador([cartas[0] + [cartas[2][0]]] + [cartas[1]] + [cartas[2][1:]])
    else:
        return cartas

#Funcion para los turnos de la casa
def turno_casa(cartas):
    if obtener_puntaje(cartas[1]) <= 5.5 and obtener_puntaje(cartas[0]) <= 7.5:
        return turno_casa([cartas[0]] + [cartas[1] + [cartas[2][0]]] + [cartas[2][1:]])            
    else:
        return cartas

#Funcion que decide quien gana
def resultado(puntaje_jugador, puntaje_casa):
    if puntaje_jugador > 7.5 and puntaje_casa <= 7.5:
        gana = 0
    elif puntaje_jugador == 7.5 and (puntaje_casa > 7.5 or puntaje_casa < 7.5):
        gana = 1
    elif puntaje_jugador <= 7.5 and puntaje_casa <= 7.5 and puntaje_jugador == puntaje_casa:
        gana = 0
    elif puntaje_jugador < 7.5 and (puntaje_casa > 7.5 or puntaje_casa < puntaje_jugador):
        gana = 1
    elif puntaje_jugador < 7.5 and puntaje_casa > puntaje_jugador:
        gana = 0
    return gana

#Funcion que guia el desarrollo del juego
def juego(cartas, turnoJugadorHecho, turnoCasaHecho):
    global gana
    if cartas[2] == []:
        juego(cartas[0:2] + [mezclar_baraja()], turnoJugadorHecho, turnoCasaHecho)
    elif cartas[0] == []:
        juego([cartas[2][0:1]] + [cartas[1]] + [cartas[2][2:]], turnoJugadorHecho, turnoCasaHecho)
    elif cartas[1] == []:
        juego([cartas[2][0:1]] + [cartas[0]] + [cartas[2][1:]], turnoJugadorHecho, turnoCasaHecho)
    elif not turnoJugadorHecho:
        juego(turno_jugador(cartas), True, turnoCasaHecho)
    elif not turnoCasaHecho:
        juego(turno_casa(cartas), turnoJugadorHecho, True)        
    else:       
        gana = resultado(obtener_puntaje(cartas[0]), obtener_puntaje(cartas[1]))
    return gana

mensaje_inicio()

for i in range(0,simulaciones):
	b = juego([[], [], []], False, False)
	if b == 0:
		cont += 1
	elif b == 1:
		cont1 += 1
		
print("Jugando",simulaciones,"partidas se obtiene:")
print("----------------------------------------")
print("casa gano:   ",cont,"veces")
print("jugador gano:",cont1,"veces")
print("----------------------------------------")


