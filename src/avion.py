"""
Creado por Lucas del Villar y Javier Esteve en 2022
Universidad Carlos III de Madrid
"""

from disparo import Disparo


class Avion:
    """Esta clase almacena toda la información necesaria para nuestro avión,
    su método init tiene una x e y para la posición"""

    def __init__(self, x: int, y: int):

        self.x = x
        self.y = y
        self.disparos = []
        self.tipo = 'AVIÓN'
        # Consideramos que tiene tres vidas al principio del juego
        self.lives = 3
        # Para cargar los sprites tenemos la tupla (banco, x, y, tamaño). En
        # este caso, nuestro avión tiene 16 x 16 de tamaño. Cargamos una
        # segunda imagen para el movimiento de las hélices
        self.sprite = (0, 0, 0, 16, 16)
        self.sprite2 = (0, 16, 0, 16, 16)
        self.spriteLoops = (0, 130, 32, 16, 16)
        # Contador para los loops
        self.loops = 3

    def mover(self, direccion: str, tamaño: int):
        """Este método define el movimiento del avión, depende del input del
        usuario"""
        tamaño_avion_x = tamaño_avion_y = self.sprite[3]
        # Movimiento horizontal
        if direccion.lower() == "derecha" and self.x < tamaño - tamaño_avion_x:
            self.x += 2
        elif direccion.lower() == "izquierda" and self.x > 0:
            self.x -= 2
        # Movimiento vertical
        elif direccion.lower() == "arriba" and self.y > 50:
            self.y -= 2
        elif direccion.lower() == "abajo" and self.y < tamaño - \
                tamaño_avion_y - 30:
            self.y += 2
        # Loop
        elif direccion.lower() == "loop" and self.y < tamaño - \
                tamaño_avion_y - 30 and self.loops > 0:
            self.y += 10

    def disparo(self):
        """Este método crea los disparos del avión principal"""
        bala = Disparo(self.x, self.y, 'ALIADO')
        self.disparos.append(bala)
