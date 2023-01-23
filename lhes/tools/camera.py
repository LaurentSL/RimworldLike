import pygame

from lhes.game import settings
from lhes.game.player_input import PlayerInput
from lhes.tools import utils


class Camera:
    ZOOM_MIN = 0.2
    ZOOM_MAX = 3

    def __init__(self, surface_rect):
        self._surface_rect = surface_rect
        self._camera_position = pygame.Vector2(self._surface_rect.center)
        self._zoom_scale = 1.0
        self._player_input = PlayerInput()

    def __str__(self):
        return f"Camera - position: {self._camera_position}, zoom scale: {self._zoom_scale}"

    @property
    def position(self):
        return self._camera_position

    @property
    def zoom_scale(self):
        return self._zoom_scale

    def update(self, deltatime):
        self._update_camera_move_vector(deltatime)
        self._update_camera_zoom(deltatime)

    def _update_camera_move_vector(self, deltatime):
        if self._player_input.camera_move_vector == pygame.Vector2(0, 0):
            return
        self._camera_position -= self._player_input.camera_move_vector * settings.CAMERA_MOVE_SPEED * deltatime
        # self._display_rect.center = self._camera_position
        print(f"Before - Camera position: {self._camera_position}, display rect= {self._surface_rect}")
        # self._display_rect = self._display_rect.clamp(self._map_rect)
        print(f"After - Camera position: {self._camera_position}, display rect= {self._surface_rect}")

    def _update_camera_zoom(self, deltatime):
        if self._player_input.camera_zoom_scale == 0:
            return
        self._zoom_scale += self._player_input.camera_zoom_scale * settings.CAMERA_ZOOM_SPEED * deltatime
        self._zoom_scale = utils.restrict(self._zoom_scale, self.ZOOM_MIN, self.ZOOM_MAX)

    def world_to_screen(self, world_position: pygame.Vector2):
        return (world_position - self.position) * self.zoom_scale

    def screen_to_world(self, screen_position: pygame.Vector2):
        return (screen_position / self.zoom_scale) + self.position
