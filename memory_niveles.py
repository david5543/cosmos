import pygame
import subprocess

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
CELESTE = (0, 255, 255)

# Inicializar pygame
pygame.init()

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Memoria")

# Cargar la imagen de fondo
imagen_fondo = pygame.image.load("images/LUCHITO.png")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO, ALTO))

# Cargar imágenes de los botones (usando imágenes de ejemplo)
imagen_boton1 = pygame.image.load("images/planetas/mercurio.png")
imagen_boton2 = pygame.image.load("images/planetas/venus.png")
imagen_boton3 = pygame.image.load("images/planetas/tierra.png")
imagen_boton4 = pygame.image.load("images/planetas/marte.png")
imagen_boton5 = pygame.image.load("images/planetas/jupier.png")
imagen_boton6 = pygame.image.load("images/planetas/saturno.png")
imagen_boton7 = pygame.image.load("images/planetas/urano.png")
imagen_boton_superior = pygame.image.load("images/regresar.png")


# Escalar las imágenes a un tamaño adecuado
imagen_boton1 = pygame.transform.scale(imagen_boton1, (100, 100))
imagen_boton2 = pygame.transform.scale(imagen_boton2, (100, 100))
imagen_boton3 = pygame.transform.scale(imagen_boton3, (100, 100))
imagen_boton4 = pygame.transform.scale(imagen_boton4, (100, 100))
imagen_boton5 = pygame.transform.scale(imagen_boton5, (100, 100))
imagen_boton6 = pygame.transform.scale(imagen_boton6, (100, 100))
imagen_boton7 = pygame.transform.scale(imagen_boton7, (100, 100))
imagen_boton_superior = pygame.transform.scale(imagen_boton_superior, (120, 90))


# Obtener los rectángulos de las imágenes para posicionar los botones
rect_boton1 = imagen_boton1.get_rect()
rect_boton2 = imagen_boton2.get_rect()
rect_boton3 = imagen_boton3.get_rect()
rect_boton4 = imagen_boton4.get_rect()
rect_boton5 = imagen_boton5.get_rect()
rect_boton6 = imagen_boton6.get_rect()
rect_boton7 = imagen_boton7.get_rect()
rect_boton_superior = imagen_boton_superior.get_rect()

# Posicionar los botones en el lado derecho
rect_boton1.topleft = (ANCHO // 2, 50)
rect_boton2.topleft = (ANCHO // 2, 175)
rect_boton3.topleft = (ANCHO // 2, 300)
rect_boton4.topleft = (ANCHO // 2 + 150, 50)
rect_boton5.topleft = (ANCHO // 2 + 150, 175)
rect_boton6.topleft = (ANCHO // 2 + 150, 300)
rect_boton7.topleft = (ANCHO // 2 + 300, 175)
rect_boton_superior.topleft = (0, 0)

# Textos de los botones
texto_boton1 = "Mercurio"
texto_boton2 = "Venus"
texto_boton3 = "Tierra"
texto_boton4 = "Marte"
texto_boton5 = "Júpiter"
texto_boton6 = "Saturno"
texto_boton7 = "Urano"

# Fuente para el texto de los botones
fuente_boton = pygame.font.Font(None, 24)

# Bucle principal del juego
juego_activo = True
while juego_activo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            juego_activo = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si se hizo clic en uno de los botones
            if rect_boton1.collidepoint(event.pos):
                subprocess.Popen(["python", "memory_mercurio.py"])
                pygame.quit()
            elif rect_boton2.collidepoint(event.pos):
                subprocess.Popen(["python", "memory_venus.py"])
                pygame.quit()
            elif rect_boton3.collidepoint(event.pos):
                subprocess.Popen(["python", "memory_tierra.py"])
                pygame.quit()
            elif rect_boton4.collidepoint(event.pos):
                subprocess.Popen(["python", "memory_venus.py"])
                pygame.quit()
            elif rect_boton5.collidepoint(event.pos):
                subprocess.Popen(["python", "memory_venus.py"])
                pygame.quit()
            elif rect_boton6.collidepoint(event.pos):
                subprocess.Popen(["python", "memory_venus.py"])
                pygame.quit()
            elif rect_boton7.collidepoint(event.pos):
                subprocess.Popen(["python", "memory_venus.py"])
                pygame.quit()
            elif rect_boton_superior.collidepoint(event.pos):
                subprocess.Popen(["python", "index.py"])
                pygame.quit()

    # Dibujar la imagen de fondo
    ventana.blit(imagen_fondo, (0, 0))
        
    # Dibujar el botón en la parte superior izquierda
    ventana.blit(imagen_boton_superior, rect_boton_superior)

    # Dibujar el título en el lado izquierdo
    titulo = pygame.font.Font(None, 70).render("JUEGO", True, CELESTE)
    titulo2 = pygame.font.Font(None, 40).render("DE", True, CELESTE)
    titulo3 = pygame.font.Font(None, 70).render("MEMORIA", True, CELESTE)
    titulo4 = pygame.font.Font(None, 30).render("Selecciona un planeta para jugar", True, BLANCO)
    ventana.blit(titulo, (90, ALTO // 6 - titulo.get_height() // 2))
    ventana.blit(titulo2, (90, ALTO // 3.8 - titulo.get_height() // 2))
    ventana.blit(titulo3, (90, ALTO // 3 - titulo.get_height() // 2))
    ventana.blit(titulo4, (50, ALTO // 1.5 - titulo.get_height() // 2))

    # Dibujar los botones en el lado derecho
    ventana.blit(imagen_boton1, rect_boton1)
    ventana.blit(imagen_boton2, rect_boton2)
    ventana.blit(imagen_boton3, rect_boton3)
    ventana.blit(imagen_boton4, rect_boton4)
    ventana.blit(imagen_boton5, rect_boton5)
    ventana.blit(imagen_boton6, rect_boton6)
    ventana.blit(imagen_boton7, rect_boton7)

    # Dibujar el texto debajo de cada botón
    texto1 = fuente_boton.render(texto_boton1, True, BLANCO)
    texto2 = fuente_boton.render(texto_boton2, True, BLANCO)
    texto3 = fuente_boton.render(texto_boton3, True, BLANCO)
    texto4 = fuente_boton.render(texto_boton4, True, BLANCO)
    texto5 = fuente_boton.render(texto_boton5, True, BLANCO)
    texto6 = fuente_boton.render(texto_boton6, True, BLANCO)
    texto7 = fuente_boton.render(texto_boton7, True, BLANCO)

    ventana.blit(texto1, (rect_boton1.left, rect_boton1.bottom))
    ventana.blit(texto2, (rect_boton2.left, rect_boton2.bottom))
    ventana.blit(texto3, (rect_boton3.left, rect_boton3.bottom))
    ventana.blit(texto4, (rect_boton4.left, rect_boton4.bottom))
    ventana.blit(texto5, (rect_boton5.left, rect_boton5.bottom))
    ventana.blit(texto6, (rect_boton6.left, rect_boton6.bottom))
    ventana.blit(texto7, (rect_boton7.left, rect_boton7.bottom))

    # Actualizar la pantalla
    pygame.display.flip()


# Salir del juego
pygame.quit()
