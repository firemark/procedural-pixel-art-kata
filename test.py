from pytest import mark

from procedural_pixel_art.grids import (
    GRID_HEIGHT,
    GRID_WIDTH,
    Position,
    add_neuman_border,
    create_grid_with_reflection,
    generate_random_grid,
    get_number_of_alive_neighbors,
    run_next_generation,
)


def get_empty_grid():
    return [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


def test__generate_random_grid_has_proper_size():
    grid = generate_random_grid()
    current_grid_height = len(grid)
    current_grid_width = len(grid[0])
    assert current_grid_height == GRID_HEIGHT
    assert current_grid_width == GRID_WIDTH


def test__random_grid_contains_only_two_states():
    grid = generate_random_grid()
    flatten_list = [cell for row in grid for cell in row]
    assert all(i in (0, 1) for i in flatten_list)


@mark.parametrize(
    "grid",
    [
        ([[0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]]),
        ([[0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0]]),
    ],
)
def test__alive_cell_with_enough_alive_neighbors_survive(grid):
    result = run_next_generation(grid)
    cell_with_enough_neighbors = result[1][1]
    assert cell_with_enough_neighbors == 1


def test__cell_die_without_required_number_of_neighbor():
    old_grid = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ]
    result = run_next_generation(old_grid)
    cell_with_1_neighbors = result[1][1]
    assert cell_with_1_neighbors == 0


def test__dead_grid_is_in_next_generation_full_of_life():
    empty_grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    result = run_next_generation(empty_grid)
    assert result == [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ]


def test__get_number_of_alive_neighbors():
    old_grid = [
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    cell_position = Position(0, 0)
    number_of_neighbors = get_number_of_alive_neighbors(old_grid, cell_position)
    assert number_of_neighbors == 0


@mark.parametrize(
    "grid,number_of_alive_neighbors",
    [
        ([[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0],], 1),
        ([[0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0],], 2),
        ([[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0],], 3),
        ([[1, 1, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0],], 8),
    ],
)
def test__get_number_of_alive_neighbors1(grid, number_of_alive_neighbors):
    cell_position = Position(1, 1)
    number_of_neighbors = get_number_of_alive_neighbors(grid, cell_position)
    assert number_of_neighbors == number_of_alive_neighbors


def test__dead_cell_without_neighbors_become_alive():
    old_grid = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    result = run_next_generation(old_grid)
    assert result == [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
    ]


def test__dead_cell_with_one_neighbor_become_alive():
    old_grid = [[1, 0]]
    result = run_next_generation(old_grid)
    assert result == [[0, 1]]


def test__make_mirror():
    empty_grid = [
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    result = create_grid_with_reflection(empty_grid)
    assert result == [
        [1, 1, 1, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]


@mark.parametrize(
    "old_grid,grid_with_border",
    [
        (
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],],
            [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],],
        ),
        (
            [[0, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0],],
            [[2, 0, 0, 0], [1, 2, 0, 0], [2, 0, 0, 0],],
        ),
        (
            [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1],],
            [[1, 1, 1, 1], [1, 2, 2, 1], [1, 1, 1, 1],],
        ),
        (
            [[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0],],
            [[0, 2, 2, 0], [2, 1, 1, 2], [0, 2, 2, 0],],
        ),
    ],
)
def test_transform_grid_with_neuman_border(old_grid, grid_with_border):
    result = add_neuman_border(old_grid)
    assert result == grid_with_border
