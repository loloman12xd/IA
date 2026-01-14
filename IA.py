import time
patrones = [".","..","...",".","..","..."]
for p in patrones:
    print(f"cargando{p}")
    time.sleep(1)
time.sleep(3)
print("LoviIA, version:1.0")
time.sleep(3)
while True:
    inicio = ("¡Como puedo ayudarte!😁😁")
    print(inicio)
    pregunta = input("").lower()

    if pregunta == "eres humano?":
        respuesta = "No, No soy humano 😊."
    elif pregunta == "cuantos años tienes?":
        respuesta = "No tengo años, Soy una IA hecha por codigo 😒."
    elif pregunta == "cual es tu nombre?":
        respuesta = "No tengo un nombre definido 🫤, Pero puedes decime:IA,LoviIA(Apodo que me escogio mi creador),O el que tu quieras 😊."
    else:
        respuesta = "Lo siento, Pero mi creador no ha creado una respuesta a tu pregunta😔, Soy una IA hecha por codigo,No por modelo etc, Pero puedes consultarle a mi creador por email para agregarlo👍.loloman12xd75352@gmail.com"

    print(respuesta)
