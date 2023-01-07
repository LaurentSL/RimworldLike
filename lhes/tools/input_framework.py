import logging

import pygame
from pygame.event import Event

from lhes.game.player_input import PlayerInput
from lhes.tools.component import Component


class InputFramework(Component):
    MOUSE_LEFT_BUTTON = 1
    MOUSE_MIDDLE_BUTTON = 2
    MOUSE_RIGHT_BUTTON = 3
    MOUSE_WHEEL_UP = 4
    MOUSE_WHEEL_DOWN = 5

    list_events = [
        pygame.QUIT,
        pygame.ACTIVEEVENT,
        pygame.KEYDOWN,
        pygame.KEYUP,
        pygame.MOUSEMOTION,
        pygame.MOUSEBUTTONUP,
        pygame.MOUSEBUTTONDOWN,
        pygame.MOUSEWHEEL,
        pygame.JOYAXISMOTION,
        pygame.JOYBALLMOTION,
        pygame.JOYHATMOTION,
        pygame.JOYBUTTONUP,
        pygame.JOYBUTTONDOWN,
        pygame.VIDEORESIZE,
        pygame.VIDEOEXPOSE,
        pygame.USEREVENT,
    ]

    def __init__(self, owner: object):
        super().__init__(owner)
        pygame.event.set_blocked(None)
        pygame.event.set_allowed([pygame.QUIT])
        self._player_input = PlayerInput()

        self.left_button: bool = False
        self.middle_button: bool = False
        self.right_button: bool = False
        self.mouse_position: tuple[int, int] = (0, 0)
        self.mouse_movement: tuple[int, int] = (0, 0)

    def set_allowed(self, events_allowed: list[Event]):
        pygame.event.set_blocked(None)
        if pygame.QUIT not in events_allowed:
            events_allowed.append(pygame.QUIT)
        pygame.event.set_allowed(events_allowed)
        logging.info(self._events_allowed())

    def _events_allowed(self):
        return "Events allowed: " + "".join(f"{pygame.event.event_name(event)}, "
                                            for event in self.list_events
                                            if not pygame.event.get_blocked(event)
                                            )

    def update(self, deltatime):
        super(InputFramework, self).update(deltatime)
        for event in pygame.event.get():
            if pygame.event.get_blocked(event.type):
                continue
            match event.type:
                case pygame.QUIT:
                    self._on_exit(event)
                case pygame.MOUSEWHEEL:
                    self._on_mouse_wheel(event)
                case pygame.MOUSEBUTTONDOWN:
                    self._on_mouse_button_down(event)
                case pygame.MOUSEBUTTONUP:
                    self._on_mouse_button_up(event)
                case pygame.MOUSEMOTION:
                    self._on_mouse_motion(event)
                case pygame.KEYDOWN:
                    self._on_key_down(event)
                case pygame.KEYUP:
                    self._on_key_up(event)

    def _on_mouse_wheel(self, event: Event):
        pass

    def _on_mouse_button_down(self, event: Event):
        match event.button:
            case self.MOUSE_LEFT_BUTTON:
                self._on_mouse_left_button_down(event)
            case self.MOUSE_MIDDLE_BUTTON:
                self._on_mouse_middle_button_down(event)
            case self.MOUSE_RIGHT_BUTTON:
                self._on_mouse_right_button_down(event)

    def _on_mouse_left_button_down(self, event: Event):
        self.left_button = event.buttons[0]
        self.mouse_position = event.pos

    def _on_mouse_middle_button_down(self, event: Event):
        self.middle_button = event.buttons[1]
        self.mouse_position = event.pos

    def _on_mouse_right_button_down(self, event: Event):
        self.right_button = event.buttons[2]
        self.mouse_position = event.pos

    def _on_mouse_button_up(self, event: Event):
        match event.button:
            case self.MOUSE_LEFT_BUTTON:
                self._on_mouse_left_button_up(event)
            case self.MOUSE_MIDDLE_BUTTON:
                self._on_mouse_middle_button_up(event)
            case self.MOUSE_RIGHT_BUTTON:
                self._on_mouse_right_button_up(event)

    def _on_mouse_left_button_up(self, event: Event):
        self.left_button = event.buttons[0]
        self.mouse_position = event.pos

    def _on_mouse_middle_button_up(self, event: Event):
        self.middle_button = event.buttons[1]
        self.mouse_position = event.pos

    def _on_mouse_right_button_up(self, event: Event):
        self.right_button = event.buttons[2]
        self.mouse_position = event.pos

    def _on_mouse_motion(self, event: Event):
        self.left_button = event.buttons[0]
        self.middle_button = event.buttons[1]
        self.right_button = event.buttons[2]
        self.mouse_position = event.pos
        self.mouse_movement = event.rel

    def _on_key_down(self, event: Event):
        pass

    def _on_key_up(self, event: Event):
        pass

    def _on_exit(self, event: Event):
        self._player_input.ask_to_exit = True
