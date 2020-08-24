import copy
from collections.abc import Iterable
from random import randint
from typing import List

from procedural_pixel_art.cells import (
    Position,
    is_alive,
    is_dead,
    is_to_kill,
    is_to_revive,
)
from procedural_pixel_art.neighborhood import (
    get_moore_neighborhood_positions,
    get_neuman_neighborhood_positions,
)

GRID_HEIGHT = 10
GRID_WIDTH = 5


def generate_random_grid() -> List[List[int]]:
    return [[randint(0, 1) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


def create_grid_with_reflection(grid: List[List[int]]) -> List[List[int]]:
    """Return grid extended by mirror reflection on the right side."""
    reflection = map(lambda x: x[::-1], grid)
    return [x + y for x, y in zip(grid, reflection)]


def run_next_generation(old_grid: List[List[int]]) -> List[List[int]]:
    new_grid = copy.deepcopy(old_grid)
    cells_to_kill = get_cells_position_to_kill(old_grid)
    for x, y in cells_to_kill:
        new_grid[x][y] = 0
    cells_to_survive = get_cells_position_to_revive(old_grid)
    for x, y in cells_to_survive:
        new_grid[x][y] = 1
    return new_grid


def get_cells_position_to_kill(grid: List[List[int]]) -> Iterable:
    alive_cells_coords = get_alive_cells_coords(grid)
    return get_cell_positions_on_neighbors_number_condition(
        grid, alive_cells_coords, is_to_kill
    )


def get_cells_position_to_revive(grid: List[List[int]]) -> Iterable:
    dead_cells_coord = get_dead_cells_coords(grid)
    return get_cell_positions_on_neighbors_number_condition(
        grid, dead_cells_coord, is_to_revive
    )


def get_cell_positions_on_neighbors_number_condition(
    grid, cells_positions, condition_func
):
    for x, y in cells_positions:
        cell_coord = Position(x=x, y=y)
        number_of_alive_neighbors = get_number_of_alive_neighbors(grid, cell_coord)
        if condition_func(number_of_alive_neighbors):
            yield x, y


def get_neighbors_vitality_status(cell_coords, old_grid: List[List[int]]) -> Iterable:
    for x, y in get_moore_neighborhood_positions(cell_coords):
        try:
            yield old_grid[x][y]
        except IndexError:
            continue


def get_number_of_alive_neighbors(
    grid: List[List[int]], cell_position: Position
) -> int:
    number_of_alive_neighbors = 0
    neighbors_values = get_neighbors_vitality_status(cell_position, grid)
    for cell in neighbors_values:
        if is_alive(cell):
            number_of_alive_neighbors += 1
    return number_of_alive_neighbors


def add_neuman_border(grid: List[List[int]]) -> List[List[int]]:
    """surround living cells with a border"""
    new_grid = copy.deepcopy(grid)
    neuman_border_positions = get_cells_positions_for_border(grid)
    for x, y in neuman_border_positions:
        try:
            cell_value = grid[x][y]
        except IndexError:
            continue
        if is_dead(cell_value):
            new_grid[x][y] = 2
    return new_grid


def get_cells_positions_for_border(grid):
    neuman_neighbors_coords = []
    alive_coords = get_alive_cells_coords(grid)
    for x, y in alive_coords:
        cell_coords = Position(x, y)
        neighbors_coords = get_neuman_neighborhood_positions(cell_coords)
        neuman_neighbors_coords.extend(neighbors_coords)
    return neuman_neighbors_coords


def get_alive_cells_coords(grid: List[List[int]]):
    return get_cell_positions_on_value_condition(grid, is_alive)


def get_dead_cells_coords(grid: List[List[int]]) -> Iterable:
    return get_cell_positions_on_value_condition(grid, is_dead)


def get_cell_positions_on_value_condition(grid, condition_func):
    for x_index, value in enumerate(grid):
        for y_index, _ in enumerate(value):
            cell_value = grid[x_index][y_index]
            if condition_func(cell_value):
                yield x_index, y_index


def grid_to_rgb_array(grid: List[List[int]]) -> Iterable:
    """
   Transform grid to rgb colors.
    """
    for row in grid:
        for cell in row:
            if cell == 1:
                yield from [128, 0, 0]  # brown color
            elif cell == 2:
                yield from [255, 255, 0]  # yellow color
            else:
                yield from [0, 0, 0]  # black color
