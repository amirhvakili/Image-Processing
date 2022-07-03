# Converting all jpg files to png
# in pokedex folder and putting them
# into a new folder (called new) in the
# same directory

import sys
import os
from PIL import Image

# check if new/ exists, if not create
file_exists = os.path.exists('./pokedex/new')
if (not file_exists):
    os.mkdir('./pokedex/new')

# loop through pokedex,
# convert images to png
# save to the new folder

all_files = os.listdir('./pokedex')

for filename in all_files:
    if filename.endswith(".jpg"):
        im = Image.open(f"./pokedex/{filename}")
        name = f"{filename[:-4]}.png"
        rgb_im = im.convert('RGB')
        rgb_im.save(f"./pokedex/new/{name}")
        print(os.path.join('./pokedex', filename))
        continue
    else:
        continue
