import random

cuevas = 13
posicion_ladron = random.randrange(0, cuevas - 1)
posicion_policia1 = 0
posicion_policia2 = cuevas - 1
buscar_ladron = True
dias = 0

def mover_ladron():
    nueva_posicion = random.randrange(0, cuevas - 1)
    distancia = 0

    #Establecer posinles movimientos del ladron
    if posicion_ladron == 0:
        distancia = 1
    elif posicion_ladron == cuevas -1:
        distancia = -1
    elif nueva_posicion == posicion_ladron:
        distancia = 0
    elif nueva_posicion > posicion_ladron:
        distancia = 1
    else:
        distancia = -1
    
    #devolver la distancia que deberia recorrer el ladron
    return distancia

#Bucle implementado pára la busqueda del ladron
while buscar_ladron:
    dias += 1

    #Determinando si se encontro al ladron
    if posicion_ladron == posicion_policia1 or posicion_ladron == posicion_policia2:
        buscar_ladron = False
        break

    #Moviendo los elementos
    posicion_ladron += mover_ladron()
    posicion_policia1 += 1
    posicion_policia2 -= 1

#Indicando los dias que se tardo en encontrar al ladron
print(f"Se tardo {dias} dia(s) en encontrar al ladron")