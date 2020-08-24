import array
from typing import List, Tuple

from PIL import Image

from procedural_pixel_art.grids import (
    add_neuman_border,
    create_grid_with_reflection,
    generate_random_grid,
    grid_to_rgb_array,
    run_next_generation,
)


class PixelArt:
    def __init__(self):
        self.raw_array = self._generate()

    def _generate(self) -> List[List[int]]:
        grid = generate_random_grid()
        new_grid = run_next_generation(grid)
        new_grid = run_next_generation(new_grid)
        new_grid = create_grid_with_reflection(new_grid)
        return add_neuman_border(new_grid)

    def _generate_image(self, size: Tuple[int, int]) -> Image:
        width = len(self.raw_array[0])
        height = len(self.raw_array)

        grid_of_rgb_colors = grid_to_rgb_array(self.raw_array)
        image = array.array("B", grid_of_rgb_colors)

        colors = bytes(image)
        img = Image.frombytes("RGB", (width, height), colors)
        img = img.resize(size, resample=Image.NEAREST)
        return img

    def save(self, name, size=(128, 128)):
        """Save grid to a png file."""
        img = self._generate_image(size)
        img.save(f"{name}.png")

    def show(self, size=(128, 128)):
        img = self._generate_image(size)
        img.show()
