import pygame
import subprocess

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
ANCHO = 800
ALTO = 650

# Definir el nombre de la fuente y el tamaño
font_name = "none"
font_size = 24

# Crear una instancia de la fuente
#fuente = pygame.font.SysFont(font_name, font_size)

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego con instrucciones")

# Definir colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)  

# Cargar imagen de fondo    
fondo = pygame.image.load("assets/images/inicio5.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

# Fuente del texto
fuente = pygame.font.SysFont(font_name, font_size)

# Texto de instrucciones
instrucciones = [
    "¡Bienvenido al juego!",
"El juego cuenta con 3 botones principales en la pantalla de inicio:",
"1. Botón Play sirve para iniciar el juego.",
"2. Botón Instrucciones abre las instrucciones de cada nivel.",
"3. Botón Salir cierra el juego por completo.",
"Al dar clic en el botón play inicia el primer nivel del juego:",
"1. En el primer nivel de juego se usa la barra espaciadora para", 
"esquivar los obstáculos, con cada clic se eleva el personaje.",
"2. Cada vez que supera un obstáculo la pantalla muestra un dato",
"sobre los planetas del “Sistema Solar”.",
"3. En la parte superior izquierda indica la puntuación, al superar ",
"los 7 puntos superamos la partida y podemos continuar al siguiente nivel.",
"4. Si choca aparecerá dos botones para repetir el nivel y continuar el nivel.,"
"Si elegimos avanzar el segundo nivel tenemos un juego de memoria:",
"1. Al iniciar el juego aparecerán recuadros en el que se debe elegir las ",
"parejas para sumar puntuación.",
"2. Si completa la primera partida en la siguiente aumenta la dificultad ",
"hasta completar el nivel",
]


# Crear botón
boton_rect = pygame.Rect(ANCHO - 750, 20, 100, 50)
borde_redondeado = 10                           

# Variable para controlar el bucle principal
ejecutando = True

while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si se hizo clic en el botón
            if boton_rect.collidepoint(event.pos):
                # Abrir otro archivo utilizando subprocess
                subprocess.Popen(["python", "index.py"])  # Reemplaza "otro_archivo.py" por el nombre de tu archivo
                pygame.quit()
                quit()
    # Dibujar el fondo y el botón en la ventana
    ventana.blit(fondo, (0, 0))
    pygame.draw.rect(ventana, AZUL, boton_rect, border_radius=borde_redondeado)

    # Dibujar el texto en el botón
    texto = fuente.render("Regresar", True, BLANCO) 
    texto_rect = texto.get_rect(center=boton_rect.center)
    ventana.blit(texto, texto_rect)

    # Dibujar el texto de instrucciones
    y = 100
    for linea in instrucciones:
        texto_instrucciones = fuente.render(linea, True, BLANCO)
        texto_instrucciones_rect = texto_instrucciones.get_rect(midleft=(50, y))
        ventana.blit(texto_instrucciones, texto_instrucciones_rect)
        y += 30

    # Actualizar la ventana
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()
