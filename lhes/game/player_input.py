from dataclasses import dataclass

import pygame

from lhes.tools.singleton_decorator import SingletonDecorator


@SingletonDecorator
@dataclass
class PlayerInput:
    ask_to_exit: bool = False
    # Camera movement
    camera_move_vector: pygame.Vector2 = pygame.Vector2(0, 0)
    camera_zoom_scale: float = 1.0
    # Mouse action
    left_button: bool = False
    middle_button: bool = False
    right_button: bool = False
    mouse_position: tuple[int, int] = (0, 0)
    mouse_movement: tuple[int, int] = (0, 0)

    def mouse_status(self):
        return f"Mouse status: Left: {self.left_button}, Middle: {self.middle_button}, Right: {self.right_button}, " \
               f"position: {self.mouse_position}, movement: {self.mouse_movement}"
