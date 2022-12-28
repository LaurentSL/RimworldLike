import logging
import logging.config
import sys

import pygame

from lhes.game import settings
from lhes.game.components.component import Component
from lhes.game.components.input import Input
from lhes.game.screen import Screen


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

    def run(self):
        while not self._input.ask_to_exit:
            self._update()
            self._draw()
            self._fps()
        self._exit()

    def _update(self):
        deltatime = self._clock.tick() / 1000
        for component in self._components:
            component.update(deltatime)

    def _draw(self):
        self._screen.clear('black')
        # player_position = self.player.position
        # camera_offset = self.screen.get_camera_offset(player_position)
        # self.level.draw(self.screen.display_surface, camera_offset)
        # self.ui.draw(self.player)
        # self.screen.debug_draw(player_position, self.level.visible_sprites)
        self._screen.draw()

    def _fps(self):
        self._clock.tick(settings.FPS)

    @staticmethod
    def _exit():
        logging.info("Game is over")
        pygame.quit()
        sys.exit()
