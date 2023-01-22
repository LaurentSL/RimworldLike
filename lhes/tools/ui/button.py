import pygame.sprite

import lhes.tools.ui.utils
import lhes.tools.utils
from lhes.game.player_input import PlayerInput


class Button(pygame.sprite.Sprite):

    def __init__(
            self,
            text: str,
            size: tuple[int, int],
            position: tuple[int, int],
            action,
            menu_position: tuple[int, int],
            *groups: pygame.sprite.AbstractGroup
    ):
        super().__init__(*groups)
        self._text = text
        self._action = action
        self._menu_position = menu_position
        self._player_input: PlayerInput = PlayerInput()
        self._size = None
        self._position = None
        self.image = None
        self.rect = None
        self.adjust_size_position(size, position)

    def adjust_size_position(self, size: tuple[int, int], position: tuple[int, int]):
        self._size = size
        self._position = position
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft=self._position)
        print(self.rect)
        self._draw()

    def _draw(self):
        self.image.fill("grey")
        rect = self.image.get_rect()
        pygame.draw.rect(self.image, 'black', rect.inflate(-1, -1), 2)
        pygame.draw.rect(self.image, 'white', rect.inflate(-3, -3), 2)
        lhes.tools.ui.utils.draw_text(self.image, self._text, pygame.font.Font(None, 16), "black", (0, 0), "center")

    def update(self, delta_time) -> None:
        super().update(delta_time)
        if self._player_input.left_button_clicked:
            x = self._player_input.mouse_position[0] - self._menu_position[0]
            y = self._player_input.mouse_position[1] - self._menu_position[1]
            if self.rect.collidepoint(x, y):
                self._on_click()

    def _on_click(self):
        if self._action:
            self._action()
