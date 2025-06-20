import random

def simular_busqueda(num_cuevas=13, pos_ladron=6):
    pol1 = 0  # Policía que va de 0 a derecha
    pol2 = num_cuevas - 1  # Policía que va de 12 a izquierda
    dia = 0

    print(f"Día {dia}: Ladrón en {pos_ladron}, Policía1 en {pol1}, Policía2 en {pol2}")

    while True:
        # Verificar si alguno atrapa al ladrón
        if pos_ladron == pol1 or pos_ladron == pol2:
            print(f"🚓 Ladrón atrapado en el día {dia} en la cueva {pos_ladron}")
            break

        # Mover policías
        pol1 = min(pol1 + 1, num_cuevas - 1)
        pol2 = max(pol2 - 1, 0)

        # Mover al ladrón: puede ir -1, 0, o +1 dentro del rango
        movimiento = random.choice([-1, 0, 1])
        nueva_pos = pos_ladron + movimiento
        if 0 <= nueva_pos < num_cuevas:
            pos_ladron = nueva_pos

        dia += 1
        print(f"Día {dia}: Ladrón en {pos_ladron}, Policía1 en {pol1}, Policía2 en {pol2}")

simular_busqueda()
