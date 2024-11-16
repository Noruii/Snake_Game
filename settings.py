# Configuración del juego (tamaño de pantalla, colores, etc.)
import pygame

# Configurar la pantalla
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Screen caption
pygame.display.set_caption("Snake Game!")

background_menu = pygame.image.load("assets/img/Background.png")

# Colores
background_color = (0, 0, 0)
comida_color = (255, 0, 0)
snake_color = (0, 255, 0)

def menu_music():
    pygame.mixer.music.load("assets/sound/MENU.mp3")
    pygame.mixer.music.play(-1) # the -1 is just so the song starts to play again, if it finished

def hover_button_sound():
    return pygame.mixer.Sound("assets/sound/HOVER.mp3")

def click_button_sound():
    click = pygame.mixer.Sound("assets/sound/CLICK.mp3")
    click.play()
    click.set_volume(0.40)

def goback_button_sound():
    goback = pygame.mixer.Sound("assets/sound/BACK.mp3")
    goback.play()
    goback.set_volume(0.50)

def score_point_sound():
    score = pygame.mixer.Sound("assets/sound/POINT.mp3")
    score.play()
    score.set_volume(0.40)

def get_font(size): # Returns font in the desired size
    return pygame.font.Font("assets/font.ttf", size)