# 🛩️ 1942 - Juego de Aviones Clásico

Un clon del clásico juego de arcade **1942** desarrollado en Python utilizando la biblioteca Pyxel. Este proyecto recrea la experiencia del juego de aviones de combate vertical donde el jugador debe sobrevivir oleadas de enemigos mientras acumula la mayor puntuación posible.

## 📋 Descripción del Proyecto

Este juego es una recreación del arcade clásico 1942, desarrollado como proyecto académico en la Universidad Carlos III de Madrid. El jugador controla un avión de combate que debe enfrentarse a diferentes tipos de enemigos mientras esquiva disparos y realiza maniobras evasivas.

### Características Principales

- ✈️ **Control del Avión Principal**: Movimiento en 4 direcciones con animación de hélices
- 🎯 **Sistema de Disparos**: Dispara proyectiles para destruir enemigos
- 🔄 **Maniobras Especiales**: Realiza loops para esquivar enemigos (limitado a 3 por vida)
- 👾 **Múltiples Tipos de Enemigos**:
  - **Regulares**: Enemigos básicos con movimiento diagonal
  - **Rojos**: Aviones que realizan patrones circulares
  - **Bombarderos**: Aviones grandes con movimiento en zigzag
  - **Superbombarderos**: Jefes con gran resistencia y múltiples disparos
- 🏝️ **Escenario Dinámico**: Islas y portaaviones que se desplazan para crear profundidad
- 💯 **Sistema de Puntuación**: Diferentes enemigos otorgan distintos puntos
- ❤️ **Sistema de Vidas**: 3 vidas para completar el juego
- 🎵 **Efectos de Sonido**: Disparos y explosiones

## 🎮 Controles del Juego

| Tecla   | Acción                                               |
| ------- | ---------------------------------------------------- |
| `↑`     | Mover hacia arriba                                   |
| `↓`     | Mover hacia abajo                                    |
| `←`     | Mover hacia la izquierda                             |
| `→`     | Mover hacia la derecha                               |
| `S`     | Disparar                                             |
| `Z`     | Realizar loop (maniobra evasiva)                     |
| `ENTER` | Iniciar juego / Continuar después de perder una vida |
| `Q`     | Salir del juego                                      |

## 🛠️ Requisitos del Sistema

- **Python**: 3.7 o superior
- **Pyxel**: 1.4.0 o superior
- **Sistema Operativo**: Windows, macOS o Linux

## 📦 Instalación y Configuración

### Paso 1: Instalar Python

