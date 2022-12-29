import pygame


class Screen:

    def __init__(self, width, height):
        # flags = pygame.FULLSCREEN | pygame.DOUBLEBUF
        # bits_per_pixel = 16
        # self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT), flags, bits_per_pixel)
        self.width = width
        self.height = height
        self.half_width = self.width // 2
        self.half_height = self.height // 2
        self._display_surface: pygame.Surface = pygame.display.set_mode((self.width, self.height))
        self._screen_offset: pygame.Vector2 = self._set_screen_offset()

    @property
    def display_surface(self):
        return self._display_surface

    def clear(self, color: pygame.Color = 'black') -> None:
        self._display_surface.fill(color)

    @staticmethod
    def draw() -> None:
        pygame.display.update()

    def get_camera_offset(self, camera_position: pygame.Vector2) -> pygame.Vector2:
        return self._screen_offset - camera_position

    def _set_screen_offset(self) -> pygame.Vector2:
        return pygame.math.Vector2(self.half_width, self.half_height)
