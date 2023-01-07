"""
https://en.wikipedia.org/wiki/Diamond-square_algorithm
The diamond-square algorithm starts with a two-dimensional grid, then randomly generates terrain height from
four seed values arranged in a grid of points so that the entire plane is covered in squares.
"""

import itertools
import random

from lhes.tools.array2d import SquareArray2D


def generate(
        n: int,
        seed: int = -1
) -> SquareArray2D:
    """
    Return a two-dimensional square grid,
    side length is (2 exposant n) + 1
    Each value of the grid is a terrain height
    """
    if seed != -1:
        random.seed(seed)
    side_length = (2 ** n) + 1
    result = SquareArray2D(side_length)
    _initialize_corners(result, side_length)
    _iteration = side_length - 1
    while _iteration > 1:
        _id = _iteration // 2
        _diamond_step(result, _iteration, _id, side_length)
        _square_step(result, _iteration, _id, side_length)
        _iteration = _id
    return result


def _initialize_corners(result: SquareArray2D, side_length: int):
    result.set(0, 0, random.randint(-side_length, side_length))
    result.set(0, side_length - 1, random.randint(-side_length, side_length))
    result.set(side_length - 1, 0, random.randint(-side_length, side_length))
    result.set(side_length - 1, side_length - 1, random.randint(-side_length, side_length))


def _diamond_step(result: SquareArray2D, iteration: int, _id: int, side_length: int):
    for x, y in itertools.product(range(_id, side_length, iteration), range(_id, side_length, iteration)):
        average = int((result.get(x - _id, y - _id) + result.get(x - _id, y + _id) +
                       result.get(x + _id, y - _id) + result.get(x + _id, y + _id)) / 4)
        result.set(x, y, average + random.randint(-_id, _id))


def _square_step(result: SquareArray2D, iteration: int, _id: int, side_length: int):
    offset = 0
    for x in range(0, side_length, _id):
        offset = _id if offset == 0 else 0
        for y in range(offset, side_length, iteration):
            _sum = 0
            n = 0
            if x >= _id:
                _sum += result.get(x - _id, y)
                n += 1
            if (x + _id) < side_length:
                _sum += result.get(x + _id, y)
                n += 1
            if y >= _id:
                _sum += result.get(x, y - _id)
                n += 1
            if (y + _id) < side_length:
                _sum += result.get(x, y + _id)
                n += 1
            result.set(x, y, int(_sum / n) + random.randint(-_id, _id))