Si no tienes Python instalado, descárgalo desde [python.org](https://www.python.org/downloads/) y asegúrate de instalarlo con la opción "Add Python to PATH".

Para verificar la instalación:

```bash
python --version
```

### Paso 2: Instalar Pyxel

Pyxel es la biblioteca de juegos retro utilizada para este proyecto. Instálala ejecutando:

```bash
pip install pyxel
```

### Paso 3: Clonar o Descargar el Proyecto

Descarga el proyecto y asegúrate de tener la siguiente estructura de archivos:

```
1942/
│
├── README.md
├── assets/                 # Carpeta con todos los sprites e imágenes
│   ├── AvionPrincipal.png
│   ├── AvionPrincipal2.png
│   ├── EnemigoRegular.png
│   ├── EnemigoRojo.png
│   ├── Bombardero.png
│   ├── isla1.png
│   └── ... (más sprites)
│
└── src/                    # Carpeta con el código fuente
    ├── main.py            # Archivo principal para ejecutar el juego
    ├── tablero.py         # Lógica del tablero y game loop
    ├── avion.py           # Clase del avión principal
    ├── enemigo.py         # Clase de los enemigos
    ├── disparo.py         # Clase de los disparos
    ├── islas.py           # Clase de los elementos del escenario
    └── constantes.py      # Configuración y constantes del juego
```

### Paso 4: Ejecutar el Juego

Navega a la carpeta `src` y ejecuta el archivo principal:

```bash
cd src
python main.py
```

El juego se iniciará en una ventana de 224x256 píxeles.

## 🏗️ Arquitectura del Código

### Estructura de Clases

#### `Tablero` (tablero.py)

Clase principal que gestiona:

- Inicialización de Pyxel y carga de recursos
- Game loop (métodos `update()` y `draw()`)
- Gestión de escenas (inicial, juego, final)
- Detección de colisiones
- Sistema de puntuación y vidas

#### `Avion` (avion.py)

Clase del avión jugador:

- Posición y movimiento
- Sistema de disparos
- Animación de sprites
- Contador de loops disponibles

#### `Enemigo` (enemigo.py)

Clase de enemigos con:

- 4 tipos diferentes (Regular, Rojo, Bombardero, Superbombardero)
- Patrones de movimiento únicos para cada tipo
- Sistema de puntos de vida (hits)
- Disparos automáticos
- Valor de puntuación

#### `Disparo` (disparo.py)

Clase de proyectiles:

- Diferenciación entre disparos aliados y enemigos
- Velocidades y sprites personalizados
- Movimiento automático

#### `Islas` (islas.py)

Clase de elementos del escenario:

- Portaaviones e islas decorativas
- Movimiento de desplazamiento para simular profundidad

#### `constantes.py`

Archivo de configuración que contiene:

- Dimensiones de la pantalla
- Coordenadas de sprites
- Generación aleatoria de enemigos e islas
- Listas de objetos del juego

## 🎯 Sistema de Puntuación

| Tipo de Enemigo | Puntos |
| --------------- | ------ |
| Regular         | 100    |
| Rojo            | 200    |
| Bombardero      | 500    |
| Superbombardero | 1000   |

## 🎨 Recursos Gráficos

Todos los sprites están almacenados en la carpeta `assets/`:

- Aviones (principal, enemigos, variantes)
- Proyectiles (aliados y enemigos)
- Escenario (islas, portaaviones)
- Diferentes estados de animación para cada objeto

## ⚙️ Mecánicas del Juego

### Sistema de Vidas

- Comienzas con **3 vidas**
- Pierdes una vida al ser impactado por un disparo enemigo o al colisionar con un enemigo
- Al perder una vida, puedes continuar presionando `ENTER`
- El juego termina cuando pierdes las 3 vidas

### Sistema de Loops

- Tienes **3 loops** disponibles por vida
- Un loop es una maniobra evasiva que te hace invulnerable momentáneamente
- Se activan presionando la tecla `Z`

### Duración del Juego

- El juego tiene una duración límite de aproximadamente **2000 frames** por vida
- Si sobrevives todo el tiempo, avanzas al siguiente nivel o al Game Over

## 🐛 Solución de Problemas

### El juego no inicia

- Verifica que Pyxel esté correctamente instalado: `pip show pyxel`
- Asegúrate de estar ejecutando desde la carpeta `src`
- Verifica que la carpeta `assets` esté en la ubicación correcta

### Error al cargar imágenes

- Confirma que todas las imágenes PNG estén en la carpeta `assets`
- Las rutas de las imágenes están configuradas como `../assets/`, lo que requiere ejecutar desde `src`

### El juego va muy lento

- Pyxel está optimizado para juegos retro, pero si experimentas lentitud, cierra otras aplicaciones
- Verifica que tu versión de Python sea 3.7 o superior

## 👥 Créditos

**Desarrolladores**: Lucas del Villar y Javier Esteve  
**Institución**: Universidad Carlos III de Madrid  
**Año**: 2022  
**Tecnología**: Python + Pyxel

## 📄 Licencia

Proyecto académico desarrollado con fines educativos.

## 🎮 ¡Disfruta del Juego!

¡Demuestra tus habilidades de piloto y consigue la mayor puntuación posible! 🏆

---

_Basado en el clásico arcade 1942 de Capcom_
