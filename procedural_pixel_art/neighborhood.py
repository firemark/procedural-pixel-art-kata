from typing import List, Tuple

from procedural_pixel_art.cells import Position


def get_only_abs_positions(positions):
    return [(x, y) for x, y in positions if x == abs(x) and y == abs(y)]


def get_neuman_neighborhood_positions(cell_coord: Position) -> List[Tuple[int, int]]:
    positions = (
        (cell_coord.x - 1, cell_coord.y),
        (cell_coord.x + 1, cell_coord.y),
        (cell_coord.x, cell_coord.y - 1),
        (cell_coord.x, cell_coord.y + 1),
    )
    return get_only_abs_positions(positions)


def get_moore_neighborhood_positions(cell_coord: Position) -> List[Tuple[int, int]]:
    positions = (
        (cell_coord.x - 1, cell_coord.y),
        (cell_coord.x + 1, cell_coord.y),
        (cell_coord.x, cell_coord.y - 1),
        (cell_coord.x, cell_coord.y + 1),
        (cell_coord.x - 1, cell_coord.y - 1),
        (cell_coord.x - 1, cell_coord.y + 1),
        (cell_coord.x + 1, cell_coord.y - 1),
        (cell_coord.x + 1, cell_coord.y + 1),
    )
    return get_only_abs_positions(positions)
