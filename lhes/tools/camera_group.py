import pygame.sprite

from lhes.game import settings
from lhes.game.player_input import PlayerInput
from lhes.game.world.map_size import MapSize
from lhes.tools import utils


class CameraGroup(pygame.sprite.Group):
    ZOOM_MIN = 0.2
    ZOOM_MAX = 3

    def __init__(self, map_size: MapSize):
        super().__init__()
        self._player_input: PlayerInput = PlayerInput()

        self._camera_position = pygame.Vector2(0, 0)
        self._zoom_scale = 1.0
        self._offset: pygame.Vector2 = pygame.Vector2(0, 0)

        # map surface
        self._map_size = pygame.Vector2(map_size, map_size)
        self._map_pixel_size_vector: pygame.Vector2 = self._map_size * settings.TILE_SIZE
        self._map_surface = pygame.Surface(self._map_pixel_size_vector)

    def custom_draw(
            self,
            surface: pygame.Surface,
            ground_surface: pygame.Surface
    ):
        self._clear(surface)
        self._draw_ground(ground_surface)
        self._draw_y_sorted_sprites()
        scaled_rect, scaled_surf = self._zoom(pygame.Vector2(surface.get_size()) / 2)
        rect = surface.get_rect()
        self._offset.x = (rect.width - scaled_rect.width) // 2
        self._offset.y = (rect.height - scaled_rect.height) // 2
        self._blit_surface(surface, scaled_rect, scaled_surf)

    def _clear(self, surface):
        self._map_surface.fill('black')
        surface.fill('black')

    def _draw_ground(self, ground_surface: pygame.Surface) -> None:
        if ground_surface is None:
            return
        ground_rect = ground_surface.get_rect(topleft=(0, 0))
        ground_offset = pygame.Vector2(ground_rect.topleft) - self._camera_position
        self._map_surface.blit(ground_surface, ground_offset)

    def _draw_y_sorted_sprites(self) -> None:
        for sprite in sorted(self.sprites(), key=lambda sprite_y: sprite_y.rect.centery):
            self._draw_sprite(sprite)

    def _draw_sprite(self, sprite: pygame.sprite.Sprite) -> None:
        self._map_surface.blit(sprite.image, sprite.rect.topleft)

    def _zoom(self, surface_half_size_vector: pygame.Vector2):
        scaled_surf = pygame.transform.scale(self._map_surface,
                                             self._map_pixel_size_vector * self._zoom_scale)
        # scaled_rect = scaled_surf.get_rect(topleft=(0, 0))
        scaled_rect = scaled_surf.get_rect(center=surface_half_size_vector - self._camera_position)
        return scaled_rect, scaled_surf

    def _blit_surface(self, surface: pygame.Surface, scaled_rect: pygame.Rect, scaled_surf: pygame.Surface):
        self._restrict_camera_position(scaled_rect, surface)
        surface.blit(scaled_surf, scaled_rect)

    @staticmethod
    def _restrict_camera_position(scaled_rect, surface):
        rect = surface.get_rect()
        scaled_rect.left = min(rect.left, scaled_rect.left)
        scaled_rect.top = min(rect.top, scaled_rect.top)
        scaled_rect.right = max(rect.right, scaled_rect.right)
        scaled_rect.bottom = max(rect.bottom, scaled_rect.bottom)
        if scaled_rect.width < rect.width:
            scaled_rect.centerx = rect.centerx
        if scaled_rect.height < rect.height:
            scaled_rect.centery = rect.centery

    def camera_update(self, deltatime) -> None:
        self._update_camera_move_vector(deltatime)
        self._update_camera_zoom(deltatime)
        self._on_left_mouse_button_down()

    def _update_camera_move_vector(self, deltatime):
        if self._player_input.camera_move_vector == pygame.Vector2(0, 0):
            return
        self._camera_position -= self._player_input.camera_move_vector * settings.CAMERA_MOVE_SPEED * deltatime

    def _update_camera_zoom(self, deltatime):
        if self._player_input.camera_zoom_scale == 0:
            return
        self._zoom_scale += self._player_input.camera_zoom_scale * settings.CAMERA_ZOOM_SPEED * deltatime
        self._zoom_scale = utils.restrict(self._zoom_scale, self.ZOOM_MIN, self.ZOOM_MAX)

    def _world_to_screen(self, world_position: pygame.Vector2):
        return (world_position - self._camera_position) * self._zoom_scale

    def _screen_to_world(self, screen_position: pygame.Vector2):
        return (screen_position / self._zoom_scale) + self._camera_position

    def _on_left_mouse_button_down(self):
        if not self._player_input.left_button:
            return
        for sprite in self.sprites():
            position = pygame.Vector2(self._player_input.mouse_position) - self._offset
            position = self._screen_to_world(position)
            if sprite.rect.collidepoint(position):
                print("camera_group.on_left_mouse_button_down", self._player_input.mouse_status())
                print(f"camera_group.on_left_mouse_button_down, Offset map vs screen: {self._offset}")
                print(f"camera_group.on_left_mouse_button_down, Position: {position}")
                print(f"camera_group.on_left_mouse_button_down, Sprite rect: {sprite.rect}")
                print(f"camera_group.on_left_mouse_button_down, Sprite: {sprite}")
