import requests
from lxml.etree import fromstring
from PIL import ImageColor
from typing import List, Tuple


def get_default_colors():
    return [(128, 0, 0), (255, 255, 0), (0, 0, 0)]


def get_random_colors() -> List[Tuple[int, int, int]]:
    """Get rgb colors from api. Apie return 5 colors"""
    response = requests.get("http://www.colourlovers.com/api/palettes/random")
    if response.status_code == 200:
        hex_colors = get_hex_colors_from_xml(response.content)
        if len(hex_colors) >= 3:
            return parse_hex_to_rgb(hex_colors)
    print("Problem with API colors, returning default colors")
    return get_default_colors()


def parse_hex_to_rgb(hex_colors):
    colors = []
    for hex_ in hex_colors:
        color = hex_.text
        rgb_color = ImageColor.getcolor(f"#{color}", "RGB")
        colors.append(rgb_color)
    return colors


def get_hex_colors_from_xml(xml: str) -> List[str]:
    xml_content = fromstring(xml)
    try:
        path_to_xml_colors = '/palettes/palette/colors'
        return xml_content.xpath(path_to_xml_colors)[0]
    except IndexError:
        return []


if __name__ == "__main__":
    print(get_random_colors())
