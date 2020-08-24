from typing import NamedTuple

NUMBER_OF_NEIGHBORS_TO_SURVIVE = (2, 3)
NUMBER_OF_NEIGHBORS_TO_REVIVE = (0, 1)


class Position(NamedTuple):
    x: int
    y: int


def is_to_revive(number_of_alive_neighbors) -> bool:
    return number_of_alive_neighbors in NUMBER_OF_NEIGHBORS_TO_REVIVE


def is_to_kill(number_of_alive_neighbors) -> bool:
    return number_of_alive_neighbors not in NUMBER_OF_NEIGHBORS_TO_SURVIVE


def is_dead(cell_value: int) -> bool:
    return cell_value == 0


def is_alive(cell_value) -> bool:
    return cell_value == 1
