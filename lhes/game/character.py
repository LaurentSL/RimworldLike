import pygame

from lhes.game.character_data import CharacterData


class Character(pygame.sprite.Sprite):

    def __init__(
            self,
            *groups: pygame.sprite.AbstractGroup
    ):
        super().__init__(groups)
        self._data = CharacterData(name="test",
                                   position=pygame.Vector2(10, 20),
                                   birthdate="25/12/2022",
                                   race="human"
                                   )
        self.image = pygame.Surface((64, 64))
        pygame.draw.circle(self.image, 'black', (32, 32), 30)
        pygame.draw.circle(self.image, 'white', (32, 32), 28)
        pygame.draw.circle(self.image, 'red', (32, 32), 24)
        self.rect = self.image.get_rect()

    def update(self, deltatime: float) -> None:
        super().update()
