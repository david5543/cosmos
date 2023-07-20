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

# Cargar las imágenes de los botones
button1_image = pygame.image.load("images/planetas/universo.png").convert_alpha()
button2_image = pygame.image.load("images/astro.png").convert_alpha()
button3_image = pygame.image.load("images/instru.png").convert_alpha()
button4_image = pygame.image.load("images/salir.png").convert_alpha()

# Escalar las imágenes de los botones al tamaño deseado
button_width = 100
button_height = 100
button1_image = pygame.transform.scale(button1_image, (button_width, button_height))
button2_image = pygame.transform.scale(button2_image, (button_width, button_height))
button3_image = pygame.transform.scale(button3_image, (button_width, button_height))
button4_image = pygame.transform.scale(button4_image, (button_width, button_height))

# Posiciones de los botones
button1_pos = (350, HEIGHT // 2 - button_height // 2)
button2_pos = (350, HEIGHT // 2 + button_height)
button3_pos = (WIDTH - button_width - 100, HEIGHT // 2 - button_height // 2)
button4_pos = (WIDTH - button_width - 100, HEIGHT // 2 + button_height)

# Título centrado en la parte superior
def draw_title():
    font = pygame.font.Font(None, 50)
    title_text = font.render("APRENDIENDO CON LOS COSMOS", True, (255, 255, 255))
    title_rect = title_text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(title_text, title_rect)

# Texto de los botones
button1_text = "Juego de Memoria"
button2_text = "Juego de Concentración"
button3_text = "Instruciones"
button4_text = "Salir"

# Funciones de apertura de archivos
def open_file_1():
    subprocess.Popen(["python", "memory_niveles.py"])
    pygame.quit()
def open_file_2():
    subprocess.Popen(["python", "planeta2_login.py"])
    pygame.quit()
def open_file_3():
    subprocess.Popen(["python", "instruciones.py"])
    pygame.quit()
def open_file_4():
    pygame.quit()
    quit()
# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si se hizo clic en alguno de los botones
            if button1_rect.collidepoint(event.pos):
                open_file_1()
            elif button2_rect.collidepoint(event.pos):
                open_file_2()
            elif button3_rect.collidepoint(event.pos):
                open_file_3()
            elif button4_rect.collidepoint(event.pos):
                open_file_4()

    # Dibujar la imagen de fondo en la pantalla
    screen.blit(background_image, (0, 0))

    # Dibujar el título
    draw_title()

    # Dibujar los botones en la pantalla
    screen.blit(button1_image, button1_pos)
    screen.blit(button2_image, button2_pos)
    screen.blit(button3_image, button3_pos)
    screen.blit(button4_image, button4_pos)

    # Dibujar el texto de los botones
    font = pygame.font.Font(None, 24)

    button1_text_surface = font.render(button1_text, True, (255, 255, 255))
    button1_text_rect = button1_text_surface.get_rect(center=(button1_pos[0] + button_width // 2, button1_pos[1] + button_height + 20))
    screen.blit(button1_text_surface, button1_text_rect)

    button2_text_surface = font.render(button2_text, True, (255, 255, 255))
    button2_text_rect = button2_text_surface.get_rect(center=(button2_pos[0] + button_width // 2, button2_pos[1] + button_height + 20))
    screen.blit(button2_text_surface, button2_text_rect)

    button3_text_surface = font.render(button3_text, True, (255, 255, 255))
    button3_text_rect = button3_text_surface.get_rect(center=(button3_pos[0] + button_width // 2, button3_pos[1] + button_height + 20))
    screen.blit(button3_text_surface, button3_text_rect)

    button4_text_surface = font.render(button4_text, True, (255, 255, 255))
    button4_text_rect = button4_text_surface.get_rect(center=(button4_pos[0] + button_width // 2, button4_pos[1] + button_height + 20))
    screen.blit(button4_text_surface, button4_text_rect)

    # Crear rectángulos de colisión para los botones
    button1_rect = pygame.Rect(button1_pos, (button_width, button_height))
    button2_rect = pygame.Rect(button2_pos, (button_width, button_height))
    button3_rect = pygame.Rect(button3_pos, (button_width, button_height))
    button4_rect = pygame.Rect(button4_pos, (button_width, button_height))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir del juego
pygame.quit()
