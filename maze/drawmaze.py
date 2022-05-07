from PIL import Image

SIZE = 7

class Maze:
    # wall order: NESW
    __data = []
    
    def __init__(self):
        for _ in range(SIZE):
            self.__data.append([[0, 0, 0, 0] for _ in range(SIZE)])