import argparse
import os
import sys
from datetime import datetime

# ugly trick to find this module
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from procedural_pixel_art.art_generator import PixelArt


def positive_int(x):
    x = int(x)
    if 0 < x:
        raise argparse.ArgumentTypeError("Can't generate negative number of arts")
    return x


parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "-s", "--save", dest="save", default=False, action="store_true", help="Save art as png file"
)
parser.add_argument(
    "-o", "--open", dest="open", default=False, action="store_true", help="Show generated_pixel"
)

parser.add_argument("-n", "--number", default =1,type=int, choices=range(1, 101), help="generate defined number of arts")

args = parser.parse_args()

arts = [PixelArt() for _ in range(args.number)]
# art = PixelArt()
for art in arts:
    if args.save:
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        art.save(f"generated_pixel_art_{timestamp}")
    if args.open:
        art.show()
