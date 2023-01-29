import pygame

from lhes.game.character import Character
from lhes.game.components.input import Input
from lhes.game.player_input import PlayerInput
from lhes.game.world.world import World
from lhes.tools.camera_group import CameraGroup
from lhes.tools.component import Component


class Level:

    def __init__(self, rect: pygame.Rect):
        self._rect = rect
        self._player_input: PlayerInput = PlayerInput()
        # Components
        self._components: list[Component] = []
        self._input = Input(self)
        self._components.append(self._input)
        # world
        self._world = World()
        # Characters
        self._camera_group = CameraGroup(self._rect, self._world.get_current_site_map_size())
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
        self._camera_group.update(deltatime)

    def draw(self, surface: pygame.Surface):
        self._camera_group.custom_draw(surface, self._ground_test)

    def screen_position_to_world_position(self, screen_position: pygame.Vector2):
        return self._camera_group.screen_position_to_world_position(screen_position)

    def screen_position_to_tile_coord(self, screen_position: pygame.Vector2):
        return self._camera_group.screen_position_to_tile_coord(screen_position)

    def world_position_to_tile_coord(self, world_position: pygame.Vector2):
        return self._camera_group.world_position_to_tile_coord(world_position)
