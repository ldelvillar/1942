"""
Creado por Lucas del Villar y Javier Esteve en 2022
Universidad Carlos III de Madrid
"""

import random
import constantes
from disparo import Disparo


class Enemigo:
    # Está clase crea enemigos y su método init tiene de atributos
    # x e y para la posición, el tipo de enmigo y los hits necesarios
    # para eliminarlo
    def __init__(self, x: int, y: int, tipo: str, hits: int):
        self.x = x
        self.y = y
        self.tipo = tipo
        self.hits = hits
        self.disparos = []
        if tipo == 'REGULAR':
            self.puntuacion = 100
        if tipo == 'ROJO':
            self.puntuacion = 200
        if tipo == 'BOMBARDERO':
            self.puntuacion = 500
        if tipo == 'SUPERBOMBARDERO':
            self.puntuacion = 1000
        # velocidades de cada enemigo
        self.velocidad_regular_x = 1
        self.velocidad_regular_y = 1.5
        self.velocidad_rojo_x = 2
        self.velocidad_rojo_y = 2
        self.velocidad_bombardero_x = 1
        self.velocidad_bombardero_y = 1
        self.velocidad_superBombardero_x = 0.5
        self.velocidad_superBombardero_y = -0.5
        # atributos que sirven para definir el movimiento
        self.num = random.randint(0, 1)
        self.circulo = False
        self.circulo2 = False

        # Sprites según el tipo
        if tipo == "REGULAR":
            self.sprite = constantes.SPRITE_REGULAR
        elif tipo == "ROJO":
            self.sprite = constantes.SPRITE_ROJO
        elif tipo == "BOMBARDERO":
            self.sprite = constantes.SPRITE_BOMBARDERO
        elif tipo == "SUPERBOMBARDERO":
            self.sprite = constantes.SPRITE_SUPERBOMBARDERO

    def mover(self):
        """Este método hace que los enemigos se muevan. Utilizaremos un
        movimiento diferente para cada tipo de enemigo"""
        if self.tipo == "REGULAR":
            if self.num == 0 and self.velocidad_regular_x > 0:
                self.velocidad_regular_x = -self.velocidad_regular_x
            if self.y > 150 and self.velocidad_regular_y > 0:
                self.velocidad_regular_y = - self.velocidad_regular_y
            if self.velocidad_regular_y > 0:
                self.y += self.velocidad_regular_y
            if self.velocidad_regular_y < 0:
                self.y += self.velocidad_regular_y
                self.x += self.velocidad_regular_x

        elif self.tipo == "ROJO":
            if self.x < 70 and self.y == 30:
                self.x += self.velocidad_rojo_x
            elif 29 < self.x <= 270:
                self.x += self.velocidad_rojo_x
                self.y += self.velocidad_rojo_y
            if (self.x == 110 and self.y == 70) or (
                    self.x == 230 and self.y == 70):
                self.velocidad_rojo_x = -self.velocidad_rojo_x
            if (self.y == 110 and self.x == 70) or (
                    self.y == 110 and self.x == 190):
                self.velocidad_rojo_y = -self.velocidad_rojo_y
            if self.y == 70 and self.x == 30:
                self.velocidad_rojo_x = -self.velocidad_rojo_x
                self.circulo = True
            if self.y == 70 and self.x == 150:
                self.velocidad_rojo_x = -self.velocidad_rojo_x
                self.circulo = False
            if (self.x == 70 and self.y == 30 and self.circulo == True) or (
                    self.x == 190 and self.y == 30 and self.circulo == False):
                self.velocidad_rojo_y = 0
            if self.x == 190 and self.y == 30 and self.circulo == True:
                self.velocidad_rojo_y = self.velocidad_rojo_x

        elif self.tipo == "BOMBARDERO":
            if self.y < 100 and self.x == 20:
                self.velocidad_bombardero_x = 0
            elif 99 < self.y < 110 and self.x < 30:
                self.velocidad_bombardero_x = self.velocidad_bombardero_y
            elif self.y == 110 and self.x == 30:
                self.velocidad_bombardero_y = 0
            elif self.x == 200 and self.y == 110:
                self.velocidad_bombardero_y = -self.velocidad_bombardero_x
            elif self.x == 210:
                self.velocidad_bombardero_x = -self.velocidad_bombardero_x
            elif self.x == 200 and self.y == 90:
                self.velocidad_bombardero_y = 0
            elif self.x == 80 and self.y == 90:
                self.velocidad_bombardero_y = -self.velocidad_bombardero_x
            elif self.x == 70 and self.y == 100:
                self.velocidad_bombardero_x = 0
            self.x += self.velocidad_bombardero_x
            self.y += self.velocidad_bombardero_y

        elif self.tipo == "SUPERBOMBARDERO":
            if self.y > 60:
                self.velocidad_superBombardero_x = 0
            elif self.y == 60 and self.x == 160 and self.circulo2 == False:
                self.velocidad_superBombardero_x = \
                    -self.velocidad_superBombardero_y
                self.velocidad_superBombardero_y = \
                    -self.velocidad_superBombardero_x
            elif self.x == 190 and self.y == 30:
                self.velocidad_superBombardero_y = 0
                self.velocidad_superBombardero_x = \
                    -self.velocidad_superBombardero_x
            elif self.x == 30 and self.y == 30:
                self.velocidad_superBombardero_y = \
                    -self.velocidad_superBombardero_x
            elif self.x == 0 and self.y == 60:
                self.velocidad_superBombardero_x = \
                    -self.velocidad_superBombardero_x
                self.velocidad_superBombardero_y = 0
                self.circulo2 = True
            elif self.y == 60 and self.x == 160:
                self.velocidad_superBombardero_y = \
                    -self.velocidad_superBombardero_x

            self.x += self.velocidad_superBombardero_x
            self.y += self.velocidad_superBombardero_y

    def disparo(self):
        # Este método crea los disparos de los enemigos
        # que varían según el tipo
        if self.tipo == 'REGULAR':
            num = random.randint(0, 1)
            if num == 1:
                bala = Disparo(self.x + 8, self.y + 16, 'ENEMIGO')
                self.disparos.append(bala)
        elif self.tipo == 'BOMBARDERO':
            bala = Disparo(self.x + 15, self.y + 30, 'ENEMIGO')
            self.disparos.append(bala)
        elif self.tipo == 'SUPERBOMBARDERO':
            bala = Disparo(self.x + 30, self.y + 32, 'ENEMIGO')
            self.disparos.append(bala)
            bala2 = Disparo(self.x + 30, self.y + 32, 'ENEMIGO')
            self.disparos.append(bala2)
            bala3 = Disparo(self.x + 30, self.y + 32, 'ENEMIGO')
            self.disparos.append(bala3)
