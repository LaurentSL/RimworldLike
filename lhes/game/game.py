import logging
import logging.config
import sys

import pygame

from lhes.game import settings
from lhes.game.level import Level
from lhes.game.player_input import PlayerInput
from lhes.game.ui.menu import Menu
from lhes.tools import utils


class Game:

    def __init__(self):
        # Logger
        utils.set_logger()
        logging.info(f"Game is starting (LogLevel is {settings.LOG_LEVEL}")
        # Pygame
        pygame.init()
        self._screen: pygame.Surface = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        size = (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT - 50)
        self._map_surface: pygame.Surface = pygame.Surface(size)
        self._menu = Menu(settings.SCREEN_WIDTH, 50)
        self._menu.add_button("Quit1", self._on_quit)
        self._menu.add_button("Quit 2", self._on_quit)
        self._menu.add_button("Test", None)
        pygame.display.set_caption(settings.SCREEN_TITLE)
        self._clock = pygame.time.Clock()
        # Player input
        self._player_input = PlayerInput()
        # Level
        self._level = Level()

    def run(self):
        while not self._player_input.ask_to_exit:
            self._update()
            self._draw()
        self._exit()

    def _update(self):
        deltatime = self._clock.tick(settings.FPS) / 1000
        pygame.display.set_caption(f"{settings.SCREEN_TITLE} - {round(self._clock.get_fps())} FPS")
        self._level.update(deltatime)
        self._menu.update(deltatime)

    def _draw(self):
        self._screen.fill('black')
        self._level.draw(self._map_surface)
        self._screen.blit(self._map_surface, (0, 0))
        self._menu.draw(self._screen)
        pygame.display.update()

    @staticmethod
    def _exit():
        logging.info("Game is over")
        pygame.quit()
        sys.exit()

    def _on_quit(self):
        self._player_input.ask_to_exit = True
