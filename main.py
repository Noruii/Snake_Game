# Archivo principal que ejecuta el juego
import pygame
from screens import main_menu, game_over, options
from snake_game import play
from settings import menu_music

# sonidos
pygame.mixer.pre_init(44100, -16, 2, 2048) # (frequency, size, channels, buffer)

# Iniciar pygame
pygame.init()

# sonidos *esta dando mal audio .pre_init() lo arreglo...
# pygame.mixer.init() # (frequency, size, channels, buffer)

# Sistema de estados de juego
# Para evitar importaciones circulares
def run_game():
    # Estado predeterminado
    state = "MAIN_MENU"
    # Musica menu principal
    menu_music()

    while True:
        if state == "MAIN_MENU":
            state = main_menu()

        elif state == "PLAY" or state == "RESUME":
            state = play()

        elif state == "OPTIONS":
            state = options()

        elif state == "GAME_OVER":
            state = game_over()

if __name__ == "__main__":
    run_game()