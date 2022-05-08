import json
import requests
from PIL import Image, ImageColor
from drawmaze import MazeBlock
from constants import WIDTH, CELL_SIZE

try:
    raw_data = requests.get('http://sp22-cs240-adm.cs.illinois.edu:24000/mazeState', timeout = 5).json()
    print(f'Loaded {len(raw_data)} blocks')
    with open('maze_data.json', 'w') as fp:
        json.dump(raw_data, fp)
except:
    with open('maze_data.json', 'r') as fp:
        raw_data = json.load(fp)
    print(f'Connection failed, loaded {len(raw_data)} blocks from `maze_data.json`')

# find minimum row and col
min_row = min([int(x.split('_')[0]) for x in raw_data.keys()])
min_col = min([int(x.split('_')[1]) for x in raw_data.keys()])
max_row = max([int(x.split('_')[0]) for x in raw_data.keys()])
max_col = max([int(x.split('_')[1]) for x in raw_data.keys()])

# adjust add coords to be non-negative
data = {}
for key, val in raw_data.items():
    row, col = [int(x) for x in key.split('_')]
    data[(row - min_row, col - min_col)] = val

# create image
block_size = CELL_SIZE * WIDTH
width_blocks = max_col - min_col + 1
height_blocks = max_row - min_row + 1
image = Image.new('RGBA', (block_size * width_blocks + 1, block_size * height_blocks + 1))

for key, val in data.items():
    img_loc = [n * CELL_SIZE * WIDTH for n in key]
    img_loc.reverse()
    color = ImageColor.getcolor(f'#{val[1]}', 'RGB')

    mb = MazeBlock(color=color)
    if type(val[0]) is dict:
        geom = val[0]['geom']
    else:
        geom = val[0]

    mb.parse_data(geom)
    image.paste(mb.export(), img_loc)

image.save('output.png')