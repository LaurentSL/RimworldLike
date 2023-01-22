import pygame

from lhes.tools.ui.button import Button


class Menu:

    def __init__(self, rect: pygame.Rect):
        self._rect: pygame.Rect = rect
        self._background: pygame.Surface = pygame.Surface(self._rect.size)
        self._buttons: pygame.sprite.Group = pygame.sprite.Group()

    def update(self, delta_time):
        self._buttons.update(delta_time)

    def draw(self, display_surface: pygame.Surface):
        self._background.fill('dark grey')
        self._buttons.draw(self._background)
        display_surface.blit(self._background, self._rect)

    def add_button(self, text, action):
        sprites = self._buttons.sprites()
        nb_buttons = len(sprites) + 1
        width = self._rect.width // nb_buttons
        x = 0
        for sprite in sprites:  # type: Button
            sprite.adjust_size_position((width, self._rect.height), (x, 0))
            x += width
        Button(text, (width, self._rect.height), (x, 0), action, self._rect.topleft, [self._buttons])
