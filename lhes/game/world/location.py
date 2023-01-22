import pygame

import lhes.tools.ui.utils
import lhes.tools.utils
from lhes.game import settings
from lhes.game.player_input import PlayerInput
from lhes.game.world.terrain import Terrain


class Location(pygame.sprite.Sprite):

    def __init__(
            self,
            groups: pygame.sprite.AbstractGroup,
            position: pygame.Vector2,
            terrain: Terrain
    ):
        super().__init__(groups)
        self.position: pygame.Vector2 = position
        self.image = pygame.Surface((settings.TILE_SIZE, settings.TILE_SIZE))
        self.rect = self.image.get_rect(topleft=self.position * settings.TILE_SIZE)
        self._terrain: Terrain = terrain
        self._player_input: PlayerInput = PlayerInput()
        self._draw_location_for_test()

    def __str__(self):
        return f"Location({self.position}) with terrain: {self._terrain}"

    def update(self, delta_time) -> None:
        super(Location, self).update(delta_time)
        self._on_left_mouse_button_down()

    def _draw_location_for_test(self):
        self.image.fill(self._terrain.get_color())
        rect = self.image.get_rect()
        pygame.draw.rect(self.image, 'black', rect, 1)
        pygame.draw.rect(self.image, 'white', rect.inflate(-2, -2), 1)
        pygame.draw.rect(self.image, 'red', rect.inflate(-4, -4), 1)
        lhes.tools.ui.utils.draw_text(self.image, self.position, pygame.font.Font(None, 16), "black", (0, 0), "center")

    def _on_left_mouse_button_down(self):
        if not self._player_input.left_button_clicked:
            return
        if not self.rect.collidepoint(self._player_input.mouse_position):
            return
        # print("location.on_left_mouse_button_down", self._player_input.mouse_status())
        # print("location.on_left_mouse_button_down", self.rect)
        # print("location.on_left_mouse_button_down", f"Click on {self}")
