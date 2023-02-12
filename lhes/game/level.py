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
        self._selected_character: Character = None
        self._create_character(pygame.Vector2(3, 3))
        self._ground_test = pygame.Surface((250, 250))
        self._ground_test.fill('yellow')

    def update(self, deltatime):
        for component in self._components:
            component.update(deltatime)
        self._all_sprites.update(deltatime)
        self._camera_group.update(deltatime)
        self._on_left_mouse_button_down()

    def draw(self, surface: pygame.Surface):
        self._camera_group.custom_draw(surface, self._ground_test)

    def screen_position_to_world_position(self, screen_position: pygame.Vector2) -> pygame.Vector2:
        return self._camera_group.screen_position_to_world_position(screen_position)

    def screen_position_to_tile_coord(self, screen_position: pygame.Vector2) -> pygame.Vector2:
        return self._camera_group.screen_position_to_tile_coord(screen_position)

    def world_position_to_tile_coord(self, world_position: pygame.Vector2) -> pygame.Vector2:
        return self._camera_group.world_position_to_tile_coord(world_position)

    def tile_coord_to_world_position(self, tile_coord: pygame.Vector2) -> pygame.Vector2:
        return self._camera_group.tile_coord_to_world_position(tile_coord)

    def _on_left_mouse_button_down(self):
        if not self._player_input.left_button_clicked:
            return
        if not self._rect.collidepoint(self._player_input.mouse_position):
            return
        sprite_coord = self.screen_position_to_tile_coord(self._player_input.mouse_position_as_vector2)
        selected_character = self.get_character_from_tile_coord(sprite_coord)
        if self._selected_character is not None and selected_character is None:
            self.move_character_to(self.tile_coord_to_world_position(sprite_coord))
        else:
            self._selected_character = selected_character

    def _create_character(self, position: pygame.Vector2):
        character = Character(position, [self._all_sprites, self._camera_group, self._characters])

    def move_character_to(self, destination: pygame.Vector2) -> None:
        self._selected_character.move_to(destination)

    def get_character_from_tile_coord(self, tile_coord: pygame.Vector2) -> Character:
        for character in self._characters:  # type: Character
            character_tile_coord = self.world_position_to_tile_coord(character.position)
            if tile_coord == character_tile_coord:
                return character
