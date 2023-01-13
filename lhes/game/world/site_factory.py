import itertools

import pygame

from lhes.game.world.location import Location
from lhes.game.world.terrain import Terrain
from lhes.tools import diamond_square_algorithm
from lhes.tools.array2d import SquareArray2D


class SiteFactory:

    @staticmethod
    def generate_by_random_method(
            size: int,
            location_group: pygame.sprite.Group
    ) -> SquareArray2D:
        grid: SquareArray2D = SquareArray2D(size, None)
        for row, column in itertools.product(range(size), range(size)):
            position = pygame.Vector2(column, row)
            terrain = Terrain.get_random()
            location = Location([location_group], position, terrain)
            grid.set(column, row, location)
        return grid

    @staticmethod
    def generate_by_diamond_square(size: int, location_group: pygame.sprite.Group) -> list[list[Location]]:
        heightmap = diamond_square_algorithm.generate(4)
        grid: list[list[Location]] = []
        for row in range(size):
            locations = []
            for column in range(size):
                position = pygame.Vector2(column, row)
                terrain = Terrain.get_random()
                locations.append(Location([location_group], position, terrain))
            grid.append(locations)
        return grid
