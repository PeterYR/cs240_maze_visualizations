from drawmaze import MazeBlock

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