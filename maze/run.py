import json
import requests
from drawmaze import MazeBlock
from PIL import Image

try:
    data = requests.get('http://sp22-cs240-adm.cs.illinois.edu:24000/mazeState').json()
    print(f'Loaded {len(data)} blocks')
    with open('maze_data.json', 'w') as fp:
        json.dump(data, fp)
except:
    with open('maze_data.json', 'r') as fp:
        data = json.load(fp)
    print(f'Connection failed, loaded {len(data)} blocks from `maze_data.json`')

#TODO: find minimum row and col, adjust data to have non-negative coords





# 503 error segment
data = ["9a8088c","5b02024","5b49494","0a02020","5b4d1e5","1e571e5","3a282a6"]
mb = MazeBlock((255, 0, 0))
mb.parse_data(data)
mb.export().save('err_503.png')

# given segment
data = ["9aa2aac", "59aaaa4", "51aa8c5", "459a651", "553ac55", "559a655", "3638a26"]
mb = MazeBlock((0, 255, 255))
mb.parse_data(data)
mb.export().save('given.png')