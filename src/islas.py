"""
Creado por Lucas del Villar y Javier Esteve en 2022
Universidad Carlos III de Madrid
"""

import constantes


class Islas:
    # Está clase crea islas y su método init tiene
    # una x e y para la posición y el tipo de isla
    def __init__(self, x: int, y: int, tipo=str):

        self.x = x
        self.y = y
        self.tipo = tipo
        # Sprites según el tipo
        if tipo == 'PORTAAVIONES':
            self.sprite = constantes.SPRITE_PORTA_AVIONES
        elif tipo == 'ISLA1':
            self.sprite = constantes.SPRITE_ISLA1
        elif tipo == 'ISLA2':
            self.sprite = constantes.SPRITE_ISLA2

    def mover(self):
        # Este método define el movimiento de las islas
        if self.tipo == 'PORTAAVIONES':
            self.y += 0.5
        elif self.tipo == 'ISLA1':
            self.y += 0.5
        elif self.tipo == 'ISLA2':
            self.y += 0.5
