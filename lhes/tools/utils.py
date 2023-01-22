import csv
import logging
import pathlib

import pygame

from lhes.game import settings


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


def load_csv(
        relative_file_path: str,
        delimiter=";"
) -> list[list[str]]:
    csv_name = get_full_filename(relative_file_path)
    data = []
    with open(csv_name) as csv_file:
        layout = csv.reader(csv_file, delimiter=delimiter)
        data.extend(list(row) for row in layout)
        return data


def load_csv_as_dict(
        relative_file_path: str,
        delimiter=";"
) -> dict[str, dict[str, str]]:
    data = load_csv(relative_file_path, delimiter)
    result = {}
    for index_data, row in enumerate(data):
        if index_data == 0:
            continue
        row_result = {
            str.strip(data[0][index_row]): str.strip(value)
            for index_row, value in enumerate(row)
        }
        result[str.strip(row[0])] = row_result
    return result


def set_logger():
    logger = logging.getLogger()
    logger.setLevel(settings.LOG_LEVEL)
    formatter = logging.Formatter(settings.LOG_FORMAT)
    #
    file_handler = logging.FileHandler(settings.LOG_FILENAME)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    #
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


def restrict(
        value: float,
        value_min: float,
        value_max: float
) -> float:
    if value_max < value_min:
        value_min, value_max = value_max, value_min
    # print(f"restrict({value}, {value_min}, {value_max}) = {max(value_min, min(value, value_max))}")
    return max(value_min, min(value, value_max))
