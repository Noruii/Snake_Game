# Pantallas (menú, opciones)
import pygame, sys
from settings import SCREEN, get_font, background_menu, hover_button_sound, click_button_sound, goback_button_sound
from button import Button

def main_menu(): # Main menu Screen
    pygame.mixer.music.set_volume(0.20)

    play_button = Button(image=pygame.image.load("assets/img/Play Rect.png").convert_alpha(), 
                        pos=(SCREEN.get_width() // 2, 250), 
                        text_input="PLAY", 
                        font=get_font(75),
                        base_color="#d7fcd4",
                        hovering_color="Green",
                        hover_sound=hover_button_sound())
    options_button = Button(image=pygame.image.load("assets/img/Options Rect.png").convert_alpha(),
                        pos=(SCREEN.get_width() // 2, 400), 
                        text_input="OPTIONS",
                        font=get_font(75),
                        base_color="#d7fcd4",
                        hovering_color="Green",
                        hover_sound=hover_button_sound())
    quit_button = Button(image=pygame.image.load("assets/img/Quit Rect.png").convert_alpha(),
                        pos=(SCREEN.get_width() // 2, 550), 
                        text_input="QUIT",
                        font=get_font(75),
                        base_color="#d7fcd4",
                        hovering_color="Green",
                        hover_sound=hover_button_sound())

    while True:
        SCREEN.blit(background_menu, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("SNAKE GAME", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(SCREEN.get_width() // 2, 100))
        SCREEN.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    pygame.mixer.music.load("assets/sound/PLAY.mp3")
                    pygame.mixer.music.play(-1) # the -1 is just so the song starts to play again, if it finished
                    click_button_sound()
                    return "PLAY"
                elif options_button.checkForInput(menu_mouse_pos):
                    click_button_sound()
                    return "OPTIONS"
                elif quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def options(): # Options Screen
    options_back = Button(image=pygame.image.load("assets/img/Quit Rect.png").convert_alpha(), 
                        pos=(SCREEN.get_width() // 2, 460),
                        text_input="BACK", 
                        font=get_font(75), 
                        base_color="Black", 
                        hovering_color="Green",
                        hover_sound=hover_button_sound())
    while True:
        options_mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill("white") # Cubrir pantalla con color para cubrir el background anterior y dar la ilucion de nueva pantalla

        options_text = get_font(30).render("Hold [SPACE] to sprint", True, "Black")
        options_rect = options_text.get_rect(center=(SCREEN.get_width() // 2, 260))
        SCREEN.blit(options_text, options_rect)

        options_text2 = get_font(30).render("Press [ESC] or [P] to Pause", True, "Black")
        options_rect2 = options_text2.get_rect(center=(SCREEN.get_width() // 2, 330))
        SCREEN.blit(options_text2, options_rect2)

        options_back.changeColor(options_mouse_pos)
        options_back.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if options_back.checkForInput(options_mouse_pos):
                    goback_button_sound()
                    return "MAIN_MENU"

        pygame.display.update()

def pause_menu(): # Pause Screen
    resume_button = Button(image=None, 
                        pos=(SCREEN.get_width() // 2, 460), 
                        text_input="Resume", 
                        font=get_font(50), 
                        base_color="White", 
                        hovering_color="Green",
                        hover_sound=hover_button_sound())
    menu_button = Button(image=None, 
                        pos=(SCREEN.get_width() // 2, 550), 
                        text_input="Menu", 
                        font=get_font(40), 
                        base_color="White", 
                        hovering_color="Green",
                        hover_sound=hover_button_sound())
    while True:
        pause_mouse_pos = pygame.mouse.get_pos()
        
        # SCREEN.fill((50, 50, 50))  # Fondo gris oscuro para el menú de pausa
        
        # Texto de pausa
        pause_text = get_font(100).render("PAUSED", True, "#b68f40")
        pause_rect = pause_text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2.7))
        SCREEN.blit(pause_text, pause_rect)

        # Mostrar y actualizar los botones
        for button in [resume_button, menu_button]:
            button.changeColor(pause_mouse_pos)
            button.update(SCREEN)

        # Detectar eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.checkForInput(pause_mouse_pos):
                    return "RESUME"
                if menu_button.checkForInput(pause_mouse_pos):
                    goback_button_sound()
                    return "MAIN_MENU"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_p:
                    return "RESUME"  # Retomar el juego con la tecla "p" o "Esc"

        pygame.display.update()