import requests
from PIL import Image, ImageDraw

data = requests.get('http://sp22-cs240-adm.cs.illinois.edu:24000/mazeState').json()
print(f'Loaded {len(data)} blocks')

rows = set()
cols = set()

coords = []
for key in data.keys():
    loc = key.split('_')
    r = int(loc[0])
    c = int(loc[1])

    coords.append([r, c])
    rows.add(r)
    cols.add(c)

# adjust to be non-negative
min_row = min(rows)
min_col = min(cols)

for coord in coords:
    coord[0] -= min_row
    coord[1] -= min_col

# create image
img_width = max(cols) - min(cols) + 1
img_height = max(rows) - min(rows) + 1
print(f'Image dimensions: ({img_width}, {img_height})')

image = Image.new('RGB', (img_width, img_height), color='black')
pixels = image.load()

# draw pixels
for coord in coords:
    pixels[coord[1], coord[0]] = (233, 192, 255)


image.save('grid.png')
