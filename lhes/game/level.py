import pygame

from lhes.game.character import Character
from lhes.game.components.input import Input
from lhes.game.player_input import PlayerInput
from lhes.game.world.world import World
from lhes.tools.camera_group import CameraGroup
from lhes.tools.component import Component


class Level:

    def __init__(self):
        # Components
        self._components: list[Component] = []
        self._input = Input(self)
        self._components.append(self._input)
        self._player_input: PlayerInput = PlayerInput()
        # world
        self._world = World()
        # Characters
        self._camera_group = CameraGroup(self._world.get_current_site_map_size())
        self._all_sprites = pygame.sprite.Group()
        self._characters = pygame.sprite.Group()
        self._all_sprites.add(self._world.get_location_group())
        self._camera_group.add(self._world.get_location_group())

        # TODO: Test to delete
        Character([self._all_sprites, self._camera_group, self._characters])
        self._ground_test = pygame.Surface((250, 250))
        self._ground_test.fill('yellow')

    def update(self, deltatime):
        for component in self._components:
            component.update(deltatime)
        self._all_sprites.update(deltatime)
        self._camera_group.camera_update(deltatime)

    def draw(self, surface: pygame.Surface):
        self._camera_group.custom_draw(surface, self._ground_test)
