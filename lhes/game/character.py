import pygame

from lhes.game import settings
from lhes.game.character_data import CharacterData
from lhes.game.character_movement import CharacterMovement


class Character(pygame.sprite.Sprite):

    def __init__(
            self,
            grid_position: pygame.Vector2,
            *groups: pygame.sprite.AbstractGroup
    ):
        super().__init__(groups)
        self.data = CharacterData(name="test",
                                  position=grid_position,
                                  birthdate="25/12/2022",
                                  race="human"
                                  )
        self._init_graphics()
        self.position = grid_position * settings.TILE_SIZE
        # Components
        self._component_movement = CharacterMovement(self)

    def _init_graphics(self):
        self.image = pygame.Surface((64, 64))
        pygame.draw.circle(self.image, 'black', (32, 32), 30)
        pygame.draw.circle(self.image, 'white', (32, 32), 28)
        pygame.draw.circle(self.image, 'red', (32, 32), 24)
        self.rect = self.image.get_rect()

    @property
    def position(self) -> pygame.Vector2:
        return pygame.Vector2(self.rect.topleft)

    @position.setter
    def position(self, value: pygame.Vector2) -> None:
        self.rect.topleft = value

    def update(self, deltatime: float) -> None:
        super().update()
        self._component_movement.update(deltatime)

    def move_to(self, destination):
        self._component_movement.move_to(destination)
