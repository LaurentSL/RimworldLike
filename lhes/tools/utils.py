import csv
import pathlib

import pygame


def load_image_and_rect(relative_file_path: str,
                        position: tuple[int, int] = (0, 0),
                        anchor: str = 'topleft'
                        ) -> tuple[pygame.Surface, pygame.Rect]:
    image_name = get_full_filename(relative_file_path)
    image = pygame.image.load(image_name).convert_alpha()
    if anchor == 'center':
        rect = image.get_rect(center=position)
    else:
        rect = image.get_rect(topleft=position)
    return image, rect


def import_all_images_and_rect_from_folder(relative_folder_path: str) -> list[tuple[pygame.Surface, pygame.Rect]]:
    surface_list = []
    folder_path = get_full_filename(relative_folder_path)
    for file in folder_path.glob("*.*"):
        image_surface, image_rect = load_image_and_rect(file)
        surface_list.append((image_surface, image_rect))
    return surface_list


def get_full_filename(relative_file_path: str) -> pathlib.Path:
    file_path = pathlib.Path(__file__).resolve().parent
    return file_path / relative_file_path


def import_csv_layout(relative_file_path: str) -> list[list[str]]:
    csv_name = get_full_filename(relative_file_path)
    terrain_map = []
    with open(csv_name) as level_map:
        layout = csv.reader(level_map, delimiter=",")
        terrain_map.extend(list(row) for row in layout)
        return terrain_map
