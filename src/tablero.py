"""
Creado por Lucas del Villar y Javier Esteve en 2022
Universidad Carlos III de Madrid
"""

from avion import Avion
import pyxel
import constantes
from enemigo import Enemigo
from disparo import Disparo
from islas import Islas


class Tablero:
    """Esta clase contiene la información necesaria para representar el
    tablero"""

    def __init__(self, w: int = 255, h: int = 255):
        # Este método init contiene atributos como el ancho o alto,
        # las puntuaciones, la escena o los loops.

        self.ancho = w
        self.alto = h
        self.score = 0
        self.scoreMax = 0
        self.escena = 'ESCENA_INICIAL'
        self.loops = 3
        self.comprobarLoop = False
        # Este bloque inicializa pyxel
        # Lo primero que tenemos que hacer es crear la pantalla
        pyxel.init(self.ancho, self.alto, title="1942")

        # Cargamos las imágenes
        # ISLAS Y PORTAAVIONES
        pyxel.image(1).load(0, 180, '../assets/isla1.png')
        pyxel.image(1).load(35, 0, '../assets/isla2.png')
        pyxel.image(1).load(160, 0, '../assets/portaAviones1.png')
        # AVIÓN PRINCIPAL
        pyxel.image(0).load(0, 0, '../assets/AvionPrincipal.png')
        pyxel.image(0).load(16, 0, '../assets/AvionPrincipal2.png')
        pyxel.image(0).load(130, 32, '../assets/AvionPrincipalLoop.png')
        # ENEMIGO REGULAR
        pyxel.image(0).load(32, 0, '../assets/EnemigoRegular.png')
        pyxel.image(0).load(48, 0, '../assets/EnemigoRegular arriba.png')
        # ENEMIGO ROJO
        pyxel.image(0).load(64, 0, '../assets/EnemigoRojo.png')
        pyxel.image(0).load(78, 0, '../assets/Enemigo rojo derecha.png')
        pyxel.image(0).load(92, 0, '../assets/Enemigo rojo arriba.png')
        # BOMBARDERO
        pyxel.image(0).load(106, 0, '../assets/Bombardero.png')
        pyxel.image(0).load(136, 0, '../assets/Bombardero derecha.png')
        pyxel.image(0).load(166, 0, '../assets/Bombardero izquierda.png')
        pyxel.image(0).load(196, 0, '../assets/Bombardero arriba.png')
        # SUPERBOMBARDERO
        pyxel.image(0).load(0, 32, '../assets/Superbombardero.png')
        # BALAS
        pyxel.image(0).load(60, 32, '../assets/BalaRegular.png')
        pyxel.image(0).load(80, 32, '../assets/balaEnemigo.png')
        # SONIDO DE BALA
        pyxel.sound(0).set("c3e3g3c1e1g1", "n", "10", "f", 3)
        # SONIDO DE EXPLOSIÓN
        pyxel.sound(1).set("a3a2a1", "n", "7742", "s", 10)

        # Trabajamos con la clase avión
        # Crea un avión en la mitad de la pantalla en x y en y en la
        # posición 200

        self.avion = Avion(120, 200)
        self.disparo = Disparo(300, 300, 'ALIADO')
        # Consideramos que tiene tres vidas al principio del juego
        self.lives = 3
        self.vivo = True
        self.framesFinales = 2000
        # Lista de enemigos
        self.enemigos = []
        for element in constantes.ENEMIGOS_TOTAL:
            enemigo = Enemigo(element[0], element[1], element[2], element[3])
            self.enemigos.append(enemigo)
        # Lista de islas
        self.islas = []
        for element in constantes.ISLAS_FINALES:
            isla = Islas(element[0], element[1], element[2])
            self.islas.append(isla)
        # Ejecutamos el juego
        pyxel.run(self.update, self.draw)

    def reiniciar(self):
        """Este método reinicia los atributos
        y se ejecuta cuando aparece la pantalla inicial"""
        if self.escena == 'ESCENA_INICIAL':
            self.score = 0
            self.vivo = True
            self.avion = Avion(120, 200)
            self.disparo = Disparo(300, 300, 'ALIADO')
            # Consideramos que tiene tres vidas al principio del juego

            # Lista de enemigos
            self.enemigos = []
            for element in constantes.ENEMIGOS_TOTAL:
                enemigo = Enemigo(element[0], element[1], element[2],
                                  element[3])
                self.enemigos.append(enemigo)
            # Lista de islas
            self.islas = []
            for element in constantes.ISLAS_FINALES:
                isla = Islas(element[0], element[1], element[2])
                self.islas.append(isla)

    def check_se_tocan(self, a, b):
        """Este método comprueba si la posición de un parámetro a está dentro
        de una baldosa del tamaño del parámetro b. Estos parámetros van a ser
        las balas y los aviones si es el avión principal"""
        if a.tipo == 'AVIÓN':
            ax2, ay2 = a.x + 16 - 1, a.y + 16 - 1
        # si es una bala aliada
        elif a.tipo == 'ALIADO':
            ax2, ay2 = a.x + 7 - 1, a.y + 10 - 1
        # si es una bala enemiga
        elif a.tipo == 'ENEMIGO':
            ax2, ay2 = a.x + 7 - 1, a.y + 5 - 1
        # esquinas
        esi = a.x, a.y  # esquina superior izquierda
        esd = ax2, a.y  # esquina superior derecha
        eii = a.x, ay2  # esquina inferior izquierda
        eid = ax2, ay2  # esquina inferior derecha
        # enemigo regular
        if b.tipo == 'REGULAR':
            bx2, by2 = b.x + 16 - 1, b.y + 16 - 1
        # enemigo rojo
        elif b.tipo == 'ROJO':
            bx2, by2 = b.x + 14 - 1, b.y + 14 - 1
        # bombardero
        elif b.tipo == 'BOMBARDERO':
            bx2, by2 = b.x + 30 - 1, b.y + 30 - 1
        # superbombardero
        elif b.tipo == 'SUPERBOMBARDERO':
            bx2, by2 = b.x + 60 - 1, b.y + 32 - 1
        elif b.tipo == 'AVIÓN':
            bx2, by2 = b.x + 16 - 1, b.y + 16 - 1

        # si alguna esquina está dentro de los límites de la baldosa,
        # es que la está tocando
        if b.x <= esi[0] <= bx2 and b.y <= esi[1] <= by2 or \
                b.x <= esd[0] <= bx2 and b.y <= esd[1] <= by2 or \
                b.x <= eii[0] <= bx2 and b.y <= eii[1] <= by2 or \
                b.x <= eid[0] <= bx2 and b.y <= eid[1] <= by2:
            return True

    def cargarEscenaInicial(self):
        """Este método carga la escena inicial"""
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.escena = 'ESCENA_DE_JUEGO'

    def cargarEscenaFinal(self):
        """Este método carga las escenas finales"""
        # Si el avión principal es abatido y le quedan vidas
        if self.vivo == False and self.lives > 0:
            self.escena = 'ESCENA_FINAL'
        # Volver a la escena inicial
        if self.escena == 'ESCENA_FINAL':
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.escena = 'ESCENA_INICIAL'
        # Si se acaban las vidas o el tiempo de juego (2000 frames)se carga
        # el final
        if (self.lives == 0) or (
                self.lives == 3 and pyxel.frame_count > self.framesFinales) \
                or \
                (self.lives == 2 and pyxel.frame_count > self.framesFinales
                 * 2) or \
                (self.lives == 1 and pyxel.frame_count > self.framesFinales
                 * 3):
            self.escena = 'FINAL'

    def update(self):
        """Esto se ejecuta cada frame, aquí vamos a invocar los métodos que
        actualizan los objetos (update)"""

        # Al pulsar 'Q', acabarse las vidas, o conseguir ganar se cierra el
        # juego. Consideraremos que se gana cuando se juega por algo más de
        # un minuto (2000 frames)
        if pyxel.btnp(pyxel.KEY_Q):
            quit()
        if pyxel.frame_count % 15 == 0:
            self.comprobarLoop = False

        # Para cargar las escenas
        self.cargarEscenaInicial()
        self.cargarEscenaFinal()
        # Si la puntuación actual supera la puntuación máxima, se convierte
        # en la nueva puntuación máxima
        if self.score > self.scoreMax:
            self.scoreMax = self.score
        if self.escena == 'ESCENA_INICIAL':
            self.reiniciar()
        if self.escena == 'ESCENA_DE_JUEGO':
            # Hacemos el disparo
            if pyxel.btnp(pyxel.KEY_S):
                self.avion.disparo()
                pyxel.play(0, 0)

            # Hacemos el movimiento
            # Movimiento horizontal
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.avion.mover('derecha', self.ancho)
            if pyxel.btn(pyxel.KEY_LEFT):
                self.avion.mover('izquierda', self.ancho)
            # Movimiento vertical
            if pyxel.btn(pyxel.KEY_UP):
                self.avion.mover('arriba', self.alto)
            if pyxel.btn(pyxel.KEY_DOWN):
                self.avion.mover('abajo', self.alto)
            # Loops
            if pyxel.btnp(pyxel.KEY_Z) and self.loops > 0:
                self.avion.mover('loop', self.alto)
                self.loops -= 1
                self.comprobarLoop = True

            # Disparo del avión principal
            for i in self.avion.disparos:
                i.disparo()
                # Si el disparo sale de la pantalla lo eliminamos
                if i.y < -10 or i.y > 260:
                    self.avion.disparos.remove(i)
            # Disparo y movimiento de los enemigos
            for i in self.enemigos:
                i.mover()
                if pyxel.frame_count % 80 == 0:
                    i.disparo()
                for j in i.disparos:
                    j.disparo()
                    # Si el disparo sale de la pantalla lo eliminamos
                    if j.y < -7 or j.y > 262 or j.x < -7 or j.x > 262:
                        i.disparos.remove(j)
            # Movimiento de las islas
            for i in self.islas:
                i.mover()
            # Contacto entre balas y enemigos
            for e in self.enemigos:
                for b in self.avion.disparos:
                    if self.check_se_tocan(b, e):
                        self.avion.disparos.remove(b)
                        e.hits -= 1
                        if e.hits == 0:
                            pyxel.play(1, 1)
                            self.score += e.puntuacion
                            self.enemigos.remove(e)
            # Contacto entre balas enemigas y el avión principal
            for i in self.enemigos:
                for j in i.disparos:
                    if self.check_se_tocan(j, self.avion):
                        i.disparos.remove(j)
                        self.lives -= 1
                        self.vivo = False
            # Contacto entre enemigos y el avión principal
            for e in self.enemigos:
                if self.check_se_tocan(self.avion, e):
                    self.enemigos.remove(e)
                    self.lives -= 1
                    self.vivo = False

    # MÉTODOS PARA DIBUJAR LOS OBJETOS (se invocarán en el draw):

    # Islas y portaviones
    def __pintarisla(self):
        """Este método hace aparecer los objetos del fondo, es decir,
        las islas y el portaaviones"""
        for element in self.islas:
            pyxel.blt(element.x, element.y, *element.sprite, colkey=7)

    # Avión principal
    def __pintarAvion(self):
        """Este método permite pintar el avión y hacer el movimiento de sus
        hélices"""
        if self.comprobarLoop == True:
            pyxel.blt(self.avion.x, self.avion.y, *self.avion.spriteLoops,
                      colkey=7)
        elif pyxel.frame_count // 1.5 % 2 == 0:
            pyxel.blt(self.avion.x, self.avion.y, *self.avion.sprite,
                      colkey=7)
        # Hélices
        else:
            pyxel.blt(self.avion.x, self.avion.y, *self.avion.sprite2,
                      colkey=7)

    def __pintarEnemigo(self):
        """Este método pinta a los enemigos y cambia sus sprites en los
        diferentes movimientos"""
        for element in self.enemigos:
            if element.tipo == 'ROJO':
                # Según el sentido de las velocidades dibujará un srpite u otro
                if (element.velocidad_rojo_y == 0) or (
                        element.x < 60 and element.y == 30):
                    pyxel.blt(element.x, element.y,
                              *constantes.SPRITE_ROJO_DERECHA, colkey=7)
                elif element.velocidad_rojo_y > 0:
                    pyxel.blt(element.x, element.y, *constantes.SPRITE_ROJO,
                              colkey=7)
                elif element.velocidad_rojo_y < 0:
                    pyxel.blt(element.x, element.y,
                              *constantes.SPRITE_ROJO_ARRIBA, colkey=7)
            elif element.tipo == 'REGULAR':
                # Según el sentido de las velocidades dibujará un srpite u otro
                if element.velocidad_regular_y > 0:
                    pyxel.blt(element.x, element.y, *constantes.SPRITE_REGULAR,
                              colkey=7)
                elif element.velocidad_regular_y < 0:
                    pyxel.blt(element.x, element.y,
                              *constantes.SPRITE_REGULAR_ARRIBA, colkey=7)
            elif element.tipo == 'BOMBARDERO':
                # Según el sentido de las velocidades dibujará un srpite u otro
                if element.velocidad_bombardero_y > 0:
                    pyxel.blt(element.x, element.y,
                              *constantes.SPRITE_BOMBARDERO, colkey=7)
                elif element.velocidad_bombardero_y < 0:
                    pyxel.blt(element.x, element.y,
                              *constantes.SPRITE_BOMBARDERO_ARRIBA, colkey=7)
                elif element.velocidad_bombardero_x > 0:
                    pyxel.blt(element.x, element.y,
                              *constantes.SPRITE_BOMBARDERO_DERECHA, colkey=7)
                elif element.velocidad_bombardero_x < 0:
                    pyxel.blt(element.x, element.y,
                              *constantes.SPRITE_BOMBARDERO_IZQUIERDA,
                              colkey=7)
            else:
                pyxel.blt(element.x, element.y, *element.sprite, colkey=7)

    def __pintarDisparo(self):
        """Este método pinta los disparos de nuestro avión y de los aviones
        enemigos"""
        for i in self.avion.disparos:
            pyxel.blt(i.x + 4, i.y - 6, *i.sprite, colkey=7)
        for i in self.enemigos:
            for j in i.disparos:
                pyxel.blt(j.x, j.y, *j.sprite, colkey=7)

    def draw(self):
        """Esto se ejecuta cada frame, aquí dibujamos los objetos"""
        # Color azul oscuro
        pyxel.cls(5)
        # Creamos los textos para la puntuación, las vidas y los loops
        textoInicial = 'PULSE ENTER PARA JUGAR'
        textoFinal = 'HAS SIDO ELIMINADO'
        puntuacion = f'SCORE: {self.score:>2}'
        puntuacionMax = f'MAX SCORE: {self.scoreMax:>2}'
        lives = f'VIDAS: {self.lives: >2}'
        loops = f'LOOPS: {self.loops: >2}'

        if self.escena == 'ESCENA_INICIAL':
            pyxel.text(85, 128, textoInicial, 0)
            self.cargarEscenaInicial()
        elif self.escena == 'ESCENA_DE_JUEGO':
            self.__pintarisla()
            self.__pintarAvion()
            self.__pintarEnemigo()
            self.__pintarDisparo()
            self.cargarEscenaFinal()
        elif self.escena == 'ESCENA_FINAL':
            self.cargarEscenaFinal()
            pyxel.text(90, 108, textoFinal, 0)
            pyxel.text(108, 128, puntuacion, 0)
            pyxel.text(72, 148, 'PRESIONE ENTER PARA CONTINUAR', 0)
            pyxel.text(85, 240, 'PRESIONE "Q" PARA SALIR', 0)
        elif self.escena == 'FINAL':
            self.cargarEscenaFinal()
            pyxel.text(110, 128, 'GAME OVER', 0)
            pyxel.text(85, 240, 'PRESIONE "Q" PARA SALIR', 0)
            pyxel.text(105, 148, puntuacionMax, 0)

        # Para cargar el texto tenemos la tupla (x, y, texto, color)
        pyxel.text(200, 5, puntuacion, 0)
        pyxel.text(20, 5, puntuacionMax, 0)
        pyxel.text(10, 245, lives, 0)
        pyxel.text(210, 245, loops, 0)
