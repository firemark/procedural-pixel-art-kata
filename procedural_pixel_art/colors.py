from PIL import ImageColor
from typing import List, Tuple
from random import randint


def get_hex_pallets():
	return [
		("DDA459", "B0975A", "D6975B"),
		("4EAEB2", "ADEFAF", "F0F5DF"),
		("7C8064", "B9C095", "EED190"),
		("11396C", "1F6378", "6F6B4D"),
		("585C59", "617974", "C2DFC4"),
		("803C50", "EC8357", "F0DC4E"),
		("C1D09E", "B4E49D", "8EB893"),
		("A7A986", "88304B", "42382C"),
		("38453F", "397B87", "A1CFB7"),
		("171A2A", "2F3D52", "3E5C84")
	]

def get_random_colors() -> List[Tuple[int, int, int]]:
	"""Get rgb colors from api. Apie return 5 colors"""
	print("Getting colors")
	hex_pallets = get_hex_pallets()
	number_of_pallets = len(hex_pallets)
	random_index = randint(0, number_of_pallets - 1)
	random_pallet = hex_pallets[random_index]
	return parse_hex_to_rgb(random_pallet)


def parse_hex_to_rgb(hex_colors):
	colors = []
	for hex_color in hex_colors:
		rgb_color = ImageColor.getcolor(f"#{hex_color}", "RGB")
		colors.append(rgb_color)
	return colors


if __name__ == "__main__":
	print(get_random_colors())
