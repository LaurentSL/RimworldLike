import pygame
from pygame.event import Event

from lhes.data.player_input import PlayerInput
from lhes.tools.input_framework import InputFramework


class Input(InputFramework):

    def __init__(self, owner: object):
        super().__init__(owner)
        self.set_allowed([pygame.QUIT, pygame.MOUSEMOTION, pygame.MOUSEWHEEL])
        self._player_input = PlayerInput()

    def update(self, deltatime):
        self._reinit()
        super(Input, self).update(deltatime)

    def _on_mouse_wheel(self, event: Event):
        super(Input, self)._on_mouse_wheel(event)
        self._camera_zoom(event.y)

    def _on_mouse_motion(self, event: Event):
        super(Input, self)._on_mouse_motion(event)
        if self.right_button:
            self._camera_move(self.mouse_movement)

    # Game functions

    def _reinit(self):
        self._player_input.camera_move_vector = pygame.Vector2(0, 0)
        self._player_input.camera_zoom_scale = 0

    def _camera_zoom(self, zoom_scale: float):
        self._player_input.camera_zoom_scale = zoom_scale

    def _camera_move(self, offset: tuple[int, int]):
        self._player_input.camera_move_vector = pygame.Vector2(offset)
