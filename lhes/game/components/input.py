import pygame

from lhes.game.components.component import Component


class Input(Component):

    def __init__(self, owner: object):
        super().__init__(owner)
        self.ask_to_exit = False

    def update(self, deltatime):
        super(Input, self).update(deltatime)
        for event in pygame.event.get():
            self._exit(event)

    def _exit(self, event):
        if event.type == pygame.QUIT:
            self.ask_to_exit = True
