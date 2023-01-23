import pygame.sprite

from lhes.game import settings
from lhes.game.player_input import PlayerInput
from lhes.game.world.map_size import MapSize
from lhes.tools.camera import Camera


class CameraGroup(pygame.sprite.Group):

    def __init__(self, display_rect: pygame.Rect, map_size: MapSize):
        super().__init__()

        # display rect
        self._display_rect = display_rect

        # map surface
        self._map_size = pygame.Vector2(map_size, map_size)
        self._map_pixel_size_vector: pygame.Vector2 = self._map_size * settings.TILE_SIZE
        self._map_surface = pygame.Surface(self._map_pixel_size_vector)
        self._map_rect = self._map_surface.get_rect()

        # scaled map surface

        self._camera = Camera(self._display_rect)
        self._offset: pygame.Vector2 = pygame.Vector2(0, 0)
        self._player_input: PlayerInput = PlayerInput()

    def __str__(self):
        return f"CameraGroup - {self._camera}, " \
               f"offset map vs screen: {self._offset} ; " \
               f"Map - size: {self._map_size}, pixel size: {self._map_pixel_size_vector}"

    def custom_draw(
            self,
            surface: pygame.Surface,
            ground_surface: pygame.Surface
    ):
        self._clear(surface)
        self._draw_ground(ground_surface)
        self._draw_y_sorted_sprites()
        scaled_rect, scaled_surf = self._zoom(pygame.Vector2(surface.get_size()) / 2)
        rect = surface.get_rect()
        self._offset.x = (rect.width - scaled_rect.width) // 2
        self._offset.y = (rect.height - scaled_rect.height) // 2
        self._blit_surface(surface, scaled_rect, scaled_surf)

    def _clear(self, surface):
        self._map_surface.fill('black')
        surface.fill('black')

    def _draw_ground(self, ground_surface: pygame.Surface) -> None:
        if ground_surface is None:
            return
        ground_rect = ground_surface.get_rect(topleft=(0, 0))
        ground_offset = pygame.Vector2(ground_rect.topleft) - self._camera.position
        self._map_surface.blit(ground_surface, ground_offset)

    def _draw_y_sorted_sprites(self) -> None:
        for sprite in sorted(self.sprites(), key=lambda sprite_y: sprite_y.rect.centery):
            self._draw_sprite(sprite)

    def _draw_sprite(self, sprite: pygame.sprite.Sprite) -> None:
        self._map_surface.blit(sprite.image, sprite.rect.topleft)

    def _zoom(self, surface_half_size_vector: pygame.Vector2):
        scaled_surf = pygame.transform.scale(self._map_surface,
                                             self._map_pixel_size_vector * self._camera.zoom_scale)
        # scaled_rect = scaled_surf.get_rect(topleft=(0, 0))
        scaled_rect = scaled_surf.get_rect(center=surface_half_size_vector - self._camera.position)
        # scaled_rect = scaled_surf.get_rect(center=self._map_rect.center)
        return scaled_rect, scaled_surf

    def _blit_surface(self, surface: pygame.Surface, scaled_rect: pygame.Rect, scaled_surf: pygame.Surface):
        # self._restrict_camera_position(scaled_rect, surface)
        rect = self._display_rect
        surface.blit(scaled_surf, scaled_rect)

    @staticmethod
    def _restrict_camera_position(scaled_rect, surface):
        rect = surface.get_rect()
        scaled_rect.left = min(rect.left, scaled_rect.left)
        scaled_rect.top = min(rect.top, scaled_rect.top)
        scaled_rect.right = max(rect.right, scaled_rect.right)
        scaled_rect.bottom = max(rect.bottom, scaled_rect.bottom)
        if scaled_rect.width < rect.width:
            scaled_rect.centerx = rect.centerx
        if scaled_rect.height < rect.height:
            scaled_rect.centery = rect.centery

    def update(self, deltatime) -> None:
        self._camera.update(deltatime)
        self._on_left_mouse_button_down()

    def _on_left_mouse_button_down(self):
        if not self._player_input.left_button_clicked:
            return
        if not self._display_rect.collidepoint(self._player_input.mouse_position):
            return
        for sprite in self.sprites():
            position = pygame.Vector2(self._player_input.mouse_position) - self._offset
            position = self._camera.screen_to_world(position)
            if sprite.rect.collidepoint(position):
                print("camera_group.on_left_mouse_button_down", self._player_input.mouse_status())
                # print(f"camera_group.on_left_mouse_button_down, Offset map vs screen: {self._offset}")
                # print(f"camera_group.on_left_mouse_button_down, Position: {position}")
                # print(f"camera_group.on_left_mouse_button_down, Sprite rect: {sprite.rect}")
                print(f"camera_group.on_left_mouse_button_down, Camera: {self}")
                print(f"camera_group.on_left_mouse_button_down, Sprite: {sprite}")
