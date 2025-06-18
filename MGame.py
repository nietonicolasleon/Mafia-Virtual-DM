import os
jugadores = ["Fran", "Elena", "Elias", "Noche"]
roles = ["policía", "mafia", "médico", "civil"]
muerto = ""

roleplayers = {}

for j in jugadores:
    numRol = int(input(f"QUE ROL ES " + j + ": "))
    roleplayers[j] = roles[numRol]
    input(f"USTED " + j + " ELIGIÓ: " + roles[numRol] + ". PRESIONE ENTER: ")
    os.system('cls')

pol_respuesta = int(input("Policía, a quién desea investigar: "))

mafia = roleplayers[jugadores[pol_respuesta]] == "mafia"

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
