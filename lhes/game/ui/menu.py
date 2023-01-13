import pygame

from lhes.game import settings
from lhes.game.ui.button import Button


class Menu:

    def __init__(self, width: int, height: int, *groups):
        self._width = width
        self._height = height
        self._position = (0, settings.SCREEN_HEIGHT - height)
        self._background: pygame.Surface = pygame.Surface((width, height))
        self._rect = self._background.get_rect(topleft=self._position)
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
        width = self._width // nb_buttons
        x = 0
        for sprite in sprites:  # type: Button
            sprite.adjust_size_position((width, self._height), (x, 0))
            x += width
        Button(text, (width, self._height), (x, 0), action, self._position, [self._buttons])
