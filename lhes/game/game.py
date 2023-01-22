import logging
import logging.config
import sys

import pygame

from lhes.game import settings
from lhes.game.level import Level
from lhes.game.player_input import PlayerInput
from lhes.tools import utils
from lhes.tools.ui.menu import Menu


class Game:
    MENU_HEIGHT = 50

    def __init__(self):
        # Logger
        utils.set_logger()
        logging.info(f"Game is starting (LogLevel is {settings.LOG_LEVEL}")
        # Pygame
        pygame.init()
        self._screen: pygame.Surface = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.SCREEN_TITLE)
        self._clock = pygame.time.Clock()
        # Player input
        self._player_input = PlayerInput()
        # Screen components
        self._rect_map: pygame.Rect = pygame.Rect(
            0, 0, settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT - self.MENU_HEIGHT)
        self._rect_menu: pygame.Rect = pygame.Rect(
            0, settings.SCREEN_HEIGHT - self.MENU_HEIGHT, settings.SCREEN_WIDTH, self.MENU_HEIGHT)
        self._map_surface: pygame.Surface = pygame.Surface(self._rect_map.size)
        self._level = Level(self._rect_map)
        self._menu: Menu = None
        self._init_menu(self._rect_menu)

    def _init_menu(self, rect: pygame.Rect):
        self._menu = Menu(rect)
        self._menu.add_button("Quit", self._on_quit)

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
