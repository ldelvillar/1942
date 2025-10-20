"""
Creado por Lucas del Villar y Javier Esteve en 2022
Universidad Carlos III de Madrid
"""

import random


class Disparo:
    # Esta clase crea disparos tanto enemigos como aliados,
    # y su método init tiene como atributos una x, una y y el tipo
    def __init__(self, x: int, y: int, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo
        # Sprites según el tipo
        if self.tipo == 'ALIADO':
            self.sprite = (0, 60, 32, 7, 10)
        elif self.tipo == 'ENEMIGO':
            self.sprite = (0, 80, 32, 7, 5)
        # Velocidades
        self.velocidad_aliado = 4
        self.velocidad_x_enemigo = random.randint(-3, 3)
        self.velocidad_y_enemigo = 3

    def disparo(self):
        # Este método define el movimiento de las balas
        # según el tipo de balas que sean
        if self.tipo == 'ALIADO':
            self.y -= self.velocidad_aliado
        elif self.tipo == 'ENEMIGO':
            self.x += self.velocidad_x_enemigo
            self.y += self.velocidad_y_enemigo
