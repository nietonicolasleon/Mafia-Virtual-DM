import os
jugadores = []
roles = ["Policía", "Mafia", "Médico", "Civil"]
muerto = ""

roleplayers = {}

cant_jugadores = int(input("Ingrese la cantidad de jugadores que participarán: "))

while cant_jugadores < 4:
    print("Recomendamos que hayan al menos cuatro jugadores en la partida.")
    cambiar_num = int(input("¿Quiere cambiar la cantidad de jugadores?: 0 - NO / 1 - SI: "))
    if cambiar_num == 1:
        cant_jugadores = int(input("Ingrese la cantidad de jugadores que participarán: "))
    else:
        print("Se asumirá que la cantidad de jugadores son 4 para cumplir el cupo mínimo de jugadores.")
        input("Presione ENTER para continuar: ")
        cant_jugadores = 4

os.system('cls')

for num in range(0, cant_jugadores):
    actual_num = str(num+1)
    jugador = input(f"Ingrese el nombre del participante n° " + actual_num + ": ")
    jugadores.append(jugador)

for j in jugadores:
    numRol = int(input(f"QUE ROL ES " + j + ": "))
    roleplayers[j] = roles[numRol]
    input(f"USTED " + j + " ELIGIÓ: " + roles[numRol] + ". PRESIONE ENTER: ")
    os.system('cls')

pol_respuesta = int(input("Policía, a quién desea investigar: "))

mafia = roleplayers[jugadores[pol_respuesta]] == "Mafia"

if mafia:
    print("SÍ, ES MAFIA")
else:
    print("NO, NO ES MAFIA")
    
input(f"POLICÍA PRESIONE ENTER: ")
    
os.system('cls')

mafia_respuesta = int(input("Mafia, a quién desea matar: "))
muerto = jugadores[mafia_respuesta]

input(f"MAFIA, ELIGIÓ A: " + muerto + " PRESIONE ENTER: ")

os.system('cls')

medico_respuesta = int(input("Médico, a quién desea salvar: "))
if muerto == jugadores[medico_respuesta]:
    muerto = "NADIE MURIÓ"
    
input(f"MÉDICO, ELIGIÓ A: " + jugadores[medico_respuesta] + " PRESIONE ENTER: ")

os.system('cls')

if muerto == "NADIE MURIO":
    print(muerto)
else:
    print(f"La mafia mató a: " + muerto)
