# Lógica del juego
import pygame, sys, random
from settings import SCREEN, background_color, snake_color, comida_color, menu_music, score_point_sound
from screens import pause_menu, score

def play(): # Play Screen
    pygame.mixer.music.set_volume(0.20)
    sprint_sound = pygame.mixer.Sound("assets/sound/SPRINT.mp3")
    sprint_sound.set_volume(0.15)
    sound_played = False

    # Configuración de la serpiente
    snake_block = 20
    snake_speed = 5
    speed_up = 25  # Para aumentar velocidad cuando se presiona la tecla espacio
    current_speed = snake_speed

    # Inicializar la posición y el cuerpo de la serpiente en el centro
    snake_x = SCREEN.get_width() // 2
    snake_y = SCREEN.get_height() // 2
    snake_body = [[snake_x, snake_y]]
    snake_length = 1

    # Dirección de movimiento
    direction = "UP"
    change_to = direction

    # Inicializar la posición de la comida
    food_x = round(random.randrange(0, SCREEN.get_width() - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, SCREEN.get_height() - snake_block) / 20.0) * 20.0

    # Bucle principal del juego
    clock = pygame.time.Clock()  # Para controlar la velocidad de fotogramas

    paused = False  # Variable para controlar el estado de pausa
    space_pressed = False # Bandera para saber si la tecla espacio está presionada

    while True:
        for event in pygame.event.get(): # Cheking for events
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN: # Buscando evento de presionar una tecla
                if event.key == pygame.K_p or event.key == pygame.K_ESCAPE:
                    # Cambiar entre estado de pausa y reanudar
                    paused = True
                    pygame.mixer.music.set_volume(0.05) # Bajar volumen de musica en menu de pausa
                    sprint_sound.stop()
                    if paused:
                        pause_state = pause_menu()
                        if pause_state == "MAIN_MENU":
                            pygame.mixer.music.stop()
                            menu_music() # Play menu music
                            return "MAIN_MENU"
                        elif pause_state == "RESUME":
                            pygame.mixer.music.set_volume(0.20)
                            paused = False
                            space_pressed = False
                            # Para que se resuma el juego en la posicion exacta antes de pausar
                            pygame.event.get() # Limpiar la cola de eventos para evitar acumulación de entradas
                            clock.tick(0) # Reiniciar el reloj para evitar acumulación de tiempo
                if not paused:  # Solo permitir el cambio de dirección si no está en pausa
                    if event.key == pygame.K_LEFT and direction != "RIGHT":
                        change_to = "LEFT"
                    elif event.key == pygame.K_RIGHT and direction != "LEFT":
                        change_to = "RIGHT"
                    elif event.key == pygame.K_UP and direction != "DOWN":
                        change_to = "UP"
                    elif event.key == pygame.K_DOWN and direction != "UP":
                        change_to = "DOWN"
                    elif event.key == pygame.K_SPACE: # Detectar cuando se presiona la tecla espacio
                        space_pressed = True
            elif event.type == pygame.KEYUP:
                if not paused:
                    if event.key == pygame.K_SPACE: # Detectar cuando se deja de presionar la tecla espacio
                        space_pressed = False

        if paused:
            continue  # Saltar la lógica de movimiento y actualización mientras está en pausa

        # Actualizar la dirección de la serpiente
        direction = change_to

        # Ajustar la velocidad si la tecla espacio está presionada
        if space_pressed:
            snake_speed = speed_up # Aumentar la velocidad
            if speed_up != 71.00000000000016: # Que esto!? que hago con mi vida diabloperodiosmio \('^')/
                speed_up += 0.1
                print(speed_up)
                if speed_up == 71.00000000000016:
                    # Restaurar a velocidad default
                    speed_up = 5
                    # Revertir spacio a no precionado y volumen de musica
                    space_pressed = False
                    pygame.mixer.music.set_volume(0.20)
            if not sound_played: # Evitar que se reproduzca el sonido repetidamente
                sprint_sound.play()
                pygame.mixer.music.set_volume(0.05)
                sound_played = True
        else:
            # Reset las variables
            # Restaurar la velocidad original
            speed_up = 25
            snake_speed = current_speed 
            sound_played = False
            sprint_sound.stop()
            pygame.mixer.music.set_volume(0.20)

        # Mover la serpiente en la dirección actual
        if direction == "UP":
            snake_y -= snake_block
        elif direction == "DOWN":
            snake_y += snake_block
        elif direction == "LEFT":
            snake_x -= snake_block
        elif direction == "RIGHT":
            snake_x += snake_block

        # Añadir la nueva posición de la cabeza al cuerpo de la serpiente
        snake_body.append([snake_x, snake_y])
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Comprobar colisiones con los bordes de la pantalla
        if snake_x < 0 or snake_x >= SCREEN.get_width() or snake_y < 0 or snake_y >= SCREEN.get_height():
            sprint_sound.stop()
            return "GAME_OVER" # Return to Game Over screen

        # Comprobar colisiones con el cuerpo
        for block in snake_body[:-1]:
            if block == [snake_x, snake_y]:
                sprint_sound.stop()
                return "GAME_OVER" # Return to Game Over screen

        # Comprobar si la serpiente ha comido la comida
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, SCREEN.get_width() - snake_block) / 20.0) * 20.0
            food_y = round(random.randrange(0, SCREEN.get_height() - snake_block) / 20.0) * 20.0
            snake_length += 1
            score_point_sound()

        # Dibujar la pantalla de juego
        SCREEN.fill(background_color)
        pygame.draw.rect(SCREEN, comida_color, [food_x, food_y, snake_block, snake_block]) # comida
        for pos in snake_body:
            pygame.draw.rect(SCREEN, snake_color, [pos[0], pos[1], snake_block, snake_block]) # serpiente

        # Dibujar el puntaje
        score(snake_length-1)

        # Actualizar la pantalla
        pygame.display.flip()

        # Control de FPS
        clock.tick(snake_speed)

        # pygame.display.update()
