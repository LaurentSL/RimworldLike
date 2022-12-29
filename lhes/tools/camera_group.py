from typing import Union, Sequence

import pygame.sprite

from lhes.data.player_input import PlayerInput
from lhes.game import settings


class CameraGroup(pygame.sprite.Group):

    def __init__(
            self,
            *sprites: Union[pygame.sprite.Sprite, Sequence[pygame.sprite.Sprite]]
    ):
        super().__init__(*sprites)
        self._player_input: PlayerInput = PlayerInput()

        self._camera_position = pygame.Vector2(0, 0)

        # display surface
        self._display_surface = pygame.display.get_surface()
        self._screen_width = self._display_surface.get_size()[0]
        self._screen_height = self._display_surface.get_size()[1]
        self._screen_size = self._display_surface.get_size()
        self._screen_size_vector = pygame.Vector2(self._screen_size)
        self._half_width = self._screen_width // 2
        self._half_height = self._screen_height // 2
        self._screen_half_size_vector = self._screen_size_vector // 2

        # internal surface
        self._internal_surf = self._display_surface.copy()
        self._internal_rect = self._internal_surf.get_rect(center=(self._half_width, self._half_height))
        self._internal_size_vector = pygame.Vector2(self._internal_surf.get_size())
        self._internal_offset_vector = self._internal_size_vector // 2 - self._screen_half_size_vector

        # zoom
        self._zoom_scale = 1.0

    def custom_draw(
            self,
            ground_surface: pygame.Surface
    ):
        self._clear()
        self._draw_ground(ground_surface)
        self._draw_y_sorted_sprites()
        scaled_rect, scaled_surf = self._zoom()
        self._blit_surface(scaled_rect, scaled_surf)

    def _clear(self):
        self._internal_surf.fill('black')

    def _draw_ground(self, ground_surface):
        if ground_surface is None:
            return
        ground_rect = ground_surface.get_rect(topleft=(0, 0))
        ground_offset = pygame.Vector2(ground_rect.topleft) - self._camera_position + self._internal_offset_vector
        self._internal_surf.blit(ground_surface, ground_offset)

    def _draw_y_sorted_sprites(self):
        for sprite in sorted(self.sprites(), key=lambda sprite_y: sprite_y.rect.centery):
            self._draw_sprite(sprite)

    def _draw_sprite(self, sprite):
        offset_position = pygame.Vector2(sprite.rect.topleft) - self._camera_position + \
                          self._internal_offset_vector  # - self._screen_half_size_vector
        self._internal_surf.blit(sprite.image, offset_position)

    def _zoom(self):
        scaled_surf = pygame.transform.scale(self._internal_surf, self._screen_size_vector * self._zoom_scale)
        scaled_rect = scaled_surf.get_rect(center=self._screen_half_size_vector)
        return scaled_rect, scaled_surf

    def _blit_surface(self, scaled_rect, scaled_surf):
        self._display_surface.blit(scaled_surf, scaled_rect)

    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
        if self._player_input.camera_move_vector != pygame.Vector2(0, 0):
            deltatime = args[0]
            self._camera_position -= self._player_input.camera_move_vector * settings.CAMERA_MOVE_SPEED * deltatime
        if self._player_input.camera_zoom_scale != 0:
            deltatime = args[0]
            self._zoom_scale += self._player_input.camera_zoom_scale * settings.CAMERA_ZOOM_SPEED * deltatime
            self._zoom_scale = max(self._zoom_scale, 0.2)
            self._zoom_scale = min(self._zoom_scale, 3)
