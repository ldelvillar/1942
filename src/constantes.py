"""
Creado por Lucas del Villar y Javier Esteve en 2022
Universidad Carlos III de Madrid
"""

import random

# Este documento contiene constantes como sprites y listas de objetos

# Módulo de las constantes que se van a utilizar en el juego
ANCHO = 224
ALTO = 256

# SPRITES AVIONES
AVION_SPRITE = (0, 0, 0, 16, 16)
AVION_SPRITE2 = (0, 16, 0, 16, 16)
AVION_SPRITE_LOOP = (0, 130, 32, 16, 16)

# SPRITES ENEMIGOS
SPRITE_REGULAR = (0, 32, 0, 16, 16)
SPRITE_REGULAR_ARRIBA = (0, 48, 0, 16, 16)
SPRITE_ROJO = (0, 64, 0, 14, 14)
SPRITE_ROJO_DERECHA = (0, 78, 0, 14, 14)
SPRITE_ROJO_ARRIBA = (0, 92, 0, 14, 14)
SPRITE_BOMBARDERO = (0, 106, 0, 30, 30)
SPRITE_BOMBARDERO_DERECHA = (0, 136, 0, 30, 30)
SPRITE_BOMBARDERO_IZQUIERDA = (0, 166, 0, 30, 30)
SPRITE_BOMBARDERO_ARRIBA = (0, 196, 0, 30, 30)
SPRITE_SUPERBOMBARDERO = (0, 0, 32, 60, 32)

ENEMIGOS_TOTAL = []

# ENEMIGOS REGULARES
# Lista de posibles (y)es que tendrán los aviones regulares
# y contadores para evitar que se creen demasiados en la misma y.
listaRandom = [-10, -70, -130, -270, -390, -500, -670, -710, -1000, -1360,
               -1420, -1480, -1700, -1760, -1820, -2000, -2060, -2120, 2300,
               2360, 2420, 2600, 2660, 2720, 2900, 2960, 3020]
listaContadores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0]
for i in range(40):
    numrandom = random.choice(listaRandom)
    ENEMIGO_REGULAR = (random.randint(0, 255), numrandom, 'REGULAR', 1)
    ENEMIGOS_TOTAL.append(ENEMIGO_REGULAR)
    for element in listaRandom:
        if numrandom == element:
            num = listaRandom.index(element)
            listaContadores[num] += 1
            if listaContadores[num] > 1:
                del (listaRandom[num])
                del (listaContadores[num])

# ENEMIGOS ROJOS
# Lista de posibles x que tendrán los aviones rojos
listaRandom = [-300, -400, -500, -600]
numrandom = random.choice(listaRandom)
for i in range(5):
    ENEMIGO_ROJO = (numrandom, 30, 'ROJO', 1)
    ENEMIGOS_TOTAL.append(ENEMIGO_ROJO)
    numrandom -= 22
# Creamos dos tandas de enemigos rojos
listaRandom = [-1000, -1100, -1200, -1300]
numrandom = random.choice(listaRandom)
for i in range(5):
    ENEMIGO_ROJO = (numrandom, 30, 'ROJO', 1)
    ENEMIGOS_TOTAL.append(ENEMIGO_ROJO)
    numrandom -= 22

# BOMBARDEROS
# Lista de posibles (y)es que tendrán los bombarderos
listaRandom = [-600, -1100, -1500]
for i in range(2):
    numrandom = random.choice(listaRandom)
    ENEMIGO_BOMBARDERO = (20, numrandom, 'BOMBARDERO', 5)
    ENEMIGOS_TOTAL.append(ENEMIGO_BOMBARDERO)
    # Para que no se creen dos bombarderos en la misma posición
    for element in listaRandom:
        if element == numrandom:
            k = listaRandom.index(element)
            del (listaRandom[k])

# SUPERBOMBARDEROS
# Lista de posibles (y)es que tendrán los bombarderos
listaRandom = [600, 700, 800, 900]
ENEMIGO_SUPERBOMBARDERO = (
160, random.choice(listaRandom), 'SUPERBOMBARDERO', 10)
ENEMIGOS_TOTAL.append(ENEMIGO_SUPERBOMBARDERO)

# SPRITES ISLAS
SPRITE_PORTA_AVIONES = (1, 160, 0, 60, 128)
SPRITE_ISLA1 = (1, 0, 180, 60, 35)
SPRITE_ISLA2 = (1, 35, 0, 70, 57)
# Lista de posibles (y)es con sus contadores para evitar la repetición
listaRandom = [-60, -340, -640, -900, -1300, -1700, -1920]
ISLAS_FINALES = []
ISLAS_FINALES.append((104, 130, 'PORTAAVIONES'))
for i in range(3):
    numrandom = random.choice(listaRandom)
    ISLA_1 = (random.randint(0, 200), numrandom, 'ISLA1')
    ISLAS_FINALES.append(ISLA_1)
    # Para evitar la repetición
    for element in listaRandom:
        if numrandom == element:
            k = listaRandom.index(element)
            del (listaRandom[k])
for i in range(3):
    numrandom = random.choice(listaRandom)
    ISLA_2 = (random.randint(0, 200), numrandom, 'ISLA2')
    ISLAS_FINALES.append(ISLA_2)
    # Para evitar la repetición
    for element in listaRandom:
        if numrandom == element:
            k = listaRandom.index(element)
            del (listaRandom[k])
