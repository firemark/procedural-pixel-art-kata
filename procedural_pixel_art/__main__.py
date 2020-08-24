import argparse
import os
import sys
from datetime import datetime

# ugly trick to find this module
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from procedural_pixel_art.art_generator import PixelArt

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "-s", dest="save", default=False, action="store_true", help="Save art as png file"
)
args = parser.parse_args()


art = PixelArt()
if args.save:
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    art.save(f"generated_pixel_art_{timestamp}")
art.show()
