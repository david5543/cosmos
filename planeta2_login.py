import pygame
import subprocess

# Dimensiones de la ventana
WIDTH = 800
HEIGHT = 600

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Cargar la imagen de fondo
background_image = pygame.image.load("images/LUCHITO.png").convert()

# Cargar el texto
font = pygame.font.Font(None, 36)
text = font.render("INSTRUCCIÓN: PRESIONA ESPACIO PARA ELEVAR LA NAVE", True, (255, 255, 255))
text1 = font.render("DA CLICK PARA CONTINUAR", True, (255, 255, 255))
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
text_rect1 = text1.get_rect(center=(WIDTH // 2, HEIGHT // 2))

# Función para abrir otro archivo .py
def open_file():
    subprocess.Popen(["python", "planeta2.py"])
    pygame.quit()
# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            open_file()

    # Dibujar la imagen de fondo en la pantalla
    screen.blit(background_image, (0, 0))

    # Dibujar el texto en el centro de la pantalla
    screen.blit(text, text_rect)
    screen.blit(text1, text_rect1)

    # Actualizar la pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()
