import pygame.sprite

from lhes.game import settings
from lhes.game.player_input import PlayerInput
from lhes.game.world.map_size import MapSize
from lhes.tools import utils
from lhes.tools.camera import Camera


class CameraGroup(pygame.sprite.Group):

    def __init__(self, display_rect: pygame.Rect, map_size: MapSize):
        super().__init__()

        # display rect
        self._display_rect = display_rect.copy()

        # map surface
        self._map_size = pygame.Vector2(map_size, map_size)
        self._map_pixel_size_vector: pygame.Vector2 = self._map_size * settings.TILE_SIZE
        self._map_surface = pygame.Surface(self._map_pixel_size_vector)
        self._map_rect = self._map_surface.get_rect()

        self._camera = Camera(self._display_rect, self._map_rect)
        # self._offset: pygame.Vector2 = pygame.Vector2(0, 0)
        self._player_input: PlayerInput = PlayerInput()

    def __str__(self):
        return f"CameraGroup - {self._camera}, " \
               f"Map - size: {self._map_size}, pixel size: {self._map_pixel_size_vector}"
        # f"offset map vs screen: {self._offset} ; " \

    def custom_draw(
            self,
            surface: pygame.Surface,
            ground_surface: pygame.Surface
    ):
        self._clear(surface)
        # self._draw_ground(ground_surface)
        self._draw_y_sorted_sprites()
        scaled_surf = self._zoom()
        # rect = surface.get_rect()
        # self._offset.x = (rect.width - scaled_rect.width) // 2
        # self._offset.y = (rect.height - scaled_rect.height) // 2
        self._blit_surface(surface, scaled_surf)

    def _clear(self, surface):
        self._map_surface.fill('black')
        surface.fill('black')

    # def _draw_ground(self, ground_surface: pygame.Surface) -> None:
    #     if ground_surface is None:
    #         return
    # ground_rect = ground_surface.get_rect(topleft=(0, 0))
    # ground_offset = pygame.Vector2(ground_rect.topleft) - self._camera.position
    # self._map_surface.blit(ground_surface, ground_offset)

    def _draw_y_sorted_sprites(self) -> None:
        for sprite in sorted(self.sprites(), key=lambda sprite_y: sprite_y.rect.centery):
            self._draw_sprite(sprite)

    def _draw_sprite(self, sprite: pygame.sprite.Sprite) -> None:
        self._map_surface.blit(sprite.image, sprite.rect.topleft)

    def _zoom(self):
        return pygame.transform.scale(self._map_surface, self._map_pixel_size_vector * self._camera.zoom_scale)

    def _blit_surface(self, display_surface: pygame.Surface, scaled_surf: pygame.Surface):
        position = -self._camera.position[0], -self._camera.position[1]
        display_surface.blit(scaled_surf, position)

    def update(self, deltatime) -> None:
        self._camera.update(deltatime)
        self._on_left_mouse_button_down()

    def _on_left_mouse_button_down(self):
        if not self._player_input.left_button_clicked:
            return
        if not self._display_rect.collidepoint(self._player_input.mouse_position):
            return
        sprite_coord = self.screen_position_to_tile_coord(self._player_input.mouse_position_as_vector2)

    def screen_position_to_world_position(self, screen_position: pygame.Vector2):
        return self._camera.screen_to_world(screen_position)

    def screen_position_to_tile_coord(self, screen_position: pygame.Vector2):
        world_position = self.screen_position_to_world_position(screen_position)
        return self.world_position_to_tile_coord(world_position)

    @staticmethod
    def world_position_to_tile_coord(world_position: pygame.Vector2):
        return utils.floor_vector2(world_position / settings.TILE_SIZE)
