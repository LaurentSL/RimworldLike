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
