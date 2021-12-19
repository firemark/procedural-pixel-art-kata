from PIL import Image, ImageColor
from typing import List, Tuple
from random import random, uniform
from array import array


def get_random_colors() -> List[Tuple[int, int, int]]:
    base_color = get_random_color()
    r = random()
    if r < 0.33:
        complementary_color = get_complementary_color(base_color)
        colors = base_color, mutate_color(base_color), mutate_color(complementary_color)
    elif r < 0.66:
        second_color, third_color = get_triadic_colors(base_color)
        colors = base_color, mutate_color(second_color), mutate_color(third_color)
    else:
        colors = base_color, mutate_color(base_color), mutate_color(base_color)

    return [hsv_to_rgb(color) for color in colors]


def get_random_color():
    h = random()
    s = uniform(0.5, 0.8)
    v = uniform(0.5, 0.8)
    return (h, s, v)


def get_complementary_color(base_color):
    h, s, v = base_color
    h = (h + 0.5) % 1.0
    return (h, s, v)


def get_triadic_colors(base_color):
    h, s, v = base_color
    h1 = (h + 0.33) % 1.0
    h2 = (h + 0.66) % 1.0
    return ((h1, s, v), (h2, s, v))


def mutate_color(color):
    h, s, v = color
    h = (h + uniform(-0.1, 0.1)) % 1.0
    s += uniform(-0.5, +0.2)
    v += uniform(-0.5, +0.2)
    return (h, s, v)


def hsv_to_rgb(color) -> Tuple[int, int, int]:
    h, s, v = color
    css_format = f"hsv({int(h * 360)},{int(s * 100)}%,{int(v * 100)}%)"
    return ImageColor.getrgb(css_format)


if __name__ == "__main__":
    pallete = get_random_colors()
    arr = array("B", pallete[0] + pallete[1] + pallete[2])
    img = Image.frombytes("RGB", (3, 1), bytes(arr))
    img = img.resize((256, 256), resample=Image.NEAREST)
    img.show()
