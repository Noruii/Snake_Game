class Button():
    # Inicializar las propiedades
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, hover_sound=None):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.hover_sound = hover_sound  # Sonido de "hover"
        self.is_hovering = False  # Bandera para rastrear si el puntero está sobre el botón

    # Método para actualizar la pantalla
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    # Checkar si se hizo click
    def checkForInput(self, position):
        # Este método es más preciso y eficiente para detectar si el puntero está en el botón
        if self.rect.collidepoint(position):
            return True
        return False

    # Checkar si se está haciendo "hover" sobre el botón para cambiar color y reproducir sonido
    def changeColor(self, position):
        if self.rect.collidepoint(position):  # Verificar si el puntero está dentro del botón
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            # Reproducir el sonido solo una vez al entrar en el estado de "hover"
            if not self.is_hovering and self.hover_sound:
                self.hover_sound.play()
            self.is_hovering = True  # Actualizar la bandera de "hover"
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
            self.is_hovering = False  # Resetear bandera cuando el puntero salga del botón
