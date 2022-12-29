import logging
import logging.config
import sys

import pygame

from lhes.data.player_input import PlayerInput
from lhes.game import settings
from lhes.game.character import Character
from lhes.game.components.input import Input
from lhes.game.screen import Screen
from lhes.tools.camera_group import CameraGroup
from lhes.tools.component import Component


class Game:

    def __init__(self):
        # Logger
        logging.basicConfig(filename=settings.LOG_FILENAME, level=settings.LOG_LEVEL, format=settings.LOG_FORMAT)
        logging.info("Game is starting")
        # Pygame
        pygame.init()
        self._screen = Screen(settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)
        pygame.display.set_caption(settings.SCREEN_TITLE)
        self._clock = pygame.time.Clock()
        # Components
        self._components: list[Component] = []
        self._input = Input(self)
        self._components.append(self._input)
        self._player_input = PlayerInput()
        # Characters
        self._camera_group = CameraGroup()
        self._all_sprites = pygame.sprite.Group()
        self._characters = pygame.sprite.Group()
        Character([self._all_sprites, self._camera_group, self._characters])

        # TODO: Test to delete
        self._ground_test = pygame.Surface((250, 250))
        self._ground_test.fill('yellow')

    def run(self):
        while not self._player_input.ask_to_exit:
            self._update()
            self._draw()
        self._exit()

    def _update(self):
        deltatime = self._clock.tick(settings.FPS) / 1000
        for component in self._components:
            component.update(deltatime)
        self._all_sprites.update(deltatime)
        self._camera_group.update(deltatime)

    def _draw(self):
        self._screen.clear('black')
        self._camera_group.custom_draw(self._ground_test)
        self._screen.draw()

    @staticmethod
    def _exit():
        logging.info("Game is over")
        pygame.quit()
        sys.exit()
