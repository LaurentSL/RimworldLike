import pygame

from lhes.game import settings


class CharacterMovement:

    def __init__(self, character):
        self._character = character
        self._destination: pygame.Vector2 = None
        self._speed = settings.CHARACTER_MOVE_SPEED

    @property
    def position(self) -> pygame.Vector2:
        return self._character.position

    @position.setter
    def position(self, value: pygame.Vector2) -> None:
        self._character.position = value

    def update(self, deltatime):
        self.move(deltatime)

    def move_to(self, destination: pygame.Vector2):
        self._destination = destination

    def move(self, deltatime):
        if self._destination is None:
            return
        direction = (self._destination - self.position).normalize()
        self.position += direction * self._speed * deltatime
        if self._destination.distance_to(self.position) <= settings.CHARACTER_MOVE_PROXIMITY:
            self.position = self._destination
            self._destination = None
