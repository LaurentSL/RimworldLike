import pygame

from lhes.game import settings
from lhes.game.player_input import PlayerInput
from lhes.tools import utils


class Camera:
    ZOOM_MIN = 0.2
    ZOOM_MAX = 3

    def __init__(self, camera_rect: pygame.Rect, restriction_rect: pygame.Rect):
        self._camera_rect: pygame.Rect = camera_rect
        self._restriction_rect: pygame.Rect = restriction_rect
        self._restriction_zoom_rect: pygame.Rect = restriction_rect.copy()
        self._zoom_scale: float = 1.0
        self._restrict_position()
        self._player_input: PlayerInput = PlayerInput()

    def __str__(self):
        return f"Camera - rect: {self._camera_rect}, position: {self.position}, zoom scale: {self._zoom_scale}"

    @property
    def position(self):
        return self._camera_rect.topleft

    @position.setter
    def position(self, value):
        self._camera_rect.topleft = value

    @property
    def zoom_scale(self):
        return self._zoom_scale

    def update(self, deltatime):
        self._update_camera_move_vector(deltatime)
        self._update_camera_zoom(deltatime)

    def _update_camera_move_vector(self, deltatime):
        if self._player_input.camera_move_vector == pygame.Vector2(0, 0):
            return
        movement = -self._player_input.camera_move_vector * settings.CAMERA_MOVE_SPEED * deltatime
        self._camera_rect.move_ip(movement)
        self._restrict_position()

    def _restrict_position(self):
        self._camera_rect.clamp_ip(self._restriction_zoom_rect)

    def _update_camera_zoom(self, deltatime):
        if self._player_input.camera_zoom_scale == 0:
            return
        old_screen_mouse_position = pygame.Vector2(self._player_input.mouse_position)
        world_mouse_position = self.screen_to_world(old_screen_mouse_position)
        self._zoom_scale += self._player_input.camera_zoom_scale * settings.CAMERA_ZOOM_SPEED * deltatime
        self._zoom_scale = utils.restrict(self._zoom_scale, self.ZOOM_MIN, self.ZOOM_MAX)
        self._adjust_restriction_rect()
        new_screen_mouse_position = self.world_to_screen(world_mouse_position)
        delta = (new_screen_mouse_position - old_screen_mouse_position) * self._zoom_scale
        self._camera_rect.move_ip(delta)
        self._restrict_position()

    def _adjust_restriction_rect(self):
        self._restriction_zoom_rect.width = self._restriction_rect.width * self._zoom_scale
        self._restriction_zoom_rect.height = self._restriction_rect.height * self._zoom_scale

    def world_to_screen(self, world_position: pygame.Vector2) -> pygame.Vector2:
        return (world_position - self.position) * self.zoom_scale

    def screen_to_world(self, screen_position: pygame.Vector2) -> pygame.Vector2:
        return (screen_position / self.zoom_scale) + self.position
