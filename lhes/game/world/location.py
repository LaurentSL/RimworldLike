import pygame

import lhes.tools.utils
from lhes.game import settings
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
        self._draw_location_for_test()

    def _draw_location_for_test(self):
        self.image.fill(self._terrain.get_color())
        rect = self.image.get_rect()
        pygame.draw.rect(self.image, 'black', rect, 1)
        pygame.draw.rect(self.image, 'white', rect.inflate(-2, -2), 1)
        pygame.draw.rect(self.image, 'red', rect.inflate(-4, -4), 1)
        lhes.tools.utils.draw_text(self.image, self.position, pygame.font.Font(None, 16), "black", (0, 0), "center")
