import pygame

from lhes.game import settings


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

    def clear(self, color: pygame.Color = 'black') -> None:
        self._display_surface.fill(color)

    @staticmethod
    def draw() -> None:
        pygame.display.update()

    def get_camera_offset(self, camera_position: pygame.Vector2) -> None:
        return self._screen_offset - camera_position

    def _set_screen_offset(self) -> pygame.Vector2:
        return pygame.math.Vector2(self.half_width, self.half_height)

    def debug_draw(self, camera_position, visible_sprites):
        if not settings.DEBUG:
            return
        # for visible_sprite in visible_sprites:
        #     self._debug_draw_rect(visible_sprite.rect, settings.UI_BORDER_COLOR, camera_position)
        #     with contextlib.suppress(AttributeError):
        #         self._debug_draw_circle(visible_sprite.rect.center,
        #                                 visible_sprite.notice_radius, settings.UI_BORDER_COLOR, camera_position)
        #         self._debug_draw_circle(visible_sprite.rect.center,
        #                                 visible_sprite.attack_radius, settings.UI_BORDER_COLOR_ACTIVE,
        #                                 camera_position)
        #         self._debug_draw_rect(visible_sprite._collision_box, settings.UI_BORDER_COLOR_ACTIVE, camera_position)

    def _debug_draw_rect(
            self,
            rect: pygame.Rect,
            color: pygame.Color,
            camera_position: pygame.Vector2
    ) -> None:
        rect_to_draw: pygame.Rect = rect.copy()
        rect_to_draw.topleft += self.get_camera_offset(camera_position)
        pygame.draw.rect(self._display_surface, color, rect_to_draw, 3)

    def _debug_draw_circle(
            self,
            center: pygame.Vector2,
            radius: int,
            color: pygame.Color,
            camera_position: pygame.Vector2
    ) -> None:
        center += self.get_camera_offset(camera_position)
        pygame.draw.circle(self._display_surface, color, center, radius, 3)
